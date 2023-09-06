# Copyright (c) 2023, Abhishek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ConsolidatedInvoice(Document):
		@frappe.whitelist()
		def get_item(self):
			doc=frappe.db.get_list('Sales Invoice')
			for d in doc:
				doc1=frappe.get_doc('Sales Invoice',d.name)
				if(self.customer==doc1.customer):
					for d1 in doc1.get("items"):
						if(doc1.count==0):
							self.append("items",{
									"item_name":"{0}:{1}".format(d1.item_code,d1.item_name),
									"qty":d1.qty,
									"rate":d1.rate,
									"amount":d1.amount,
									"document_name":d.name,
									}
								)
							qt=0
							amt=0
							for d3 in self.get("items"):
									qt=qt+d3.qty
									amt=amt+d3.amount
							self.total_qty=qt
							self.total=amt						
		def before_save(self):
			count=1
			for d3 in self.get("items"):
				document_name=d3.document_name
				doc1=frappe.get_doc('Sales Invoice',document_name)
				if(self.customer==doc1.customer):
					frappe.db.set_value(
						"Sales Invoice", document_name,"count",count
					)
		def on_cancel(self):
			count=0
			for i in self.get("items"):
				doc = frappe.db.get_list("Sales Invoice")
				for d in doc:
					d1 = frappe.get_doc("Sales Invoice", d.name)
					if(i.document_name == d.name):
						frappe.db.set_value(
							"Sales Invoice", d.name,"count",count
						)
		def after_delete(self):
			count=0
			for i in self.get("items"):
				doc = frappe.db.get_list("Sales Invoice")
				for d in doc:
					d1 = frappe.get_doc("Sales Invoice", d.name)
					if(i.document_name == d.name):
						frappe.db.set_value(
							"Sales Invoice", d.name,"count",count
						)
		@frappe.whitelist()
		def Clcbutton(self):
			unicitem_dict = {}
			for row in self.items:
				if row.item_name in unicitem_dict:
					# If we've seen this name before, add the litre value to the existing total
					unicitem_dict[row.item_name] += int(row.qty)
				else:
					# If this is a new name, start a new total with the current litre value
					unicitem_dict[row.item_name] = int(row.qty)
				self.table_46 = []
			for item_name,qty in unicitem_dict.items():
				for i in self.items:
					if(i.item_name==item_name):
						rate=i.rate
						stock_uom=i.stock_uom
				row = self.append('table_46', {})
				row.item_name = item_name
				row.qty = qty
				row.rate=rate
				row.stock_uom=stock_uom
			for j in self.get('table_46'):
				j.amount=j.qty*j.rate
