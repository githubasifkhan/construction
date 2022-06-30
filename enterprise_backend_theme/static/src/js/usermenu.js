odoo.define('enterprise_backend_theme.SideBar', function (require) {
"use strict";

var user_menu = require('web.UserMenu');

	user_menu.include({
		events: {
        	'click .side_menu': '_change_sidebar',
    	},

		start:function(){
			this._super.apply(this, arguments)
			var session = this.getSession();
			this._rpc({
                model: 'res.users',
                method: 'search_read',
                fields: ['toggle_sidebar'],
                domain: [['id', '=',session.uid]],
            }).then(function (view) {
              	var toggle_sidebar = view[0].toggle_sidebar
              	if (toggle_sidebar=='full'){
              		$(".o_sidebar_menu").removeAttr('style')
              		$('a[data-work="half"]').removeClass('d-none')
              		$('a[data-work="half"]').addClass('active')
              	}
              	else if (toggle_sidebar=='half'){
              		var span_tag = $('#sidebar').find('span').hide()
					$(".o_sidebar_menu").animate({'width':85+'px'})
              		$('a[data-work="none"]').removeClass('d-none')
              		$('a[data-work="none"]').addClass('active')
              		
              	}
              	else {
              		$(".o_sidebar_menu").animate({'width':0+'px'})
              		$('a[data-work="full"]').removeClass('d-none')
              		$('a[data-work="full"]').addClass('active')
              	}
            })
		},

		_change_sidebar:function(){
			var e = $(this.el).find('a.active');
			var session = this.getSession();
			if (e){
				var work = e.attr('data-work');
				if ('half'===work){
					var span_tag = $('#sidebar').find('span').hide();
					$(".o_sidebar_menu").animate({'width':85+'px'})
					e.addClass('d-none')
					e.removeClass('active')
					$("[data-work='none']").removeClass('d-none')
					$("[data-work='none']").addClass('active')
					this._rpc({model:'res.users',method:'write',args:[session.uid,{toggle_sidebar:'half'}]});
				}
				else if ('none' === work){
					$(".o_sidebar_menu").animate({'width':0+'px'})
					e.addClass('d-none')
					e.removeClass('active')
					$("[data-work='full']").removeClass('d-none')
					$("[data-work='full']").addClass('active')
					this._rpc({model:'res.users',method:'write',args:[session.uid,{toggle_sidebar:'none'}]});
				}
				else if ('full' === work){
					$(".o_sidebar_menu").animate().removeAttr('style');
					$('#sidebar').find('span').show()
					e.addClass('d-none')
					e.removeClass('active')
					$("[data-work='half']").removeClass('d-none')
					$("[data-work='half']").addClass('active')
					this._rpc({model:'res.users',method:'write',args:[session.uid,{toggle_sidebar:'full'}]});
				}
			}
		}

	})
});