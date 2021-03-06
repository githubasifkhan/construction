# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Accounting Reports',
    'version': '12.0.0.1',
    'category': 'Accounting',
    'summary': 'Accounting Reports For Odoo 12',
    'sequence': '10',
    'author': 'The Anonymous, Odoo SA',
    'company': 'The Anonymous',
    'maintainer': 'The Anonymous',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/account_financial_report_data.xml',
        'views/account_report_view.xml',
        'views/report_financial.xml',
        'views/search_template_view.xml',
        'views/report_followup.xml',
        'views/partner_view.xml',
        'views/followup_view.xml',
        'views/account_journal_dashboard_view.xml',
        'views/account_pdf_reports.xml',
        'views/accounting_reports_settings.xml',
        'wizards/partner_ledger.xml',
        'wizards/general_ledger.xml',
        'wizards/trial_balance.xml',
        'wizards/balance_sheet.xml',
        'wizards/profit_and_loss.xml',
        'wizards/tax_report.xml',
        'wizards/aged_partner.xml',
        'wizards/journal_audit.xml',
        'reports/report.xml',
        'reports/report_partner_ledger.xml',
        'reports/report_general_ledger.xml',
        'reports/report_trial_balance.xml',
        'reports/report_financial.xml',
        'reports/report_tax.xml',
        'reports/report_aged_partner.xml',
        'reports/report_journal_audit.xml',
        'views/res_config_settings_views.xml',

    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'images': ['static/description/banner.gif'],
    'qweb': [
        'static/src/xml/account_report_template.xml',
    ],
}
