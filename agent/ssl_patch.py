"""SSL patch — disable certificate verification for Polymarket APIs.
Polymarket Gamma API certificate has expired. This patches requests
to skip SSL verification for polymarket.com domains only.
Import this at the top of main.py.
"""
import requests
import urllib3
import warnings

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Monkey-patch requests.get/post to add verify=False for polymarket domains
_orig_get = requests.get
_orig_post = requests.post

def _patched_get(url, **kwargs):
    if 'polymarket.com' in str(url) or 'gamma-api' in str(url):
        kwargs.setdefault('verify', False)
    return _orig_get(url, **kwargs)

def _patched_post(url, **kwargs):
    if 'polymarket.com' in str(url) or 'gamma-api' in str(url):
        kwargs.setdefault('verify', False)
    return _orig_post(url, **kwargs)

requests.get = _patched_get
requests.post = _patched_post
