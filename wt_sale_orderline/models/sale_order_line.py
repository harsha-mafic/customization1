from odoo import api, fields, models, _
from odoo.exceptions import Warning


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_delivered = fields.Boolean()
    qty_remained = fields.Float(compute='_check_availability', string="Remained to deliver")
    remaining_valuation = fields.Float(string="remaining valuation")
    done_valuation = fields.Float(string="done valuation")

    def _check_availability(self):
        for rec in self:
            rec.is_delivered = True
            if ((rec.qty_delivered != rec.product_uom_qty) and (rec.qty_delivered < rec.product_uom_qty)) and (rec.state not in ['sent', 'draft', 'cancel']):
                rec.is_delivered = False
            rec.qty_remained = rec.product_uom_qty - rec.qty_delivered
            rec.done_valuation = rec.qty_delivered * rec.price_unit
            rec.remaining_valuation = rec.qty_remained * rec.price_unit

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_delivered_fully = fields.Boolean()
    temp_bool = fields.Boolean(compute='_check_delivery_status')

    def _check_delivery_status(self):
        for order in self:
            order.is_delivered_fully = False
            flag = 1
            for rec in order.order_line:
                rec.is_delivered = False
                if (rec.qty_delivered >= rec.product_uom_qty) and rec.state not in ['sent', 'draft', 'cancel']:
                    rec.is_delivered = True
                else:
                    flag = 0
                    break
            if flag and order.order_line:
                order.is_delivered_fully = True
            order.temp_bool = True

    def action_mark_as_done(self):
        self.picking_ids.filtered(lambda x: x.state not in ['done', 'cancel']).action_cancel()
        for rec in self.order_line:
            rec.is_delivered = True
            rec.is_delivered_fully = True
