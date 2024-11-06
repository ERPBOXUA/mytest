# -*- coding: utf-8 -*-
{
    'name': 'Delivery carrier shipping state',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Delivery',
    'description': """Delivery carrier shipping state""",
    'author': 'AnstRoute, SimplicIT',
    'website': 'https://antsroute.com/',
    'depends': [
        'base',
        'delivery',
        'stock_delivery',
    ],
    'data': [
        'views/delivery_carrier.xml',
        'views/stock_picking.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'EUR',
}
