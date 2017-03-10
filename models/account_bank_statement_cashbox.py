# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api
from openerp.tools.translate import _
import logging
_logger = logging.getLogger(__name__)



class account_bank_statement_cashbox(models.Model):
	_name = 'account.bank.statement.cashbox'
		
	_inherit = 'account.bank.statement.cashbox'


	""" 
	Metodo que nos permite cargar las denominaciones
	de las monedas por defecto, este metodo es de 
	odoo por eso se usa el @api.Model
	"""
	@api.model
	def default_get(self, fields):
		res = super(account_bank_statement_cashbox,self).default_get(fields)
		tipo_moneda_id = self.tipo_monedas()
		tipo_monedas = []
		if tipo_moneda_id:
			for datos in self.env['tipo.moneda'].browse(tipo_moneda_id):
				tipo_monedas.append((0,0,{'coin_value' : int(datos.name)}))
			
			if tipo_monedas:
				res['cashbox_lines_ids'] = tipo_monedas

		return res

	""" 
	Metodo que nos permite buscar el valor de las monedas
	que el usuario a creado en el modelo de tipo.moneda
	"""
	def tipo_monedas(self):
		tipo_moneda_id = self.env['tipo.moneda'].search([])
		tipo_monedas = []
		if tipo_moneda_id:
			for datos in tipo_moneda_id:
				tipo_monedas.append(datos.id)
			return tipo_monedas
		return None

		


account_bank_statement_cashbox()