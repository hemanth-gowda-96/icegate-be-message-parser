''' Data model for be records.'''

from dataclasses import dataclass
from typing import Optional


@dataclass
class TableBERecord:
    '''Data model for be records.'''

    message_type: str
    custom_house_code: str
    user_job_no: str
    user_job_date: Optional[str]
    be_number: Optional[str]
    be_date: Optional[str]
    be_type: Optional[str]
    iec_code: Optional[str]
    branch_sr_no: Optional[str]
    importer_name: Optional[str]
    address_1: Optional[str]
    address_2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    pin: Optional[str]
    class_: Optional[str]
    mode_of_transport: Optional[str]
    importer_type: Optional[str]
    kachcha_be: Optional[str]
    high_sea_sale_flag: Optional[str]
    port_of_origin: Optional[str]
    cha_code: Optional[str]
    country_of_origin: Optional[str]
    country_of_consignment: Optional[str]
    port_of_shipment: Optional[str]
    green_channel_requested: Optional[str]
    section_48_requested: Optional[str]
    prior_be: Optional[str]
    authorized_dealer_code: Optional[str]
    first_check_requested: Optional[str]
    warehouse_code: Optional[str]
    warehouse_customs_site_id: Optional[str]
    warehouse_be_no: Optional[str]
    warehouse_be_date: Optional[str]
    no_of_packages_released: Optional[str]
    package_code: Optional[str]
    gross_weight: Optional[str]
    unit_of_measurement: Optional[str]
    purchase_on_high_seas: Optional[str]
    miscellaneous_load: Optional[str]
    ucr: Optional[str]
    ucr_type: Optional[str]
    payment_method_code: Optional[str]


# NOTE:
# Currencies for which the exchange rate notification is issued
#                by Ministry of Finance are termed as 'Standard
# Currencies" and the rest as "Non-standard Currencies" in ICES.
# Refer Annexure C for Currency Code Directory. Standard Currency Codes are marked as '*'.
# For Non-standard Currencies providing of - Unit in Rs, Rate, Effective Date, Bank Name,
#                Certificate Number
# and Certificate date is mandatory. Date of Certificate should match the date of filing.
# For Standard Currencies, these parameters are optional.
# There shall be number of records equivalent to the number of currencies used in the BE
# SEZ-M type BE the currency code should only be INR
