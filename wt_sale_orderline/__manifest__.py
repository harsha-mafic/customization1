# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    "name": "wt_sale_orderline",
    "version": "13.0.0.1",
    "category": "Sales",
    "summary": "list the pending orderline",
    "description": """
    list the pending orderline
    """,
    "author": "Warlock Technologies Pvt Ltd.",
    "website": "http://warlocktechnologies.com",
    "support": "info@warlocktechnologies.com",
    "depends": ["sale_management"],
    "data": ['views/sale_orderline_view.xml'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "OPL-1",
}