# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api
from openerp.tools.translate import _

class moneda(models.Model):
	_name = 'tipo.moneda'
	
	_description = 'Se crea la denominacion del tipo de moneda del pais'
	
	"""
	metodo que nos permite de acuerdo a el tipo de moneda que tiene la compania
	cargar por defecto ese tipo de moneda, cuando estemos creando el valor de estas
	"""
	def buscar_moneda_localizacion(self):
		return self.env['res.company'].browse(self.env.user.company_id.id).currency_id
	
	name =  fields.Char('Valor moneda', size=48, required=True)
	moneda_id = fields.Many2one('res.currency', 'Unidad monetaria', default=buscar_moneda_localizacion)
	



moneda()
