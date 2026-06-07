#!/usr/bin/env python3
import sys
import argparse
import pgeocode


def zip_to_gps(zip_code, country="US"):
    nomi = pgeocode.Nominatim(country)
    result = nomi.query_postal_code(str(zip_code))

    if result is None or result.empty:
        return None

    lat = result.latitude
    lon = result.longitude

    if lat != lat or lon != lon:  # NaN check
        return None

    return {
        "zip": str(zip_code),
        "city": result.place_name,
        "state": result.state_name,
        "state_code": result.state_code,
        "latitude": float(lat),
        "longitude": float(lon),
    }


def main():
    parser = argparse.ArgumentParser(description="Convert ZIP code to GPS coordinates")
    parser.add_argument("zip", nargs="?", help="ZIP code")
    parser.add_argument("-c", "--country", default="US", help="Country code, default US")
    args = parser.parse_args()

    zip_code = args.zip

    if not zip_code:
        zip_code = sys.stdin.read().strip()

    if not zip_code:
        print("No ZIP code provided")
        sys.exit(1)

    data = zip_to_gps(zip_code, args.country)

    if not data:
        print(f"No GPS coordinates found for ZIP: {zip_code}")
        sys.exit(1)

    print(data["latitude"], data["longitude"])
    print(data)


if __name__ == "__main__":
    main()