from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountJournal(models.Model):
    _inherit = "account.journal"

    l10n_ec_sequence_start = fields.Integer(
        string="Sequential Start Number",
        default=1,
        help="Starting number for electronic document sequential numbering. "
        "Default is 1, but can be set to any number (e.g., 999). "
        "If this number already exists, the system will use the next available number.",
    )

    @api.depends("l10n_latam_use_documents")
    def _compute_compatible_edi_ids(self):
        # Extend dependency: base compute depends on type/company/country but
        # Ecuador's _is_compatible_with_journal also checks l10n_latam_use_documents.
        return super()._compute_compatible_edi_ids()

    @api.depends("l10n_latam_use_documents")
    def _compute_edi_format_ids(self):
        return super()._compute_edi_format_ids()

    @api.constrains("l10n_ec_sequence_start")
    def _check_l10n_ec_sequence_start(self):
        for journal in self:
            if (
                journal.l10n_ec_require_emission
                and journal.l10n_ec_sequence_start < 1
            ):
                raise ValidationError(
                    _("Sequential start number must be greater than 0.")
                )
