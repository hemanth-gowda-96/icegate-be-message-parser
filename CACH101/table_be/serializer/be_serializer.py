"""
Serializer for BE records to BE file format
with validation rules, FINAL/SEZ mode support,
field type checking, and strict ICEGATE compliance.
"""

from CACH101.specification.specification import TABLE_BE_FIELDS_SPECS
from CACH101.table_be.models.be_model import TableBERecord
from helpers.validation import _normalize, _validate_date, _validate_numeric, _validate_decimal

DELIM = "\x1d"  # ASCII 29 GS


# ------------------------------
# Main Validation Function
# ------------------------------
def validate_be_field(name, value, field_type, length, rule):
    """Apply validation rules for a single BE field."""

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
        str_value = str(value) if isinstance(value, (int, float)) else value
        if not _validate_decimal(str_value, r"\d{1,7}\.\d{1,2}"):
            return f"Field '{name}' must be numeric with format 7,2 (e.g., '84.50')"

    elif field_type == "N9,4":
        str_value = str(value) if isinstance(value, (int, float)) else value
        if not _validate_decimal(str_value, r"\d{1,9}\.\d{1,4}"):
            return f"Field '{name}' must be numeric with format 9,4 (e.g., '1.0000')"

    elif field_type == "N12,3":
        str_value = str(value) if isinstance(value, (int, float)) else value
        if not _validate_decimal(str_value, r"\d{1,12}\.\d{1,3}"):
            return f"Field '{name}' must be numeric with format 12,3"

    elif field_type == "N6,2":
        str_value = str(value) if isinstance(value, (int, float)) else value
        if not _validate_decimal(str_value, r"\d{1,6}\.\d{1,2}"):
            return f"Field '{name}' must be numeric with format 6,2"

    return None


# ------------------------------
# Serializers
# ------------------------------
def be_to_be_line(record: TableBERecord, mode: str = "FINAL") -> dict:
    """Serialize a validated TableBERecord into a .be line."""

    try:
        mode = mode.upper()
        if mode not in ("FINAL", "SEZ"):
            return {"err": "Invalid mode. Use 'FINAL' or 'SEZ'.", "data": None}

        fields_out = []

        for (name, ftype, length, rules) in TABLE_BE_FIELDS_SPECS:
            # Handle field name Mapping (e.g., 'class' is 'class_' in dataclass)
            attr_name = "class_" if name == "class" else name
            value = getattr(record, attr_name, "")

            # Apply validation rules
            rule = rules[mode]
            err = validate_be_field(name, value, ftype, length, rule)
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


def be_to_be_file(records: list[TableBERecord], mode="FINAL") -> dict:
    """Serialize multiple records into BE file format."""
    if not records:
        return {"err": "No records provided", "data": None}

    lines = []
    for i, record in enumerate(records):
        result = be_to_be_line(record, mode=mode)
        if result["err"]:
            return {"err": f"Record {i+1}: {result['err']}", "data": None}

        lines.append(result["data"])

    return {"err": None, "data": "\n".join(lines)}
