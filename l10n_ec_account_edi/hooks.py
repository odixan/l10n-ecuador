import logging

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Migrate company-level sequence start to per-journal field.

    Copies the existing l10n_ec_invoice_sequence_start value from each company
    to all its journals that use LATAM document numbering.
    """
    _logger.info(
        "Migrating l10n_ec_invoice_sequence_start from company to journals..."
    )
    # Check if old column still exists
    env.cr.execute(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_name = 'res_company' "
        "AND column_name = 'l10n_ec_invoice_sequence_start'"
    )
    if not env.cr.fetchone():
        _logger.info("Old column not found, skipping migration.")
        return

    companies = env["res.company"].search(
        [("account_fiscal_country_id.code", "=", "EC")]
    )
    for company in companies:
        env.cr.execute(
            "SELECT l10n_ec_invoice_sequence_start FROM res_company WHERE id = %s",
            (company.id,),
        )
        result = env.cr.fetchone()
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
                "Set l10n_ec_sequence_start=%s for %d journals in company %s",
                start_number,
                len(journals),
                company.name,
            )
