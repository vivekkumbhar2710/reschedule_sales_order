# Copyright (c) 2023, Quantbit Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RescheduleSalesOrder(Document):
	@frappe.whitelist()
	def opcost(self):
		doc=frappe.db.get_list('Sales Order',filters={'name':self.sales_order_no})
		for d in doc:
			doc1=frappe.get_doc('Sales Order',d.name)
			if(self.sales_order_no==d.name):
				for d1 in doc1.get("items"):
					self.append("item",{
							"items":d1.item_code,
							"item_name":d1.item_name,
							"our_delivery_date":d1.our_delivery_date,
							"delivery_date":d1.delivery_date,
							}
						)
					
	@frappe.whitelist()
	def setval(self):
		doc = frappe.get_all("Sales Order Item",filters={'parent': self.sales_order_no},fields=["name", "parent", "our_delivery_date", "item_code"],
			ignore_permissions=True
		)

		for i in self.get("item"):
			for d in doc:
				if i.items == d.item_code:
					sql = f"""
						UPDATE `tabSales Order Item`
						SET `our_delivery_date` = '{i.our_delivery_date}'
						WHERE `name` = '{d.name}'
					"""
					frappe.db.sql(sql, as_dict=True)
