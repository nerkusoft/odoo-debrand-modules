# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_logo = fields.Binary(string="Company Logo", help="This field holds the image used for the Company Logo.")
    company_name = fields.Char(string="Company Name", help="Branding Name")
    company_favicon = fields.Binary(string="Company Favicon", help="This field holds the image used for as favicon.")
    company_website = fields.Char(string="Company URL", help="Website URL for company")
    favicon_url = fields.Char("Url", compute='_get_favicon')
    company_logo_url = fields.Char("Url", compute='_get_company_logo')

    @api.one
    @api.depends('company_favicon')
    def _get_favicon(self):
        self.favicon_url = 'data:image/png;base64,' + str(self.company_favicon)

    @api.one
    @api.depends('company_logo')
    def _get_company_logo(self):
        self.company_logo_url = 'data:image/png;base64,' + str(self.company_logo)
