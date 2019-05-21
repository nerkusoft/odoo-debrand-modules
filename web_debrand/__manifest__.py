# -*- coding: utf-8 -*-
{
    'name': "Web Debranding",
    'version': "11.0.1.0",
    'summary': """Web Debrand """,
    'description': """ Web Debrand""",
    'company': "Nerku",
    'website': "https://nerku.com/",
    'category': 'Tools',
    'depends': ['base','base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/template_debrand.xml',
        'views/res_company_extend.xml'],
    'demo': [],
    'qweb': ["static/src/xml/*.xml"],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': False
}
