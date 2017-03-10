# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv
from openerp.tools.translate import _

class moneda(osv.osv):
	_name = 'tipo.moneda'
	
	_description = 'Se crea la denominacion del tipo de moneda del pais'
	
	_columns = {
	   'name': fields.char('Moneda', size=48, required=True),
	   'moneda_id': fields.many2one('res.currency', 'Moneda'),
	}


moneda()
