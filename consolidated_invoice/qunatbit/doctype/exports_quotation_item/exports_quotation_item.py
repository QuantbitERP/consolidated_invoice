# Copyright (c) 2023, Pradip and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExportsQuotationItem(Document):
	@frappe.whitelist()
	def ratecal(self):
		frappe.msgprint("ffhhhddd")
		self.rate = self.item_rate * self.export_duty_single_item
