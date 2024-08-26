# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate :
			self.rate = frappe.db.get_single_value("Rentals Settings","standard_rates")
		total_distance = 0
		for i in self.items:
			total_distance += i.distance
			
		self.amount = total_distance * self.rate
		

