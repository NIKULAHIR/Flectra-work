# -*- coding: utf-8 -*-


{
    'name': 'ONLINE E-store',
    'author': 'NIKUL',
    'version': '1.1',
    'summary': 'Sell Product and Track store ',
    'sequence': 30,
    'description': " E-coomarce application",
    'category': 'Online Product Selling',

    'depends': ['base'],
    'data': [
        'views/store_view.xml',
        'views/store_keeper_view.xml',
        'views/store_amenity_view.xml',],
    'demo': [],
    'qweb': [],
    'application': True,
    'bootstrap': True,

    'installable': True,
    'application': True,
    'auto_install': False,
  
}
