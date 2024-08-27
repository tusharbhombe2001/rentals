# Copyright (c) 2024, tushar and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_fullname(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Tushar"
		test_driver.last_name = "Bhombe"
		test_driver.licenses = "tybuuu"
		#test_driver.phone_number = "1234567890"
		test_driver.save()


		self.assertEqual(test_driver.full_name, "Tushar Bhombe")
