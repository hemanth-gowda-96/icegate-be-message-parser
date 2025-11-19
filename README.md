# ICEGate BE Message Parser

A Python package for parsing and serializing Indian Customs EXCHANGE (.be) format messages used in ICEGate systems.

## Features

- Parse BE format files to Python objects
- Serialize Python objects to BE format
- Support for both binary (\x1d) and tab-delimited formats
- Type hints and dataclass-based models
- Comprehensive examples and documentation

## Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/hemanth-gowda-96/icegate-be-message-parser.git
cd icegate-be-message-parser

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install in development mode
pip install -e .
```

## Quick Start

```python
from exchange_parser import ExchangeRecord, parse_be_file, to_be_file

# Create an exchange record
record = ExchangeRecord(
    message_type="EXCHANGE",
    custom_house_code="INBLR1",
    user_job_no="JOB001",
    user_job_date="20241119",
    be_number="BE12345",
    be_date="20241119",
    currency_code="USD",
    standard_currency="Y",
    unit_rs="84.50",
    rate="1.00",
    effective_date="20241119",
    bank_name="STATE BANK OF INDIA",
    certificate_number="CERT001",
    certificate_date="20241119"
)

# Serialize to BE format
be_content = to_be_file([record])
print(be_content)

# Parse back from BE format
parsed_records = parse_be_file(be_content)
print(f"Parsed {len(parsed_records)} records")
```

## API Reference

### Classes

#### `ExchangeRecord`

Data model for exchange records with the following fields:

- `message_type`: Message type identifier
- `custom_house_code`: Custom house code
- `user_job_no`: User job number
- `user_job_date`: User job date (optional)
- `be_number`: BE number (optional)
- `be_date`: BE date (optional)
- `currency_code`: Currency code
- `standard_currency`: Standard currency flag
- `unit_rs`: Unit in rupees (optional)
- `rate`: Exchange rate (optional)
- `effective_date`: Effective date (optional)
- `bank_name`: Bank name (optional)
- `certificate_number`: Certificate number (optional)
- `certificate_date`: Certificate date (optional)

### Functions

#### `parse_be_file(content: str) -> List[ExchangeRecord]`

Parse BE file content to list of ExchangeRecord objects.

#### `parse_be_file_from_path(file_path: str) -> List[ExchangeRecord]`

Parse BE file from file path to list of ExchangeRecord objects.

#### `to_be_file(records: List[ExchangeRecord]) -> str`

Serialize list of ExchangeRecord objects to BE file format.

#### `to_be_line(record: ExchangeRecord) -> str`

Serialize single ExchangeRecord to BE line format.

## Examples

See the `example/` directory for comprehensive usage examples:

- `simple_usage.py`: Basic usage example
- `main.py`: Complete demonstration with serialization, parsing, and round-trip testing
- `file_parsing_example.py`: File-based operations
- `sample_files/`: Sample BE files for testing

### Running Examples

```bash
# Simple usage
python example/simple_usage.py

# Complete demo
python example/main.py

# File parsing demo
python example/file_parsing_example.py
```

## File Format

The BE format uses the ASCII Group Separator character (\x1d, decimal 29) as a field delimiter. Each record is on a separate line with 14 fields:

```
EXCHANGE[GS]INBLR1[GS]JOB001[GS]20241119[GS]BE12345[GS]20241119[GS]USD[GS]Y[GS]84.50[GS]1.00[GS]20241119[GS]STATE BANK OF INDIA[GS]CERT001[GS]20241119
```

Where `[GS]` represents the Group Separator character (\x1d).

For readability, the parser also supports tab-delimited format in sample files.

## Currency Information

- **Standard Currencies**: Currencies for which exchange rate notifications are issued by the Ministry of Finance
- **Non-standard Currencies**: All other currencies requiring mandatory fields (Unit Rs, Rate, Effective Date, Bank Name, Certificate Number, Certificate Date)
- **SEZ-M type BE**: Currency code should only be INR

## Development

### Project Structure

```
icegate-be-message-parser/
├── exchange_parser/           # Main package
│   ├── __init__.py           # Package exports
│   ├── parser.py             # Parsing functions
│   ├── models/
│   │   └── exchange_model.py # Data models
│   └── serializer/
│       └── exchange_serializer.py # Serialization functions
├── example/                  # Usage examples
│   ├── main.py              # Complete demo
│   ├── simple_usage.py      # Basic usage
│   ├── file_parsing_example.py # File operations
│   └── sample_files/        # Sample BE files
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

### Building the Package

```bash
# Install build dependencies
pip install build

# Build the package
python -m build
```

## License

This project is open source. See LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions, please use the GitHub issue tracker.
