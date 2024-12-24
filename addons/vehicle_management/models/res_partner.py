from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    vehicle_ids = fields.One2many('my.company.vehicle', 'partner_id', string='Vehicles')
    vehicle_count = fields.Integer(string='Vehicle Count', compute='_compute_vehicle_count')

    @api.depends('vehicle_ids')
    def _compute_vehicle_count(self):
        for record in self:
            record.vehicle_count = len(record.vehicle_ids)
