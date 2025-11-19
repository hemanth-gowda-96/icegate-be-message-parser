''' Serializer for exchange records to BE file format.'''

from exchange_parser.models.exchange_model import ExchangeRecord

DELIM = "\x1d"  # Group Separator (ASCII 29)


def to_be_line(record: ExchangeRecord) -> str:
    ''' Serialize an ExchangeRecord to a BE file line.'''

    fields = [
        record.message_type or "",
        record.custom_house_code or "",
        record.user_job_no or "",
        record.user_job_date or "",
        record.be_number or "",
        record.be_date or "",
        record.currency_code or "",
        record.standard_currency or "",
        record.unit_rs or "",
        record.rate or "",
        record.effective_date or "",
        record.bank_name or "",
        record.certificate_number or "",
        record.certificate_date or "",
    ]

    return DELIM.join(fields)


def to_be_file(records: list[ExchangeRecord]) -> str:
    ''' Serialize a list of ExchangeRecord to BE file format.'''
    return "\n".join(to_be_line(r) for r in records)
