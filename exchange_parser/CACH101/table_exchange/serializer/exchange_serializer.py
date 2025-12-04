"""
Serializer for EXCHANGE records to BE file format
with validation rules, FINAL/SEZ mode support,
field type checking, and strict ICEGATE compliance.
"""


from exchange_parser.CACH101.specification.specification import EXCHANGE_FIELD_SPECS
from exchange_parser.CACH101.table_exchange.models.exchange_model import ExchangeRecord
from exchange_parser.helpers.validation import _normalize, _validate_date, _validate_numeric, _validate_decimal

DELIM = "\x1d"  # ASCII 29 GS


# ------------------------------
# Main Validation Function
# ------------------------------
def validate_field(name, value, field_type, length, rule):
    """Apply validation rules for a single field."""

    value = _normalize(value)

    # If rule = X → field must be empty
    if rule == "X":
        if value != "":
            return f"Field '{name}' is not allowed in this mode"
        return None

    # If mandatory (F,K,M) → cannot be empty
    if rule in ("F", "K", "M") and value == "":
        return f"Field '{name}' is mandatory"

    # If empty and optional → OK
    if value == "":
        return None

    # Validate TYPE
    if field_type == "C":
        if length and len(value) > length:
            return f"Field '{name}' exceeds max length {length}"

    elif field_type == "N":
        if not _validate_numeric(value):
            return f"Field '{name}' must be numeric"
        if length and len(str(value)) > length:
            return f"Field '{name}' exceeds numeric length {length}"

    elif field_type == "DATE":
        if not _validate_date(value):
            return f"Field '{name}' must be in YYYYMMDD format"

    elif field_type == "N7,2":
        # Convert numeric values to string for validation
        str_value = str(value) if isinstance(value, (int, float)) else value
        if not _validate_decimal(str_value, r"\d{1,7}\.\d{1,2}"):
            return f"Field '{name}' must be numeric with format 7,2 (e.g., '84.50')"

    elif field_type == "N9,4":
        # Convert numeric values to string for validation
        str_value = str(value) if isinstance(value, (int, float)) else value
        if not _validate_decimal(str_value, r"\d{1,9}\.\d{1,4}"):
            return f"Field '{name}' must be numeric with format 9,4 (e.g., '1.0000')"

    return None


# ------------------------------
# Serializers
# ------------------------------
def exchange_to_be_line(record: ExchangeRecord, mode: str = "FINAL") -> dict:
    """Serialize a validated ExchangeRecord into a .be line."""

    try:
        mode = mode.upper()
        if mode not in ("FINAL", "SEZ"):
            return {"err": "Invalid mode. Use 'FINAL' or 'SEZ'.", "data": None}

        fields_out = []

        for (name, ftype, length, rules) in EXCHANGE_FIELD_SPECS:
            value = getattr(record, name, "")

            # Apply validation rules
            rule = rules[mode]
            err = validate_field(name, value, ftype, length, rule)
            if err:
                return {"err": err, "data": None}

            # Convert numeric values to string format
            normalized_value = _normalize(value)
            if isinstance(value, (int, float)) and normalized_value != "":
                normalized_value = str(value)
            fields_out.append(normalized_value)

        # Join fields with GS delimiter
        be_line = DELIM.join(fields_out)
        return {"err": None, "data": be_line}

    except (AttributeError, ValueError, TypeError) as e:
        return {"err": str(e), "data": None}


def exchange_to_be_file(records: list[ExchangeRecord], mode="FINAL") -> dict:
    """Serialize multiple records into BE file format."""
    if not records:
        return {"err": "No records provided", "data": None}

    lines = []
    for i, record in enumerate(records):
        result = exchange_to_be_line(record, mode=mode)
        if result["err"]:
            return {"err": f"Record {i+1}: {result['err']}", "data": None}

        lines.append(result["data"])

    return {"err": None, "data": "\n".join(lines)}
