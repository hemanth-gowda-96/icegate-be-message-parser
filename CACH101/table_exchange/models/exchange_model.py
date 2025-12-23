''' Data model for exchange records.'''

from dataclasses import dataclass
from typing import Optional


@dataclass
class ExchangeRecord:
    '''Data model for exchange records.'''

    message_type: str
    custom_house_code: str
    user_job_no: str
    user_job_date: Optional[str]
    be_number: Optional[str]
    be_date: Optional[str]
    currency_code: str
    standard_currency: str
    unit_rs: Optional[str]
    rate: Optional[str]
    effective_date: Optional[str]
    bank_name: Optional[str]
    certificate_number: Optional[str]
    certificate_date: Optional[str]


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
