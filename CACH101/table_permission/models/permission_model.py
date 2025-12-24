''' Data model for permission records.'''

from dataclasses import dataclass
from typing import Optional


@dataclass
class TablePermissionRecord:
    '''Data model for permission records.'''

    message_type: str
    custom_house_code: str
    user_job_no: str
    user_job_date: Optional[str]
    be_number: Optional[str]
    be_date: Optional[str]
    permission_code: Optional[str]
    reasons_for_request: Optional[str]
