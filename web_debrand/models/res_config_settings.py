# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _default_company(self):
        return self.env['res.company'].search([], limit=1)

    company_id = fields.Many2one('res.company', string="res company", default=_default_company, required=True)
    company_logo = fields.Binary('Company Logo', related='company_id.company_logo')
    company_name = fields.Char('Company Name', related='company_id.company_name')
    company_favicon = fields.Binary('Company Favicon', related='company_id.company_favicon')
    company_website = fields.Char('Company Website', related='company_id.company_website')

    @api.multi
    def error(self):
    	raise ValueError

    # Sample Warning Dialogue
    @api.multi
    def warning(self):
    	raise Warning(_("This is a Warning"))