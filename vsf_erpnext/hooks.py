# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "vsf_erpnext"
app_title = "Vsf Erpnext"
app_publisher = "vijay_wm@yahoo.com"
app_description = "vue storefront api for erpnext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vijay_wm@yahoo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vsf_erpnext/css/vsf_erpnext.css"
# app_include_js = "/assets/vsf_erpnext/js/vsf_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/vsf_erpnext/css/vsf_erpnext.css"
# web_include_js = "/assets/vsf_erpnext/js/vsf_erpnext.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vsf_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vsf_erpnext.install.before_install"
# after_install = "vsf_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vsf_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Item": {
        "on_update": "vsf_erpnext.sync.on_update_item"
    }
    # "*": {
    # 	"on_update": "method",
    # 	"on_cancel": "method",
    # 	"on_trash": "method"
    # }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vsf_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"vsf_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"vsf_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vsf_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vsf_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vsf_erpnext.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vsf_erpnext.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vsf_erpnext.task.get_dashboard_data"
# }
