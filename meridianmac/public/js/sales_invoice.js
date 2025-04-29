frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Generate Feedback Request'), function() {
                frappe.call({
                    method: "meridianmac.events.sales_invoice.create_feedback_request",
                    args: {
                        customer: frm.doc.customer
                    },
                    callback: function(r) {
                        if (!r.exc && r.message) {
                            frappe.msgprint(__('Customer Feedback created successfully.'));
                            frappe.set_route("Form", "Customer Feedback", r.message.name);
                        }
                    }
                });
            });
        }
    }
});
