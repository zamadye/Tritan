#!/usr/bin/env bash
# ===========================================================================
# Extract hermes-airdrop-agent into its own repository.
# ===========================================================================
#
# This project currently lives as a subdirectory of an unrelated repository
# (Tritan, a Polymarket prediction-market trading agent). It should not: the
# domains, dependencies and lifecycles have nothing in common, and sharing a
# .gitignore already caused a real bug -- an unanchored `skills/` rule in the
# parent repo silently swallowed this project's SKILL.md files.
#
#   ./scripts/extract-standalone.sh                  # build the branch, stop
#   ./scripts/extract-standalone.sh --push <remote>  # and push it
#   ./scripts/extract-standalone.sh --dir <path>     # export a clean worktree
#
# Uses `git subtree split`, which rewrites history so the extracted branch has
# this directory as its ROOT and keeps all commit messages. Nothing in the
# parent repository is modified.
#
# NOTE: the agent that built this project runs in a session bound to a single
# branch and cannot create repositories. Run this yourself.
# ===========================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
PREFIX="$(basename "$PROJECT_DIR")"

# Walk up to the enclosing git repository.
REPO="$(cd "$PROJECT_DIR" && git rev-parse --show-toplevel)"
BRANCH="${HAA_EXTRACT_BRANCH:-hermes-airdrop-agent}"
PUSH_REMOTE=""
EXPORT_DIR=""

while (( $# )); do
  case "$1" in
    --push) PUSH_REMOTE="${2:?--push needs a remote name or URL}"; shift 2 ;;
    --dir)  EXPORT_DIR="${2:?--dir needs a path}"; shift 2 ;;
    --branch) BRANCH="${2:?--branch needs a name}"; shift 2 ;;
    -h|--help) sed -n '2,24p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

if ! git -C "$REPO" ls-files --error-unmatch "$PROJECT_DIR" >/dev/null 2>&1; then
  echo "✗ $PROJECT_DIR is not tracked in $REPO — commit it first." >&2
  exit 1
fi

echo "Repository : $REPO"
echo "Extracting : $PREFIX/  ->  branch '$BRANCH'"
echo

# ---------------------------------------------------------------- split ----
if git -C "$REPO" show-ref --verify --quiet "refs/heads/$BRANCH"; then
  echo "  ! branch '$BRANCH' already exists — deleting and rebuilding"
  git -C "$REPO" branch -D "$BRANCH" >/dev/null
fi
git -C "$REPO" subtree split --prefix="$PREFIX" -b "$BRANCH" >/dev/null
echo "  ✓ branch '$BRANCH' created"

# --------------------------------------------------------------- verify ----
# The branch name usually collides with the directory name, so every reference
# must be fully qualified or git reports "ambiguous argument".
REF="refs/heads/$BRANCH"

FILES=$(git -C "$REPO" ls-tree -r --name-only "$REF" | wc -l | tr -d ' ')
COMMITS=$(git -C "$REPO" rev-list --count "$REF")
# The extracted branch must not contain anything from the parent project.
# `|| true` matters: with `set -o pipefail`, a grep that finds nothing exits 1
# and would kill the script at exactly the moment it should report success.
LEAKED=$(git -C "$REPO" ls-tree -r --name-only "$REF" \
         | { grep -E '^(agent/|web/|main\.py$|requirements\.txt$)' || true; } | wc -l | tr -d ' ')

echo "  ✓ $FILES files, $COMMITS commits"
if [[ "$LEAKED" != "0" ]]; then
  echo "  ✗ parent-project files leaked into the extracted branch:" >&2
  git -C "$REPO" ls-tree -r --name-only "$REF" \
    | grep -E '^(agent/|web/|main\.py$|requirements\.txt$)' | sed 's/^/      /' >&2
  exit 1
fi
echo "  ✓ no parent-project files present"

# Root of the extracted branch should be this project, not a wrapper dir.
if ! git -C "$REPO" cat-file -e "$REF:install.sh" 2>/dev/null; then
  echo "  ✗ install.sh is not at the root of the extracted branch" >&2
  exit 1
fi
echo "  ✓ install.sh is at the root"

# ---------------------------------------------------------------- export ---
if [[ -n "$EXPORT_DIR" ]]; then
  rm -rf "$EXPORT_DIR"
  git -C "$REPO" worktree add --detach "$EXPORT_DIR" "$REF" >/dev/null 2>&1 \
    || git -C "$REPO" clone --branch "$BRANCH" --single-branch "$REPO" "$EXPORT_DIR" >/dev/null
  rm -rf "$EXPORT_DIR/.git"
  ( cd "$EXPORT_DIR" && git init -q && git add -A \
      && git -c user.name="${GIT_AUTHOR_NAME:-extract}" \
             -c user.email="${GIT_AUTHOR_EMAIL:-extract@localhost}" \
             commit -qm "Initial import from ${PREFIX}/" )
  echo "  ✓ exported a clean working copy to $EXPORT_DIR"
fi

# ------------------------------------------------------------------ push ---
if [[ -n "$PUSH_REMOTE" ]]; then
  echo
  echo "Pushing '$BRANCH' to $PUSH_REMOTE ..."
  if git -C "$REPO" remote get-url "$PUSH_REMOTE" >/dev/null 2>&1; then
    git -C "$REPO" push "$PUSH_REMOTE" "$BRANCH:main"
  else
    git -C "$REPO" push "$PUSH_REMOTE" "$BRANCH:main"
  fi
  echo "  ✓ pushed to $PUSH_REMOTE as 'main'"
else
  cat <<NEXT

Done. The extracted history is on branch '$BRANCH' in $REPO.

To publish it as its own repository:

  gh repo create hermes-airdrop-agent --private
  git -C "$REPO" remote add haa https://github.com/<you>/hermes-airdrop-agent.git
  git -C "$REPO" push haa $BRANCH:main

Or export a clean copy and start fresh:

  $0 --dir /tmp/hermes-airdrop-agent

NEXT
fi
