from odoo import api, fields, models
from odoo.tools.translate import _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class MyCompanyVehicle(models.Model):
    _name = 'my.company.vehicle'

    name = fields.Char(string='Name', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    fuel_type = fields.Selection([
        ('diesel', 'Diesel'),
        ('gasoline,', 'gasoline,'),
        ('electric', 'Electric'),
    ], string='Fuel Type')
    mileage = fields.Float(string='Mileage')
    last_service_date = fields.Date(string='Last Service Date')
    needs_service = fields.Boolean(string='Needs Service', compute='_compute_needs_service')
    partner_id = fields.Many2one('res.partner', string='Contact')

    @api.depends('mileage', 'last_service_date')
    def _compute_needs_service(self):
        for record in self:
            if record.mileage > 20000:
                record.needs_service = True
            elif record.last_service_date:
                last_service_date = fields.Date.from_string(record.last_service_date)
                if datetime.now().date() > last_service_date + timedelta(days=180):
                    record.needs_service = True
                else:
                    record.needs_service = False
            else:
                record.needs_service = False

    @api.onchange('fuel_type')
    def _onchange_fuel_type(self):
        for record in self:
            if record.fuel_type == 'electric':
                record.mileage = 0

    def action_shedule_service(self):
        for record in self:
            pass

    @api.model
    def create(self, vals):
        if 'license_plate' in vals:
            existing_vehicle = self.search([('license_plate', '=', vals['license_plate'])])
            if existing_vehicle:
                raise ValidationError(_('A vehicle with this license plate already exists.'))
        return super(MyCompanyVehicle, self).create(vals)
