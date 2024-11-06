import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class AddressMixin(models.AbstractModel):
    _inherit = 'kw.address.mixin'

    contact_person = fields.Char()

    @api.model
    def _get_default_address_format(self):
        return '%(contact_person)s\n%(street)s\n%(street2)s\n%(city)s ' \
               '%(state_code)s %(zip)s\n%(country_name)s'

    def _display_address(self):
        self.ensure_one()
        args = {
            'contact_person': self.contact_person or '',
            'state_code': self.state_id.code or '',
            'state_name': self.state_id.name or '',
            'country_code': self.country_id.code or '',
            'country_name': self._get_country_name(), }
        for field in self._formatting_address_fields():
            args[field] = getattr(self, field) or ''
        return '%(contact_person)s\n%(street)s\n%(street2)s\n%(city)s' \
               ' %(state_code)s %(zip)s\n%(country_name)s' % args


class Address(models.Model):
    _inherit = 'kw.address'

    @api.depends('contact_person', 'street', 'street2',
                 'zip', 'city', 'state_id', 'country_id')
    def _compute_name(self):
        for obj in self:
            obj.name = obj._display_address()
