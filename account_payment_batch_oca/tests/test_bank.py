# © 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestBank(TransactionCase):
    def test_bank(self):
        # res.bank was removed in Odoo 20: bank data (incl. BIC) now lives
        # directly on res.partner.bank, and the BIC length check of
        # account_payment_base_oca applies to bank_bic.
        bank_account = self.env["res.partner.bank"].create(
            {
                "account_number": "FR7630001007941234567890185",
                "partner_id": self.env.ref("base.main_partner").id,
                "bank_name": "Qonto",
                "bank_bic": "QNTOFRP1XXX",
            }
        )
        with self.assertRaises(ValidationError):
            bank_account.bank_bic = "TEST"
