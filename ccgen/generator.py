# ccgen/generator.py

import random
from datetime import datetime
from typing import Tuple, List

def luhn_check_digit(partial: str) -> str:
    """Compute Luhn check digit for a partial (without check digit)."""
    total = 0
    for i, ch in enumerate(reversed(partial)):
        d = int(ch)
        if i % 2 == 0:
            dd = d * 2
            total += dd if dd < 10 else dd - 9
        else:
            total += d
    return str((10 - (total % 10)) % 10)

def generate_card_number(bin_prefix: str) -> str:
    """Generate a full 16-digit card number from a BIN prefix."""
    # build 15 digits then append Luhn digit
    needed = 15 - len(bin_prefix)
    filler = "".join(str(random.randint(0,9)) for _ in range(needed))
    partial = bin_prefix + filler
    return partial + luhn_check_digit(partial)

def generate_expiry(now: datetime=None) -> str:
    """Pick an expiry between 1–5 years from today (MM/YY)."""
    now = now or datetime.now()
    y0, m0 = now.year, now.month
    years = random.randint(1, 5)
    if years == 1:
        month = random.randint(m0, 12)
    else:
        month = random.randint(1, 12)
    year = (y0 + years) % 100
    return f"{month:02d}/{year:02d}"

def generate_cvv() -> str:
    """3-digit CVV."""
    return f"{random.randint(0,999):03d}"

def generate_zip() -> str:
    """5-digit ZIP."""
    return f"{random.randint(0,99999):05d}"

def generate_profile(bin_prefix: str, count: int) -> List[Tuple[str,str,str,str]]:
    """Return `count` card profiles as (number, expiry, cvv, zip)."""
    now = datetime.now()
    profiles = []
    for _ in range(count):
        num = generate_card_number(bin_prefix)
        exp = generate_expiry(now)
        cvv = generate_cvv()
        zp  = generate_zip()
        profiles.append((num, exp, cvv, zp))
    return profiles
