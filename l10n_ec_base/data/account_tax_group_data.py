# data to update into taxes
# return dict(tax_idxml: dict(values to write into tax))
# IMPORTANT: XML IDs should NOT include company prefix or module prefix
# The chart template system automatically adds "account.{company_id}_" prefix
# e.g., "tax_group_vat_12" becomes "account.2_tax_group_vat_12" for company 2
TAX_GROUP_DATA_EC = {
    # VAT tax groups - all use SRI code "2" (IVA)
    "tax_group_vat_12": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat_05": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat_08": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat_13": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat14": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat_15": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat0": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat_not_charged": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_vat_exempt": {"l10n_ec_xml_fe_code": "2"},
    # Withholding groups
    "tax_group_withhold_income_sale": {"l10n_ec_xml_fe_code": "1"},
    "tax_group_withhold_income_purchase": {"l10n_ec_xml_fe_code": "1"},
    "tax_group_withhold_vat_sale": {"l10n_ec_xml_fe_code": "2"},
    "tax_group_withhold_vat_purchase": {"l10n_ec_xml_fe_code": "2"},
    # Special taxes
    "tax_group_ice": {"l10n_ec_xml_fe_code": "3"},
    "tax_group_irbpnr": {"l10n_ec_xml_fe_code": "5"},
    "tax_group_outflows": {"l10n_ec_xml_fe_code": "6"},
}
