# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Car Repair/Maintenance Management Odoo/OpenERP",
    "version" : "12.0.0.3",
    "depends" : ['base', 'sale', 'purchase', 'account', 'sale_stock', 'mail', 'product', 'stock', 'fleet','sale_management'],
    "author": "BrowseInfo",
    "summary": "Car Maintenance Repair management module helps to manage repair order, repair diagnosis, Diagnosis report,Workorder,Quote/Sales/Invoicing Whole workflow of Repair Industry",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps.
    This module use for autorepair industry , workshop management, Car Repair service industry, Spare parts industry. Fleet repair management. Vehicle Repair shop, Mechanic workshop, Mechanic repair software.Maintenance and Repair car. Car Maintenance Spare Part Supply. Car Servicing, Auto Servicing, Auto mobile Service, Bike Repair Service. Maintenance and Operation.Car Maintenance Repair management module helps to manage repair order, repair diagnosis, Diagnosis report, Diagnosis analysis, Quote for Repair, Invoice for Repair, Repair invoice, Repair orders, Workorder for repair, Fleet Maintenance.
    product repair, car workshop management, auto workshop management, repair workshop, workorder for product, 
This module use for following industry.
    -Laptop Repair, Computer servicing, Maintenance and Operation, Maintenance Repair, Service Industry. Computer Repair.Product Repair. car Maintenance, Repair and Maintenance. Product Repair management
      repair order
      repair workflow
      product repair management
      car repair management
      car repair order
      car repair Diagnosis
      car repair workorder
      car repair management with dynamic flow
      repair order for car
      car repair receipt
      Maintenance and repair management for car
      car Maintenance and repair 

      fleet repair order
      fleet repair workflow
      fleet repair management
      fleetrepair order
      fleet repair Diagnosis
      fleet repair workorder
      fleet repair management with dynamic flow
      repair order for fleet
      fleet repair receipt
      Maintenance and repair management for fleet
      fleet Maintenance and repair  
      car repair dynamic workflow
      fleet repair dynamic workflow
      vehicle repair
      workshop automobile
      automobile workshop
      automobile repair
       vehicle workshop




    """,
    'category': 'Industries',
    'price': '89',
    'currency': "EUR",
    "website" : "www.browseinfo.in",
    "data" :[
        'security/fleet_repair_security.xml',
        'security/ir.model.access.csv',
        'wizard/fleet_repair_assign_to_head_tech_view.xml',
        'wizard/fleet_diagnose_assign_to_technician_view.xml',
        'views/fleet_repair_view.xml',
        'views/fleet_repair_sequence.xml',
        'views/fleet_diagnose_view.xml',
        # 'views/fleet_diagnose_workflow.xml',
        # 'views/fleet_repair_workflow.xml',
        'views/fleet_workorder_sequence.xml',
        'views/fleet_workorder_view.xml',
        # 'views/fleet_workorder_workflow.xml',
        'views/custom_sale_view.xml',
        'report/fleet_repair_label_view.xml',
        'report/fleet_repair_label_menu.xml',
        'report/fleet_repair_receipt_view.xml',
        'report/fleet_repair_receipt_menu.xml',
        'report/fleet_diagnostic_request_report_view.xml',
        'report/fleet_diagnostic_request_report_menu.xml',
        'report/fleet_diagnostic_result_report_view.xml',
        'report/fleet_diagnostic_result_report_menu.xml',
        'report/fleet_workorder_report_view.xml',
        'report/fleet_workorder_report_menu.xml',
    ],
    'qweb':[
    ],
    "auto_install": False,
    "installable": True,
    'live_test_url':'https://www.youtube.com/watch?v=V6OCodztNA4&t=133s',
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
