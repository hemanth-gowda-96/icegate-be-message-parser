"""
ICEGATE BE Message Format 2.23 - Field Specifications for EXCHANGE records (CACH101).
Contains field definitions, validation rules, and type specifications.
"""


# ------------------------------
# Field Specification Table (CACH101)
# ------------------------------
EXCHANGE_FIELD_SPECS = [
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


PERMISSION_FIELD_SPECS = [
    ("message_type",             "C",     1,     {"FINAL": "F", "SEZ": "F"}),
    ("custom_house_code",        "C",     6,     {"FINAL": "K", "SEZ": "K"}),
    ("user_job_no",              "N",     7,     {"FINAL": "K", "SEZ": "K"}),
    ("user_job_date",            "DATE",  8,     {"FINAL": "K", "SEZ": "K"}),

    ("be_number",                "N",     7,     {"FINAL": "X", "SEZ": "X"}),
    ("be_date",                  "DATE",  8,     {"FINAL": "X", "SEZ": "X"}),

    ("permission_code",          "C",     3,     {"FINAL": "M", "SEZ": "M"}),
    ("reasons_for_request",      "C",     2000,  {"FINAL": "M", "SEZ": "M"}),
]


TABLE_BE_FIELDS_SPECS = [
    # Fields 1-6
    ("message_type",             "C",     1,     {"FINAL": "F", "SEZ": "F"}),
    ("custom_house_code",        "C",     6,     {"FINAL": "K", "SEZ": "K"}),
    ("user_job_no",              "N",     7,     {"FINAL": "K", "SEZ": "K"}),
    ("user_job_date",            "DATE",  8,     {"FINAL": "K", "SEZ": "K"}),
    ("be_number",                "N",     7,     {"FINAL": "X", "SEZ": "X"}),
    ("be_date",                  "DATE",  8,     {"FINAL": "X", "SEZ": "X"}),
    ("be_type",                  "C",     4,     {"FINAL": "M", "SEZ": "M"}),
    ("iec_code",                 "C",     10,    {"FINAL": "M", "SEZ": "M"}),
    ("branch_sr_no",             "N",     3,     {"FINAL": "M", "SEZ": "M"}),
    ("importer_name",            "C",     50,    {"FINAL": "O", "SEZ": "O"}),
    ("address_1",                "C",     35,    {"FINAL": "O", "SEZ": "O"}),
    ("address_2",                "C",     35,    {"FINAL": "O", "SEZ": "O"}),
    ("city",                     "C",     35,    {"FINAL": "O", "SEZ": "O"}),
    ("state",                    "C",     25,    {"FINAL": "O", "SEZ": "O"}),
    ("pin",                      "C",     6,     {"FINAL": "O", "SEZ": "O"}),
    ("class",                    "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("mode_of_transport",        "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("importer_type",            "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("kachcha_be",               "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("high_sea_sale_flag",       "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("port_of_origin",           "C",     6,     {"FINAL": "M", "SEZ": "M"}),
    ("cha_code",                 "C",     15,    {"FINAL": "M", "SEZ": "X"}),
    ("country_of_origin",        "C",     2,     {"FINAL": "M", "SEZ": "M"}),
    ("country_of_consignment",   "C",     2,     {"FINAL": "M", "SEZ": "M"}),
    ("port_of_shipment",         "C",     6,     {"FINAL": "M", "SEZ": "M"}),
    ("green_channel_requested",  "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("section_48_requested",     "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("prior_be",                 "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("authorized_dealer_code",   "C",     10,    {"FINAL": "M", "SEZ": "M"}),
    ("first_check_requested",    "C",     1,     {"FINAL": "M", "SEZ": "M"}),
    ("warehouse_code",           "C",     8,     {"FINAL": "O", "SEZ": "M"}),
    ("warehouse_customs_site_id", "N",     6,     {"FINAL": "O", "SEZ": "M"}),
    ("warehouse_be_no",          "C",     7,     {"FINAL": "O", "SEZ": "M"}),
    ("warehouse_be_date",        "DATE",  8,     {"FINAL": "O", "SEZ": "M"}),
    ("no_of_packages_released",  "N",     8,     {"FINAL": "O", "SEZ": "M"}),
    ("package_code",             "C",     3,     {"FINAL": "O", "SEZ": "M"}),
    ("gross_weight",             "N12,3", None,  {"FINAL": "O", "SEZ": "M"}),
    ("unit_of_measurement",      "C",     3,     {"FINAL": "O", "SEZ": "M"}),
    ("purchase_on_high_seas",    "N6,2",  None,  {"FINAL": "O", "SEZ": "O"}),
    ("miscellaneous_load",       "N6,2",  None,  {"FINAL": "O", "SEZ": "O"}),
    ("ucr",                      "C",     35,    {"FINAL": "O", "SEZ": "O"}),
    ("ucr_type",                 "C",     6,     {"FINAL": "O", "SEZ": "O"}),
    ("payment_method_code",      "C",     1,     {"FINAL": "M", "SEZ": "O"}),
]
