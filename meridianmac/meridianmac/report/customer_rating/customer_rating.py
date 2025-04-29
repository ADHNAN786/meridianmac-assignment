# Copyright (c) 2025, emeron infospace and contributors
# For license information, please see license.txt
import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data

def get_columns():
	return [
		{
			"fieldname": "customer",
			"label": _("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"width": 200
		},
		{
			"fieldname": "avg_rating",
			"label": _("Average Rating (Out of 5)"),
			"fieldtype": "Float",
			"width": 300
		},
	]

def get_data():
	return frappe.db.sql("""
		SELECT
			customer,
			ROUND(AVG(rating) * 5, 2) AS avg_rating
		FROM `tabCustomer Feedback`
		WHERE customer IS NOT NULL
		GROUP BY customer
		ORDER BY avg_rating DESC
	""", as_dict=True)
