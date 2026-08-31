"""Hard-stop guardrails.

These are the conditions under which the agent must *stop and hand control to a
human* rather than continue. Each is a pure function so the behaviour is
testable without a browser or a model.

The rules implemented here come from two sources:

* **Hermes' own "Take Over" pattern** — Manus and Hermes both pause for the
  human on CAPTCHA / MFA instead of trying to defeat it. Solving a CAPTCHA is
  not something this system does, by design.
* **This project's own policy** — no private key material is ever stored, and
  no wallet transaction is issued without explicit operator approval.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum

# ---------------------------------------------------------------------------
# Secret material detection
# ---------------------------------------------------------------------------

#: A 64-hex-char string, with or without a 0x prefix. Matches EVM private keys.
_HEX64_RE = re.compile(r"\b(?:0x)?[0-9a-fA-F]{64}\b")

#: Common private-key / seed labels an operator might paste into .env.
_KEY_LABEL_RE = re.compile(
    r"(?i)\b(private[_\-\s]?key|secret[_\-\s]?key|seed[_\-\s]?phrase|mnemonic|"
    r"recovery[_\-\s]?phrase|keystore[_\-\s]?json|signing[_\-\s]?key)\b"
)

#: base58-ish blob of the length used by Solana secret keys.
_B58_RE = re.compile(r"\b[1-9A-HJ-NP-Za-km-z]{87,89}\b")

#: PEM-encoded private key block.
_PEM_RE = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")


class HaltReason(str, Enum):
    """Why execution must stop."""

    CAPTCHA = "captcha"
    MFA = "mfa"
    PRIVATE_KEY = "private_key"
    SIGNATURE_REQUEST = "signature_request"
    APPROVAL_REQUIRED = "approval_required"
    LOGIN_EXPIRED = "login_expired"
    UNKNOWN_PAGE = "unknown_page"
    SPEND_LIMIT = "spend_limit"


@dataclass(frozen=True)
class Halt:
    """A stop condition. ``actionable`` tells the operator what to do."""

    reason: HaltReason
    detail: str
    actionable: str

    def __str__(self) -> str:
        return f"HALT[{self.reason.value}]: {self.detail} — {self.actionable}"


def classify_secret_material(text: str | None) -> str | None:
    """Identify wallet key material in a string.

    Returns a short label (``"evm-private-key"`` etc.) or ``None``. Only the
    label is ever returned — never the matched value.
    """
    if not text:
        return None
    t = text.strip()
    if len(t) < 12:
        return None
    if _PEM_RE.search(t):
        return "pem-private-key"
    # A labelled key is a hit even if the value is oddly formatted.
    if _KEY_LABEL_RE.search(t):
        return "labelled-private-key"
    if _HEX64_RE.search(t):
        return "evm-private-key"
    if _B58_RE.search(t):
        return "solana-secret-key"
    if _looks_like_mnemonic(t):
        return "mnemonic-phrase"
    return None


_BIP39_SAMPLE = frozenset(
    """abandon ability able about above absent absorb abstract absurd abuse access accident
account accuse achieve acid acoustic acquire across act action actor actress actual adapt add
address adjust admit adult advance advice aerobic affair afford afraid again age agent agree
ahead aim air airport aisle alarm album alcohol alert alien all alley allow almost alone alpha
already also alter always amateur amazing among amount amused analyst anchor ancient anger angle
angry animal ankle announce annual another answer antenna antique anxiety any apart apology
appear apple approve april arch arctic area arena argue arm armed armor army around arrange
arrest arrive arrow art artefact artist artwork ask aspect assault asset assist assume asthma
athlete atom attack attend attitude attract auction audit august aunt author auto autumn average
avocado avoid awake aware away awesome awful awkward axis baby bachelor bacon badge bag balance
balcony ball bamboo banana banner bar barely bargain barrel base basic basket battle beach bean
beauty because become beef before begin behave behind believe below belt bench benefit best betray
better between beyond bicycle bid bike bind biology bird birth bitter black blade blame blanket
blast bleak bless blind blood blossom blouse blue blur blush board boat body boil bomb bone bonus
book boost border boring borrow boss bottom bounce box boy bracket brain brand brass brave bread
breeze brick bridge brief bright bring brisk broccoli broken bronze broom brother brown brush
bubble buddy budget buffalo build bulb bulk bullet bundle bunker burden burger burst bus business
busy butter buyer buzz cabbage cabin cable cactus cage cake call calm camera camp can canal cancel
candy cannon canoe canvas canyon capable capital captain car carbon card cargo carpet carry cart
case cash casino castle casual cat catalog catch category cattle caught cause caution cave ceiling
celery cement census century cereal certain chair chalk champion change chaos chapter charge chase
chat cheap check cheese chef cherry chest chicken chief child chimney choice choose chronic chuckle
chunk churn cigar cinnamon circle citizen city civil claim clap clarify claw clay clean clerk clever
click client cliff climb clinic clip clock clog close cloth cloud clown club clump cluster clutch
coach coast coconut code coffee coil coin collect color column combine come comfort comic common
company concert conduct confirm congress connect consider control convince cook cool copper copy
coral core corn correct cost cotton couch country couple course cousin cover coyote crack cradle
craft cram crane crash crater crawl crazy cream credit creek crew cricket crime crisp critic crop
cross crouch crowd crucial cruel cruise crumble crunch crush cry crystal cube culture cup cupboard
curious current curtain curve cushion custom cute cycle dad damage damp dance danger daring dash
daughter dawn day deal debate debris decade december decide decline decorate decrease deer defense
define defy degree delay deliver demand demise denial dentist deny depart depend deposit depth deputy
derive describe desert design desk despair destroy detail detect develop device devote diagram dial
diamond diary dice diesel diet differ digital dignity dilemma dinner dinosaur direct dirt disagree
discover disease dish dismiss disorder display distance divert divide divorce dizzy doctor document
dog doll dolphin domain donate donkey donor door dose double dove draft dragon drama drastic draw
dream dress drift drill drink drip drive drop drum dry duck dumb dune during dust dutch duty dwarf
dynamic eager eagle early earn earth easily east easy echo ecology economy edge edit educate effort
egg eight either elbow elder electric elegant element elephant elevator elite else embark embody
embrace emerge emotion employ empower empty enable enact end endless endorse enemy energy enforce
engage engine enhance enjoy enlist enough enrich enroll ensure enter entire entry envelope episode
equal equip era erase erode erosion error erupt escape essay essence estate eternal ethics evidence
evil evoke evolve exact example excess exchange excite exclude excuse execute exercise exhaust
exhibit exile exist exit exotic expand expect expire explain expose express extend extra eye eyebrow
fabric face faculty fade faint faith fall false fame family famous fan fancy fantasy farm fashion
fat fatal father fatigue fault favorite feature february federal fee feed feel female fence festival
fetch fever few fiber fiction field figure file film filter final find fine finger finish fire firm
first fiscal fish fit fitness fix flag flame flash flat flavor flee flight flip float flock floor
flower fluid flush fly foam focus fog foil fold follow food foot force forest forget fork fortune
forum forward fossil foster found fox fragile frame frequent fresh friend fringe frog front frost
frown frozen fruit fuel fun funny furnace fury future gadget gain galaxy gallery game gap garage
garbage garden garlic garment gas gasp gate gather gauge gaze general genius genre gentle genuine
gesture ghost giant gift giggle ginger giraffe girl give glad glance glare glass glide glimpse
globe gloom glory glove glow glue goat goddess gold good goose gorilla gospel gossip govern gown
grab grace grain grant grape grass gravity great green grid grief grit grocery group grow grunt
guard guess guide guilt guitar gun gym habit hair half hammer hamster hand happy harbor hard harsh
harvest hat have hawk hazard head health heart heavy hedgehog height hello helmet help hen hero
hidden high hill hint hip hire history hobby hockey hold hole holiday hollow home honey hood hope
horn horror horse hospital host hotel hour hover hub huge human humble humor hundred hungry hunt
hurdle hurry hurt husband hybrid ice icon idea identify idle ignore ill illegal illness image imitate
immense immune impact impose improve impulse inch include income increase index indicate indoor
industry infant inflict inform inhale inherit initial inject injury inmate inner innocent input
inquiry insane insect inside inspire install intact interest into invest invite involve iron island
isolate issue item ivory jacket jaguar jar jazz jealous jeans jelly jewel job join joke journey joy
judge juice jump jungle junior junk just kangaroo keen keep ketchup key kick kid kidney kind kingdom
kiss kit kitchen kite kitten kiwi knee knife knock know lab label labor ladder lady lake lamp language
laptop large later latin laugh laundry lava law lawn lawsuit layer lazy leader leaf learn leave lecture
left leg legal legend leisure lemon lend length lens leopard lesson letter level liar liberty library
license life lift light like limb limit link lion liquid list little live lizard load loan lobster
local lock logic lonely long loop lottery loud lounge love loyal lucky luggage lumber lunar lunch
luxury lyrics machine mad magic magnet maid mail main major make mammal man manage mandate mango
mansion manual maple marble march margin marine market marriage mask mass master match material math
matrix matter maximum maze meadow mean measure meat mechanic medal media melody melt member memory
mention menu mercy merge merit merry mesh message metal method middle midnight milk million mimic mind
minimum minor minute miracle mirror misery miss mistake mix mixed mixture mobile model modify mom
moment monitor monkey monster month moon moral more morning mosquito mother motion motor mountain
mouse move movie much muffin mule multiply muscle museum mushroom music must mutual myself mystery myth
naive name napkin narrow nasty nation nature near neck need negative neglect neither nephew nerve nest
net network neutral never news next nice night noble noise nominee noodle normal north nose notable note
nothing notice novel now nuclear number nurse nut oak obey object oblige obscure observe obtain obvious
occur ocean october odor off offer office often oil okay old olive olympic omit once one onion online
only open opera opinion oppose option orange orbit orchard order ordinary organ orient original orphan
ostrich other outdoor outer output outside oval oven over own owner oxygen oyster ozone pact paddle page
pair palace palm panda panel panic panther paper parade parent park parrot party pass patch path patient
patrol pattern pause pave payment peace peanut pear peasant pelican pen penalty pencil people pepper
perfect permit person pet phone photo phrase physical piano picnic picture piece pig pigeon pill pilot
pink pioneer pipe pistol pitch pizza place planet plastic plate play please pledge pluck plug plunge poem
poet point polar pole police pond pony pool popular portion position possible post potato pottery poverty
powder power practice praise predict prefer prepare present pretty prevent price pride primary print
priority prison private prize problem process produce profit program project promote proof property prosper
protect proud provide public pudding pull pulp pulse pumpkin punch pupil puppy purchase purity purpose purse
push put puzzle pyramid quality quantum quarter question quick quit quiz quote rabbit raccoon race rack radar
radio rail rain raise rally ramp ranch random range rapid rare rate rather raven raw razor ready real reason
rebel rebuild recall receive recipe record recycle reduce reflect reform refuse region regret regular reject
relax release relief rely remain remember remind remove render renew rent reopen repair repeat replace report
require rescue resemble resist resource response result retire retreat return reunion reveal review reward
rhythm rib ribbon rice rich ride ridge rifle right rigid ring riot ripple risk ritual rival river road roast
robot robust rocket romance roof rookie room rose rotate rough round route royal rubber rude rug rule run
runway rural sad saddle sadness safe sail salad salmon salon salt salute same sample sand satisfy satoshi
sauce sausage save say scale scan scare scatter scene scheme school science scissors scorpion scout scrap
screen script scrub sea search season seat second secret section security seed seek segment select sell
seminar senior sense sentence series service session settle setup seven shadow shaft shallow share shed shell
sheriff shield shift shine ship shiver shock shoe shoot shop short shoulder shove shrimp shrug shuffle shy
sibling sick side siege sight sign silent silk silly silver similar simple since sing siren sister situate six
size skate sketch ski skill skin skirt skull slab slam sleep slender slice slide slight slim slogan slot slow
slush small smart smile smoke smooth snack snake snap sniff snow soap soccer social sock soda soft solar
soldier solid solution solve someone song soon sorry sort soul sound soup source south space spare spatial
spawn speak special speed spell spend sphere spice spider spike spin spirit split spoil sponsor spoon sport
spot spray spread spring spy square squeeze squirrel stable stadium staff stage stairs stamp stand start
state stay steak steel stem step stereo stick still sting stock stomach stone stool story stove strategy
street strike strong struggle student stuff stumble style subject submit subway success such sudden suffer
sugar suggest suit summer sun sunny sunset super supply supreme sure surface surge surprise surround survey
suspect sustain swallow swamp swap swarm swear sweet swift swim swing switch sword symbol symptom syrup
system table tackle tag tail talent talk tank tape target task taste tattoo taxi teach team tell ten tenant
tennis tent term test text thank that theme then theory there they thing this thought three thrive throw
thumb thunder ticket tide tiger tilt timber time tiny tip tired tissue title toast tobacco today toddler toe
together toilet token tomato tomorrow tone tongue tonight tool tooth top topic topple torch tornado tortoise
toss total tourist toward tower town toy track trade traffic tragic train transfer trap trash travel tray
treat tree trend trial tribe trick trigger trim trip trophy trouble truck true truly trumpet trust truth try
tube tuition tumble tuna tunnel turkey turn turtle twelve twenty twice twin twist two type typical ugly
umbrella unable unaware uncle uncover under undo unfair unfold unhappy uniform unique unit universe unknown
unlock until unusual unveil update upgrade uphold upon upper upset urban urge usage use used useful useless
usual utility vacant vacuum vague valid valley valve van vanish vapor various vast vault vehicle velvet
vendor venture venue verb verify version very vessel veteran viable vibrant vicious victory video view
village vintage violin virtual virus visa visit visual vital vivid vocal voice void volcano volume vote
voyage wage wagon wait walk wall walnut want warfare warm warrior wash wasp waste water wave way wealth
weapon wear weasel weather web wedding weekend weird welcome west wet whale what wheat wheel when where whip
whisper wide width wife wild will win window wine wing wink winner winter wire wisdom wise wish witness wolf
woman wonder wood wool word work world worry worth wrap wreck wrestle wrist write wrong yard year yellow you
young youth zebra zero zone zoo""".split()
)


def _looks_like_mnemonic(text: str) -> bool:
    words = text.split()
    if len(words) not in (12, 15, 18, 21, 24):
        return False
    hits = sum(1 for w in words if w.lower() in _BIP39_SAMPLE)
    # Require a strong majority — plain English prose should not trip this.
    return hits >= len(words) * 0.8


# ---------------------------------------------------------------------------
# Page-state classification
# ---------------------------------------------------------------------------

#: Phrases that mean "a human must solve this". We detect, we do not solve.
CAPTCHA_PHRASES: tuple[str, ...] = (
    "captcha",
    "i'm not a robot",
    "im not a robot",
    "verify you are human",
    "verify that you are human",
    "are you a human",
    "human verification",
    "recaptcha",
    "hcaptcha",
    "turnstile",
    "geetest",
    "select all images",
    "cloudflare challenge",
    "checking your browser",
    "just a moment",
)

MFA_PHRASES: tuple[str, ...] = (
    "two-factor",
    "two factor",
    "2fa",
    "verification code",
    "one-time code",
    "one-time password",
    "otp",
    "authenticator app",
    "enter the code",
    "sms code",
    "recovery code",
    "backup code",
)

LOGIN_EXPIRED_PHRASES: tuple[str, ...] = (
    "session expired",
    "session has expired",
    "your session timed out",
    "please sign in",
    "please log in",
    "please log in again",
    "you have been logged out",
    "you need to sign in",
    "authentication required",
    "token expired",
    "unauthorized",
    "401",
)

SIGNATURE_PHRASES: tuple[str, ...] = (
    "sign message",
    "signature request",
    "confirm transaction",
    "approve transaction",
    "confirm in wallet",
    "sign in wallet",
    "metamask",
    "phantom",
    "walletconnect",
    "gas fee",
    "max slippage",
    "permit2",
    "setapprovalforall",
    "unlimited approval",
)


def _match(text: str, phrases: tuple[str, ...]) -> str | None:
    low = text.lower()
    for p in phrases:
        if p in low:
            return p
    return None


def inspect_page(text: str | None, *, url: str = "") -> Halt | None:
    """Classify page text and return a :class:`Halt` if a human must intervene.

    Order matters: a wallet signature prompt on a page that also mentions
    "sign in" should halt on the signature, not be dismissed as a login.
    """
    if not text:
        return None

    if m := _match(text, CAPTCHA_PHRASES):
        return Halt(
            HaltReason.CAPTCHA,
            f"challenge detected ({m!r}) at {url or 'unknown url'}",
            "Take over the browser and solve it manually. This system never "
            "attempts to solve a CAPTCHA.",
        )
    if m := _match(text, SIGNATURE_PHRASES):
        return Halt(
            HaltReason.SIGNATURE_REQUEST,
            f"wallet signature prompt detected ({m!r}) at {url or 'unknown url'}",
            "Review the payload yourself and sign only if you intended it. "
            "Blind-signing an approval can drain the wallet.",
        )
    if m := _match(text, MFA_PHRASES):
        return Halt(
            HaltReason.MFA,
            f"MFA prompt detected ({m!r})",
            "Take over the browser and complete verification.",
        )
    if m := _match(text, LOGIN_EXPIRED_PHRASES):
        return Halt(
            HaltReason.LOGIN_EXPIRED,
            f"session appears expired ({m!r})",
            "Log back in manually, then re-run the task.",
        )
    return None


# ---------------------------------------------------------------------------
# Approval gating
# ---------------------------------------------------------------------------

#: Actions that may move funds. These always need an operator's explicit yes.
SPEND_ACTIONS: frozenset[str] = frozenset(
    {
        "bridge",
        "swap",
        "stake",
        "unstake",
        "deposit",
        "withdraw",
        "transfer",
        "approve",
        "claim",
        "mint",
        "buy",
        "sell",
        "lend",
        "borrow",
    }
)


def requires_approval(action: str, *, approved_actions: frozenset[str] = frozenset()) -> bool:
    """True when ``action`` must be gated behind operator approval.

    An action can be pre-approved by name, but only for non-spend actions;
    spend actions are never auto-approved from config alone.
    """
    a = action.strip().lower()
    if a in SPEND_ACTIONS:
        return True
    return a not in approved_actions


def check_spend_limit(amount_usd: float, limit_usd: float) -> Halt | None:
    """Block any single action above the configured per-action USD limit."""
    if amount_usd > limit_usd:
        return Halt(
            HaltReason.SPEND_LIMIT,
            f"action costs ${amount_usd:.2f}, above the ${limit_usd:.2f} per-action limit",
            "Raise the limit deliberately, or split the action.",
        )
    return None


def scan_text_for_keys(text: str | None) -> Halt | None:
    """Refuse to proceed if key material appears in anything we would persist."""
    kind = classify_secret_material(text)
    if kind is None:
        return None
    return Halt(
        HaltReason.PRIVATE_KEY,
        f"{kind} material detected",
        "Remove it. This system stores wallet addresses only — keys belong in "
        "a hardware wallet or an OS keychain you control.",
    )


# ---------------------------------------------------------------------------
# Tiered approval
# ---------------------------------------------------------------------------
#
# "The operator signs everything" does not survive contact with a real
# campaign. Monad alone is 30-50 actions across ~15 dApps, most of them
# testnet interactions with tokens that have no value. Asking a human to sign
# each one is 30-50 interruptions for nothing.
#
# So approval is tiered by what is actually at risk, not by whether a
# signature happens:
#
#   read      navigate, snapshot, screenshot, read a page      -> autonomous
#   connect   connect a wallet without signing anything        -> autonomous
#   testnet   on-chain, but the tokens have no value           -> autonomous
#   mainnet   real value, within the per-action limit          -> autonomous + report
#   critical  unbounded grant, or over the limit               -> ALWAYS human
#
# The last row is the one that must never be relaxed. An unlimited ERC-20
# approval or setApprovalForAll is how wallets get drained, and it is not
# bounded by any spend limit because the exposure is the whole balance.

class Tier(str, Enum):
    READ = "read"
    CONNECT = "connect"
    TESTNET = "testnet"
    MAINNET = "mainnet"
    CRITICAL = "critical"


#: Actions whose exposure is unbounded. Never autonomous, on any network,
#: at any amount — a spend limit cannot cap "everything you own".
UNBOUNDED_ACTIONS: frozenset[str] = frozenset(
    {
        "setapprovalforall",
        "approve_unlimited",
        "unlimited_approval",
        "permit2",
        "increase_allowance",
        "set_approval_for_all",
    }
)

#: Read-only interactions. No signature, no spend, no state change.
READ_ACTIONS: frozenset[str] = frozenset(
    {
        "navigate",
        "snapshot",
        "screenshot",
        "read",
        "check_in_readonly",
        "view",
        "scroll",
        "search",
    }
)

#: Wallet connection that does not sign. Linking an address is not a grant.
CONNECT_ACTIONS: frozenset[str] = frozenset(
    {"connect_wallet", "connect", "link_wallet", "add_network", "switch_network"}
)


@dataclass(frozen=True)
class ApprovalDecision:
    """Who has to act, and why."""

    tier: Tier
    autonomous: bool
    must_report: bool
    reason: str

    def __str__(self) -> str:
        who = "AUTONOMOUS" if self.autonomous else "HUMAN REQUIRED"
        rep = " (+report)" if self.must_report else ""
        return f"[{self.tier.value}] {who}{rep} — {self.reason}"


def classify_tier(
    action: str,
    *,
    network: str = "",
    is_unbounded: bool | None = None,
) -> Tier:
    """Work out which tier an action falls into.

    ``network`` should be a chain name or ``"testnet"``/``"mainnet"``. An
    unknown network is treated as **mainnet** — failing open here would mean
    an unrecognised chain gets to spend real money unattended.
    """
    a = action.strip().lower().replace("-", "_").replace(" ", "_")

    if is_unbounded or a in UNBOUNDED_ACTIONS:
        return Tier.CRITICAL
    if a in READ_ACTIONS:
        return Tier.READ
    if a in CONNECT_ACTIONS:
        return Tier.CONNECT

    n = network.strip().lower()
    if n.endswith("testnet") or n.startswith("testnet") or n in ("test", "devnet"):
        return Tier.TESTNET
    # Anything we cannot classify is assumed to hold real value.
    return Tier.MAINNET


def decide(
    action: str,
    *,
    network: str = "",
    amount_usd: float = 0.0,
    spend_limit_usd: float = 0.0,
    is_unbounded: bool | None = None,
) -> ApprovalDecision:
    """Decide whether an action may run unattended.

    Ordering matters. The unbounded check runs first so that an unlimited
    approval on a testnet is still flagged as something a human should see —
    the habit of blind-approving is what causes mainnet losses later.
    """
    tier = classify_tier(action, network=network, is_unbounded=is_unbounded)

    if tier is Tier.CRITICAL:
        why = (
            "unbounded grant — exposure is the whole balance, so no spend "
            "limit can cap it"
            if (is_unbounded or action.strip().lower().replace("-", "_") in UNBOUNDED_ACTIONS)
            else f"cost ${amount_usd:.2f} exceeds the ${spend_limit_usd:.2f} per-action limit"
        )
        return ApprovalDecision(Tier.CRITICAL, False, True, why)

    if tier is Tier.READ:
        return ApprovalDecision(Tier.READ, True, False, "read-only, nothing signed or spent")

    if tier is Tier.CONNECT:
        return ApprovalDecision(
            Tier.CONNECT, True, False, "links an address; no signature, no grant"
        )

    if tier is Tier.TESTNET:
        return ApprovalDecision(
            Tier.TESTNET,
            True,
            False,
            f"on-chain on {network or 'a testnet'}, but the tokens have no value",
        )

    # MAINNET
    if spend_limit_usd > 0 and amount_usd > spend_limit_usd:
        return ApprovalDecision(
            Tier.CRITICAL,
            False,
            True,
            f"cost ${amount_usd:.2f} exceeds the ${spend_limit_usd:.2f} per-action limit",
        )
    return ApprovalDecision(
        Tier.MAINNET,
        True,
        True,
        f"mainnet spend of ${amount_usd:.2f} within the ${spend_limit_usd:.2f} limit",
    )
