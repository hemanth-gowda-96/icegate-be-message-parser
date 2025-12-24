"""
Serializer for PERMISSION records to BE file format
with validation rules, FINAL/SEZ mode support,
field type checking, and strict ICEGATE compliance.
"""

from CACH101.specification.specification import PERMISSION_FIELD_SPECS
from CACH101.table_permission.models.permission_model import TablePermissionRecord
from helpers.validation import _normalize, _validate_date, _validate_numeric, _validate_decimal

DELIM = "\x1d"  # ASCII 29 GS


# ------------------------------
# Main Validation Function
# ------------------------------
def validate_permission_field(name, value, field_type, length, rule):
    """Apply validation rules for a single PERMISSION field."""

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

    return None


# ------------------------------
# Serializers
# ------------------------------
def permission_to_be_line(record: TablePermissionRecord, mode: str = "FINAL") -> dict:
    """Serialize a validated TablePermissionRecord into a .be line."""

    try:
        mode = mode.upper()
        if mode not in ("FINAL", "SEZ"):
            return {"err": "Invalid mode. Use 'FINAL' or 'SEZ'.", "data": None}

        fields_out = []

        for (name, ftype, length, rules) in PERMISSION_FIELD_SPECS:
            value = getattr(record, name, "")

            # Apply validation rules
            rule = rules[mode]
            err = validate_permission_field(name, value, ftype, length, rule)
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


def permission_to_be_file(records: list[TablePermissionRecord], mode="FINAL") -> dict:
    """Serialize multiple records into BE file format."""
    if not records:
        return {"err": "No records provided", "data": None}

    lines = []
    for i, record in enumerate(records):
        result = permission_to_be_line(record, mode=mode)
        if result["err"]:
            return {"err": f"Record {i+1}: {result['err']}", "data": None}

        lines.append(result["data"])

    return {"err": None, "data": "\n".join(lines)}
