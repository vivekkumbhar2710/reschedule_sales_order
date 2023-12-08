// Copyright (c) 2023, Quantbit Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Reschedule Sales Order', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Reschedule Sales Order', {
	sales_order_no: function(frm) {
		frm.clear_table("item")
		frm.refresh_field('item')
		frm.call({
				method:'opcost',//function name defined in python
				doc: frm.doc, //current document
			});

	}
});

frappe.ui.form.on('Reschedule Sales Order', {
	after_save: function(frm) {
		frm.call({
				method:'setval',//function name defined in python
				doc: frm.doc, //current document
			});

	}
});

