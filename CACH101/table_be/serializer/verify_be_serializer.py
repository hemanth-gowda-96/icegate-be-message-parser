from CACH101.table_be.models.be_model import TableBERecord
from CACH101.table_be.serializer.be_serializer import be_to_be_line

def test_be_serialization():
    # Mock data for TableBERecord
    record = TableBERecord(
        message_type="F",
        custom_house_code="INNSA1",
        user_job_no="1234567",
        user_job_date="20231223",
        be_number="",
        be_date="",
        be_type="HOME",
        iec_code="0123456789",
        branch_sr_no="001",
        importer_name="EXAMPLE IMPORTER",
        address_1="ADDRESS LINE 1",
        address_2="ADDRESS LINE 2",
        city="MUMBAI",
        state="MAHARASHTRA",
        pin="400001",
        class_="G",
        mode_of_transport="S",
        importer_type="P",
        kachcha_be="N",
        high_sea_sale_flag="N",
        port_of_origin="USNYC1",
        cha_code="CHAC0DE12345678",
        country_of_origin="US",
        country_of_consignment="US",
        port_of_shipment="USNYC1",
        green_channel_requested="N",
        section_48_requested="N",
        prior_be="N",
        authorized_dealer_code="ADCODE1234",
        first_check_requested="N",
        warehouse_code="WH001",
        warehouse_customs_site_id="123456",
        warehouse_be_no="WBE1234",
        warehouse_be_date="20231223",
        no_of_packages_released="100",
        package_code="BOX",
        gross_weight="1234.567",
        unit_of_measurement="KGS",
        purchase_on_high_seas="100.50",
        miscellaneous_load="50.25",
        ucr="UCR123456789012345678901234567890",
        ucr_type="UCRT01",
        payment_method_code="T"
    )

    print("--- Testing FINAL Mode ---")
    result_final = be_to_be_line(record, mode="FINAL")
    if result_final["err"]:
        print(f"Error (FINAL): {result_final['err']}")
    else:
        print(f"Serialized (FINAL): {result_final['data'].replace('\x1d', '|')}")

    print("\n--- Testing SEZ Mode ---")
    # For SEZ mode, cha_code should be empty (rule X)
    record.cha_code = ""
    result_sez = be_to_be_line(record, mode="SEZ")
    if result_sez["err"]:
        print(f"Error (SEZ): {result_sez['err']}")
    else:
        print(f"Serialized (SEZ): {result_sez['data'].replace('\x1d', '|')}")

if __name__ == "__main__":
    test_be_serialization()
