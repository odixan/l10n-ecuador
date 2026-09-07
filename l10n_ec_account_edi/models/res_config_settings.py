from odoo import _, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_ec_type_environment = fields.Selection(
        related="company_id.l10n_ec_type_environment", readonly=False
    )
    l10n_ec_key_type_id = fields.Many2one(
        comodel_name="sri.key.type",
        related="company_id.l10n_ec_key_type_id",
        readonly=False,
    )
    l10n_ec_invoice_version = fields.Selection(
        related="company_id.l10n_ec_invoice_version", readonly=False
    )
    l10n_ec_liquidation_version = fields.Selection(
        related="company_id.l10n_ec_liquidation_version", readonly=False
    )
    l10n_ec_credit_note_version = fields.Selection(
        related="company_id.l10n_ec_credit_note_version", readonly=False
    )
    l10n_ec_debit_note_version = fields.Selection(
        related="company_id.l10n_ec_debit_note_version", readonly=False
    )
    l10n_ec_final_consumer_limit = fields.Float(
        string="Invoice Sales Limit Final Consumer",
        config_parameter="l10n_ec_final_consumer_limit",
        default=50.0,
        readonly=False,
    )
    l10n_ec_edi_provider_vat = fields.Char(
        related="company_id.l10n_ec_edi_provider_vat", readonly=False
    )

    def action_open_journal_sequence_config(self):
        return {
            "name": _("Journal Sequential Configuration"),
            "type": "ir.actions.act_window",
            "res_model": "account.journal",
            "view_mode": "list,form",
            "domain": [
                ("l10n_latam_use_documents", "=", True),
                ("company_id", "=", self.env.company.id),
                ("country_code", "=", "EC"),
            ],
            "context": {
                "search_default_group_by_type": 1,
            },
        }
