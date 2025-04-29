import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def create_feedback_request(customer):
	if not customer:
		frappe.throw("Customer is required")

	doc = frappe.get_doc({
		"doctype": "Customer Feedback",
		"customer": customer,
		"date": nowdate(),
		"status": "Draft"
	})
	doc.insert()
	return {"name": doc.name}
