# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

	columns = [{"fieldname" : "total_fairs","label":"Total Fairs", "fieldtype":"Data"},
				{"fieldname" : "make","label":"Make", "fieldtype":"Data"},
			   {"fieldname" : "revenu_by_car","label":"Total Revenue", "fieldtype":"Currency","options":"AED"},]
	#print(columns)
	
	data = frappe.get_all("Ride Booking", fields=["SUM(amount) AS revenu_by_car","count(make) AS total_fairs","vehical.make"],filters={"docstatus":1},group_by="make")

	chart = {
		"data" : {
			"labels" : [x.make for x in data],
			"datasets" : [{"values": [x.revenu_by_car for x in data]}],
		},
		"type":"donut"
	}

	return columns, data , "Pie Chart", chart
