// Copyright (c) 2024, tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {

	},
	rate(frm){
		frm.trigger("update_total_amount");

	},

	update_total_amount(frm){
		let t_distance = 0
		for (let item of frm.doc.items){
			t_distance += item.distance ;
		}
		

		const amount = frm.doc.rate * t_distance 
	
		frm.set_value("amount",amount);

	}
});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {

	},
	distance(frm,cdt,cdn) {
		//console.log(cdt,cdn)
		//console.log("distance changed")
		frm.trigger("update_total_amount");
	},
	items_remove(frm){
		frm.trigger("update_total_amount");

	}
})
