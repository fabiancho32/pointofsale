odoo.define('pointofsale.screens_inherit', function(require) {
"use strict";

var PosDB = require('point_of_sale.DB');
var core = require('web.core');
var module = require('point_of_sale.models');
var Model = require('web.DataModel');
var gui = require('point_of_sale.gui');
var screens = require('point_of_sale.screens');
var _t = core._t;

var round_pr = utils.round_precision;


var set_buscar_carrito_compra = ActionButtonWidget.extend({
    template: 'BuscarCarritoCompra',
    button_click: function () {
        var self = this;
        var selection_list = _.map(self.pos.fiscal_positions, function (fiscal_position) {
            return {
                label: fiscal_position.name,
                item: fiscal_position
            };
        });
        self.gui.show_popup('selection',{
            title: _t('Select tax'),
            list: selection_list,
            confirm: function (fiscal_position) {
                var order = self.pos.get_order();
                order.fiscal_position = fiscal_position;
                order.trigger('change');
            }
        });
    },
});

define_action_button({
    'name': 'set_buscar_carrito',
    'widget': set_buscar_carrito_compra,
    'condition': function(){
        return this.pos.fiscal_positions.length > 0;
    },


return {
    set_buscar_carrito_compra: set_buscar_carrito_compra,
};



});