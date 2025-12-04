#!/usr/bin/env python3
"""Simple JSON to BE format converter example."""

import json

from exchange_parser.CACH101.table_exchange.models.exchange_model import ExchangeRecord
from exchange_parser.CACH101.table_exchange.serializer.exchange_serializer import exchange_to_be_file


def json_to_be_string():
    """Convert JSON data to BE format string."""

    print("JSON to BE String Conversion")
    print("-" * 40)

    # Sample JSON data
    json_data = {
        "message_type": "F",
        "custom_house_code": "INBLR1",
        "user_job_no": 993922,
        "user_job_date": "20241119",
        "be_number": None,
        "be_date": None,
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
    be_result = exchange_to_be_file([record])

    if be_result["err"] is not None:
        print(f"\n❌ Serialization Error: {be_result['err']}")
        return None

    be_string = be_result["data"]
    print("\nBE String Output:")
    print(f"'{be_string}'")

    return be_string


def main():
    """Main function showing simple conversions."""

    be_string = json_to_be_string()

    # store be_string to a file or further processing if needed
    if be_string is not None:
        with open("output.be", "w") as f:
            f.write(be_string)


if __name__ == "__main__":
    main()
