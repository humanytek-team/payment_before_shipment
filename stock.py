# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError

_CONTADO = 'immediate payment'

class StockPicking(models.Model):
    _inherit = "stock.picking"


    @api.multi
    def do_new_transfer(self):
        #print 'do_new_transfer'
        #CHECKS IF RECORD HAS RELATED INVOICES
        for picking in self:
            invoice_ids = []
            if picking.group_id:
                sale_ids = self.env['sale.order'].search([('procurement_group_id','=',picking.group_id.id)])
                if sale_ids:
                    invoice_ids = [sale.invoice_ids for sale in sale_ids]
                    #print 'invoice_ids: ',invoice_ids
            #if invoice_ids != []:
            for invoice_group in invoice_ids:
                for invoice in invoice_group:
                    #print str(invoice.id)+', state: '+invoice.state
                    #if invoice.state not in ('cancel','done')
                    if invoice.payment_term_id and invoice.payment_term_id.name.lower() == _CONTADO:
                        #print 'xxxx'
                        if invoice.state not in ('paid','cancel') and invoice.type in ('out_invoice',):
                            raise UserError(_('No se puede ralizar el movimiento\nLa factura %s no esta pagada'%(invoice.number,)))
                        # if not invoice.payment_ids:
                        #     raise UserError(_('La factura no tiene pagos aplicados'))
                        # for payment in invoice.payment_ids:
                        #     print 'payment: ',payment.name
                        #     if payment.state not in ('reconciled'):
                        #         raise UserError(_('El pago '+str(payment.name)+' no esta aplicado'))

        return super(StockPicking, self).do_new_transfer()
