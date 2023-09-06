// Copyright (c) 2023, Pradip and contributors
// For license information, please see license.txt

{% include 'erpnext/selling/sales_common.js' %}

frappe.ui.form.on('Exports Quotation', {

});

erpnext.selling.QuotationController = class QuotationController extends erpnext.selling.SellingController {
};
cur_frm.script_manager.make(erpnext.selling.QuotationController);


frappe.ui.form.on('Exports Quotation Item', {
	item_rate:function(frm) {
		frm.call({
			method:'ratecal',
			doc: frm.doc,
		});
	}
})
frappe.ui.form.on('Exports Quotation Item', {
	export_duty_single_item:function(frm) {
		frm.call({
			method:'ratecal',
			doc: frm.doc,
		});
	}
})



