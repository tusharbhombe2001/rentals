import frappe

def get_emoji():
    return "U+1F600"

def throw_emoji(doc,event):
    frappe.throw("😀") 
