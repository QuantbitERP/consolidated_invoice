// Copyright (c) 2023, Pradip and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Consolidated Invoice', {
// 	// refresh: function(frm) {

// 	// }
// });
frappe.ui.form.on('Consolidated Invoice', {
	customer: function(frm) {
		frm.clear_table("items")
		frm.refresh_field('items')
			frm.call({
				method:'get_item',//function name defined in python
				doc:frm.doc, //current document
			 });
		 }
});

frappe.ui.form.on('Consolidated Invoice', {
	consoldated: function(frm) {
		frm.call({
			method:'Clcbutton',//function name defined in python
			doc:frm.doc, //current document
		 });
	 }
});

// frappe.ui.form.on('Consolidated Invoice', {
// 	before_save:function(frm){
// 		frm.call	({
// 			method:"clickbutton",
// 			doc:frm.doc,
// 			args:{
// 				doctype:"Consolidated Invoice",
// 				},
// 			callback: function(r) {
// 			}
// 		})
// 	}
// });
