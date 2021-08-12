from odoo import api, fields, models, _
from odoo.exceptions import Warning


class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	is_delivered = fields.Boolean()
	qty_remained = fields.Float(compute='_check_availability', string="Remained to deliver")

	def _check_availability(self):
		for rec in self:
			rec.is_delivered = True
			if ((rec.qty_delivered != rec.product_uom_qty) and (rec.qty_delivered < rec.product_uom_qty)) and (rec.state not in ['sent', 'draft', 'cancel']):
				rec.is_delivered = False
			rec.qty_remained = rec.product_uom_qty - rec.qty_delivered


