# -*- coding: utf-8 -*-
# License LGPL-3.0 or later ().

{
    "name": "Enterprise Backend Theme",
    "summary": "Backend Theme",
    "version": "12.0.1",
    "category": "Theme/Backend",
    "website": "www.solutionfounder.com",
    "description": """
       
    """,
    "author": "Solution Founder Team",
    "license": "LGPL-3",
    "installable": True,
    'auto_install': True,
    "depends": [
        'base',
        'mail',
        'web',
        'web_responsive',
    ],
    "data": [
        'views/assets.xml',
        'views/res_company_view.xml',
        'views/users.xml',
    ],
    'qweb': [
        'static/src/xml/web.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/jpv_theme_screenshot.png', 
    ],
}

