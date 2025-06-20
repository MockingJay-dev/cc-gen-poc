# tests/test_generator.py

import re
from ccgen.generator import (
    luhn_check_digit, generate_card_number,
    generate_expiry, generate_cvv, generate_zip
)
from datetime import datetime

def test_luhn_simple():
    # partial '7992739871' => full Luhn example => check digit 3
    assert luhn_check_digit("7992739871") == "3"

def test_card_number_length_and_digits():
    for _ in range(5):
        num = generate_card_number("123456")
        assert re.fullmatch(r"\d{16}", num)

def test_expiry_format():
    now = datetime(2025,6,19)
    for _ in range(10):
        exp = generate_expiry(now)
        assert re.fullmatch(r"(0[1-9]|1[0-2])\/\d{2}", exp)

def test_cvv_and_zip():
    for _ in range(10):
        assert re.fullmatch(r"\d{3}", generate_cvv())
        assert re.fullmatch(r"\d{5}", generate_zip())

