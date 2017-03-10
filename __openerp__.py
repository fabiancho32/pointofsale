{
    'name': 'Colombia - Punto de venta (Terceros)',
    'category': 'Localization',
    'version': '0.9',
    'author': 'Dreamsoft',
    'license': 'AGPL-3',
    'maintainer': 'mantenimiento@dreamsoft.com',
    'website': 'https://www.dreamsoft.com',
    'summary': 'Colombia Punto de Venta: Extending the Contact Module in the Point of Sales Module - Odoo 9.0',
    'images': [],
    'description': """
Colombia Punto de Venta:
======================
_
    * This Module extends the  l10n_co_point_of_sale / Contact form in the Point of Sales Module
    """,
    'depends': [
        'l10n_co_point_of_sale'
    ],
    
    'data': ['views/tipoMoneda_view.xml'],
    'qweb': ['static/src/xml/pos.xml'],

    'installable': True,
}

