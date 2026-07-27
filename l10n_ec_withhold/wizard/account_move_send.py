from odoo import api, models


class AccountMoveSend(models.AbstractModel):
    _inherit = "account.move.send"

    @api.model
    def _prepare_invoice_pdf_report(self, invoices_data):
        """Prepare the pdf report for the invoices passed as parameter.
        :param invoices_data: dict {account.move: invoice_data}
        """
        withhold_invoices_data = {
            invoice: invoice_data
            for invoice, invoice_data in invoices_data.items()
            if invoice.is_purchase_withhold()
        }
        regular_invoices_data = {
            invoice: invoice_data
            for invoice, invoice_data in invoices_data.items()
            if not invoice.is_purchase_withhold()
        }

        ActionReport = self.env["ir.actions.report"]
        report_idxml = "l10n_ec_withhold.action_report_withholding_ec"
        for invoice, invoice_data in withhold_invoices_data.items():
            content, _report_format = ActionReport._render(report_idxml, invoice.ids)
            invoice_data["pdf_attachment_values"] = {
                "raw": content,
                "name": invoice._get_invoice_report_filename(),
                "mimetype": "application/pdf",
                "res_model": invoice._name,
                "res_id": invoice.id,
                "res_field": "invoice_pdf_report_file",
            }

        if regular_invoices_data:
            super()._prepare_invoice_pdf_report(regular_invoices_data)
