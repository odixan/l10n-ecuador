import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Migrate company-level sequence start to per-journal field on upgrade."""
    if not version:
        return

    # Check if old column still exists
    cr.execute(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_name = 'res_company' "
        "AND column_name = 'l10n_ec_invoice_sequence_start'"
    )
    if not cr.fetchone():
        _logger.info("Old column l10n_ec_invoice_sequence_start not found, skipping.")
        return

    env = api.Environment(cr, SUPERUSER_ID, {})
    companies = env["res.company"].search(
        [("account_fiscal_country_id.code", "=", "EC")]
    )
    for company in companies:
        cr.execute(
            "SELECT l10n_ec_invoice_sequence_start FROM res_company WHERE id = %s",
            (company.id,),
        )
        result = cr.fetchone()
        start_number = result[0] if result and result[0] else 1

        journals = env["account.journal"].search(
            [
                ("company_id", "=", company.id),
                ("l10n_latam_use_documents", "=", True),
            ]
        )
        if journals:
            journals.write({"l10n_ec_sequence_start": start_number})
            _logger.info(
                "Migrated l10n_ec_sequence_start=%s for %d journals in company %s",
                start_number,
                len(journals),
                company.name,
            )
