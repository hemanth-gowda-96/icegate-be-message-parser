"""
Verification script for PERMISSION serializer.
"""

from CACH101.table_permission.serializer.permission_serializer import permission_to_be_line
from CACH101.table_permission.models.permission_model import TablePermissionRecord
import sys
import os

# Add project root to sys.path to support direct execution
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../../..")))


def test_permission_serialization():
    # Sample data based on documentation
    # Message type: P (assuming P for Permission, but spec shows F for Final)
    # The spec in the image shows Message Type 'F' for 'Final'

    sample_record = TablePermissionRecord(
        message_type="F",
        custom_house_code="INMAA4",
        user_job_no="1234567",
        user_job_date="20231224",
        be_number="",
        be_date="",
        permission_code="S48",
        reasons_for_request="Late filing of BE U/s 48 of Customs Act."
    )

    print("Testing PERMISSION serialization...")
    result = permission_to_be_line(sample_record, mode="FINAL")

    if result["err"]:
        print(f"FAILED: {result['err']}")
    else:
        print(f"SUCCESS: {result['data']}")
        # Verify delimiter (ASCII 29)
        expected_delim = "\x1d"
        if expected_delim in result["data"]:
            print("Delimiter verified.")
        else:
            print("ERROR: Delimiter missing!")


if __name__ == "__main__":
    test_permission_serialization()
