# -*- coding: utf-8 -*-
{
    'name' : 'Check if invoice is paid before shipping',
    'version' : '1',
    'author': 'Humanytek',
    'description': """
        Checks if invoice is paid, before shipping products to customer
    """,
    'category' : 'Account',
    'depends' : ['stock','l10n_mx_einvoice'],
    'data': [
        #'sale_view.xml',  
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
