odoo.define('enterprise_backend_theme.Menu', function(require) {
	"use strict";
	var core = require('web.core');
	var session = require('web.session');
	var Widget = require('web.Widget');
	var AppsMenu = require('web.AppsMenu');
	//AppsMenu
	AppsMenu.include({
		getLogo: function () {
			var url = session.url('/web/image', {model: 'res.company', field: 'logo', id: session.company_id, unique: false});
			return {'logo':url,'name':'Hi ' + session.name}
		},
	});
});