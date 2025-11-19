#!/usr/bin/env python3
"""Simple JSON to BE format converter example."""

import json
from exchange_parser.CACH101 import ExchangeRecord, parse_be_file, to_be_file


def json_to_be_string():
    """Convert JSON data to BE format string."""

    print("JSON to BE String Conversion")
    print("-" * 40)

    # Sample JSON data
    json_data = {
        "message_type": "EXCHANGE",
        "custom_house_code": "INBLR1",
        "user_job_no": "JOB001",
        "user_job_date": "20241119",
        "be_number": "BE12345",
        "be_date": "20241119",
        "currency_code": "USD",
        "standard_currency": "Y",
        "unit_rs": "84.50",
        "rate": "1.00",
        "effective_date": "20241119",
        "bank_name": "STATE BANK OF INDIA",
        "certificate_number": "CERT001",
        "certificate_date": "20241119"
    }

    print("Input JSON:")
    print(json.dumps(json_data, indent=2))

    # Convert JSON to ExchangeRecord
    record = ExchangeRecord(**json_data)

    # Convert to BE string
    be_result = to_be_file([record])

    if be_result["err"] is not None:
        print(f"\n❌ Serialization Error: {be_result['err']}")
        return None

    be_string = be_result["data"]
    print("\nBE String Output:")
    print(f"'{be_string}'")

    return be_string


def be_string_to_json(be_string):
    """Convert BE format string back to JSON/dict."""

    print("\n" + "=" * 50)
    print("BE String to JSON Conversion")
    print("-" * 40)

    print("Input BE String:")
    print(f"'{be_string}'")

    # Parse BE string back to records
    records = parse_be_file(be_string)
    record = records[0]

    # Convert to dictionary
    record_dict = {
        "message_type": record.message_type,
        "custom_house_code": record.custom_house_code,
        "user_job_no": record.user_job_no,
        "user_job_date": record.user_job_date,
        "be_number": record.be_number,
        "be_date": record.be_date,
        "currency_code": record.currency_code,
        "standard_currency": record.standard_currency,
        "unit_rs": record.unit_rs,
        "rate": record.rate,
        "effective_date": record.effective_date,
        "bank_name": record.bank_name,
        "certificate_number": record.certificate_number,
        "certificate_date": record.certificate_date
    }

    print("\nOutput JSON:")
    print(json.dumps(record_dict, indent=2))

    return record_dict


def main():
    """Main function showing simple conversions."""

    print("Simple Exchange Parser - JSON ↔ BE String Converter")
    print("=" * 60)

    # JSON to BE string
    be_string = json_to_be_string()

    # BE string back to JSON
    json_dict = be_string_to_json(be_string)

    print("\n" + "=" * 60)
    print("✅ Conversion completed successfully!")
    print(f"Processed {len(json_dict)} fields successfully")

    print("\nUsage Summary:")
    print("- JSON → BE String: Use ExchangeRecord + to_be_file()")
    print("- BE String → JSON: Use parse_be_file() + convert to dict")


if __name__ == "__main__":
    main()
