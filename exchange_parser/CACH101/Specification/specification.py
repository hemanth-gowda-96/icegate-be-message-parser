"""
ICEGATE BE Message Format 2.23 - Field Specifications for EXCHANGE records (CACH101).
Contains field definitions, validation rules, and type specifications.
"""


# ------------------------------
# Field Specification Table (CACH101)
# ------------------------------
FIELD_SPECS = [
    ("message_type",             "C",     1,     {"FINAL": "F", "SEZ": "F"}),
    ("custom_house_code",        "C",     6,     {"FINAL": "K", "SEZ": "K"}),
    ("user_job_no",              "N",     7,     {"FINAL": "K", "SEZ": "K"}),
    ("user_job_date",            "DATE",  8,     {"FINAL": "K", "SEZ": "K"}),

    ("be_number",                "N",     7,     {"FINAL": "X", "SEZ": "X"}),
    ("be_date",                  "DATE",  8,     {"FINAL": "X", "SEZ": "X"}),

    ("currency_code",            "C",     3,     {"FINAL": "K", "SEZ": "K"}),
    ("standard_currency",        "C",     1,     {"FINAL": "M", "SEZ": "M"}),

    ("unit_rs",                  "N7,2",  None,  {"FINAL": "O", "SEZ": "O"}),
    ("rate",                     "N9,4",  None,  {"FINAL": "O", "SEZ": "O"}),

    ("effective_date",           "DATE",  8,     {"FINAL": "O", "SEZ": "O"}),

    ("bank_name",                "C",     35,    {"FINAL": "O", "SEZ": "O"}),
    ("certificate_number",       "C",     20,    {"FINAL": "O", "SEZ": "O"}),
    ("certificate_date",         "DATE",  8,     {"FINAL": "O", "SEZ": "O"}),
]
