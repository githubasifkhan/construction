# -*- coding: utf-8 -*-

# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api
from openerp.tools.translate import _

	
PARAMS = [
	('enterprise_backend_theme.new_name', _('BRJ CLOUDS')),
	('enterprise_backend_theme.new_title', _('BRJ CLOUDS')),
	('enterprise_backend_theme.new_website', '#'),
	('enterprise_backend_theme.favicon_url', ''),
	('enterprise_backend_theme.send_publisher_warranty_url', '0'),
	('enterprise_backend_theme.planner_footer', ''),
	('enterprise_backend_theme.icon_url', ''),
	('enterprise_backend_theme.apple_touch_icon_url', ''),
	('web.login_theme', '1'),
	('web.sidebar_theme', '2'),
	('web.switcher_theme', '1'),
	('web.enable_footer', '1'),
	('web.login_logo',''),
]

class ResUsers(models.Model):

	_inherit = 'res.users'

	sidebar_visible = fields.Boolean("Show App Sidebar", default=True)
	#Antash_Code
	toggle_sidebar = fields.Selection([('full','Full'),('half','Half'),('none','None')],default='full')

	def __init__(self, pool, cr):
		""" Override of __init__ to add access rights on notification_email_send
			and alias fields. Access rights are disabled by default, but allowed
			on some specific fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
		"""
		init_res = super(ResUsers, self).__init__(pool, cr)
		# duplicate list to avoid modifying the original reference
		type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
		type(self).SELF_WRITEABLE_FIELDS.extend(['sidebar_visible'])
		# duplicate list to avoid modifying the original reference
		type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
		type(self).SELF_READABLE_FIELDS.extend(['sidebar_visible'])
		return init_res

class IrConfigParameter(models.Model):
	_inherit = 'ir.config_parameter'

	@api.model
	def get_debranding_parameters(self):
		res = {}
		for param, default in PARAMS:
			value = self.env['ir.config_parameter'].get_param(param, default)
			res[param] = value.strip()
		return res

	@api.model
	def create_debranding_parameters(self):
		for param, default in PARAMS:
			if not self.env['ir.config_parameter'].get_param(param):
				self.env['ir.config_parameter'].set_param(param, default or ' ')