# -*- coding: utf-8 -*-
{
    'name': "RegistrationForm",

    'summary': """
       Part of BMG's technical test""",

    'description': """
        Part of BMG's technical test
    """,

    'author': "Muftah Afrizal Pangestu",
    'website': "https://www.linkedin.com/in/muftah-pangestu/",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable':True,
    'application':True,
}