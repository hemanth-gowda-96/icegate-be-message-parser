''' Parser for exchange records from BE file format.'''

from typing import List
from .models.exchange_model import ExchangeRecord


def parse_be_line(line: str) -> ExchangeRecord:
    ''' Parse a single line from BE file format to ExchangeRecord.'''

    # Split by the delimiter (Group Separator character or tab for readability)
    if '\x1d' in line:
        fields = line.split('\x1d')
    elif '\t' in line:
        fields = line.split('\t')
    else:
        # If no delimiters found, assume single field
        fields = [line]

    # Ensure we have enough fields, pad with empty strings if needed
    while len(fields) < 14:
        fields.append('')

    return ExchangeRecord(
        message_type=fields[0] or '',
        custom_house_code=fields[1] or '',
        user_job_no=fields[2] or '',
        user_job_date=fields[3] if fields[3] else None,
        be_number=fields[4] if fields[4] else None,
        be_date=fields[5] if fields[5] else None,
        currency_code=fields[6] or '',
        standard_currency=fields[7] or '',
        unit_rs=fields[8] if fields[8] else None,
        rate=fields[9] if fields[9] else None,
        effective_date=fields[10] if fields[10] else None,
        bank_name=fields[11] if fields[11] else None,
        certificate_number=fields[12] if fields[12] else None,
        certificate_date=fields[13] if fields[13] else None,
    )


def parse_be_file(content: str) -> List[ExchangeRecord]:
    ''' Parse BE file content to list of ExchangeRecord.'''

    records = []
    lines = content.strip().split('\n')

    for line in lines:
        if line.strip():  # Skip empty lines
            records.append(parse_be_line(line))

    return records


def parse_be_file_from_path(file_path: str) -> List[ExchangeRecord]:
    ''' Parse BE file from file path to list of ExchangeRecord.'''

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return parse_be_file(content)
