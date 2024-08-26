// Copyright (c) 2024, tushar and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by make"] = {
	"filters": [
		{ "fieldname" : "my_filter",
			"label" : "Filter By Vehical",
			"fieldtype" : "Link",
			"options" : "Vehical"


		}


	]
};
