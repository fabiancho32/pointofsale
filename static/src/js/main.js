odoo.define('pointofsale.main', function(require) {
"use strict";

var PosDB = require('point_of_sale.DB');
var core = require('web.core');
var module = require('point_of_sale.models');
var Model = require('web.DataModel');
var gui = require('point_of_sale.gui');
var screens = require('point_of_sale.screens');
var _t = core._t;


// extending client screen behavior
screens.ProductScreenWidget.include({

	this.metodo_prueba = function(event){
		var self = this;

		if(event.type == "keypress"){
			console.log('se presiono una tecla');
		}
		self.el.querySelector('.searchbox input').addEventListener('keypress', metodo_prueba);
	},



});


});
