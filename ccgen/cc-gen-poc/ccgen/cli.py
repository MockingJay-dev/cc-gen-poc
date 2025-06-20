# ccgen/cli.py

import argparse
import csv
import sys
from .generator import generate_profile

def main():
    parser = argparse.ArgumentParser(
        description="POC CC Regen – generate test card profiles (all fictional)."
    )
    parser.add_argument("bin", help="BIN prefix (6–12 digits)")
    parser.add_argument(
        "-n", "--number", type=int, default=100,
        help="Number of profiles to generate (default: 100)"
    )
    parser.add_argument(
        "-o", "--output", help="CSV filename to save results"
    )
    args = parser.parse_args()

    if not args.bin.isdigit() or not (6 <= len(args.bin) <= 12):
        sys.exit("Error: BIN must be 6–12 digits.")

    profiles = generate_profile(args.bin, args.number)

    # Print to stdout
    print(f"{'Card Number':<16}  {'Expiry':<7}  {'CVV':<3}  {'ZIP':<5}")
    print("-" * 36)
    for num, exp, cvv, zp in profiles:
        print(f"{num:<16}  {exp:<7}  {cvv:<3}  {zp:<5}")

    # Optional CSV export
    if args.output:
        with open(args.output, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Card Number","Expiry","CVV","ZIP"])
            w.writerows(profiles)
        print(f"\nSaved {len(profiles)} profiles to {args.output}")

