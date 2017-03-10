# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api
from openerp.tools.translate import _

class moneda(models.Model):
	_name = 'tipo.moneda'
	
	_description = 'Se crea la denominacion del tipo de moneda del pais'
	
	
	name =  fields.Char('Valor moneda', size=48, required=True)
	moneda_id = fields.Many2one('res.currency', 'Unidad monetaria')
	


moneda()
