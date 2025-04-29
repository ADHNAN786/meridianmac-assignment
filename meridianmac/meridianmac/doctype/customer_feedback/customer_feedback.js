// Copyright (c) 2025, Adhnan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer Feedback", {
	rating: function (frm) {
        if (!frm.doc.rating) return;

        let rating = frm.doc.rating;
        let indicator = "";

        if (rating >= 0.2 && rating <= 0.4) {
            indicator = "🔴";
        } else if (rating >= 0.8 && rating <= 1) {
            indicator = "🟢";
        } else {
            indicator = "🟡";
        }
        frm.set_value("rating_indicator", indicator);
    },

});
