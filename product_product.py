# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import openerp
from openerp import models, fields, api
from openerp.osv import orm, fields, osv

import datetime 
#import pdb
#import logging
#_logger = logging.getLogger(__name__)

class product_product(osv.osv):

    _name = 'product.product'
    _inherit = 'product.product' 

    def _fnct_pricelist_price(self, cr, uid, ids, field_name, args, context=None):
        product_pricelist_obj = self.pool.get('product.pricelist')

        if context is None:
            context = {}
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            price_pricelist=self.pool.get('product.pricelist').price_get(cr,uid,[5,12,29],product.id,1.0,1,{'uom':1,'date':date.today()})

            if 1 in price_pricelist:
                res[product.id] = "3:"+str(price_pricelist[1]) + "\n4:"+str(price_pricelist[2])+ "\n5:"+str(price_pricelist[2])
            else : 
                res[product.id] = str('--')


        return res

    _columns = {
        'pricelist_principal': fields.function(_fnct_pricelist_price, string='lista principal',type='char', size=256,),
    }

class product_template(osv.osv):

    _name = 'product.template'
    _inherit = 'product.template' 

    def _fnct_pricelist_price(self, cr, uid, ids, field_name, args, context=None):
        product_pricelist_obj = self.pool.get('product.pricelist')

        if context is None:
            context = {}
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            price_pricelist=self.pool.get('product.pricelist').price_get(cr,uid,[5,12,29],product.id,1.0,1,{'uom':1,'date':date.today()})

            if 1 in price_pricelist:
                res[product.id] = "3:"+str(price_pricelist[1]) + "\n4:"+str(price_pricelist[2])+ "\n5:"+str(price_pricelist[2])
            else : 
                res[product.id] = str('--')


        return res

    _columns = {
        'pricelist_principal': fields.function(_fnct_pricelist_price, string='Mayoristas',type='char', size=256,),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: