# -*- coding: utf-8 -*-

from flectra import api, fields, models


class StoreData(models.Model):
    _name = "store.data"

    name = fields.Char(string="Store Name", required="True",)
    store_addres = fields.Text(string="Addrres")
    prod_name = fields.Char(string="Product Name", size=50,)
    prod_code = fields.Char(string="Prod Code", size=3,)
    prod_pkg_date = fields.Date(string="Packaging Date",)
    prod_ex_date = fields.Date(string="Expiry Date",)
    is_prod_ex = fields.Boolean( string="ISI Certification", default="True,")
    prod_category = fields.Selection([ ('CL','Cloths'),
                                       ('MB','Mobile Phones'),
                                       ('FT', 'Footwares'),
                                       ('LP', 'laptops'), ], string="Categorys", default="CL",)

    prod_img = fields.Binary(string="Product Imaage")

    keeper_id = fields.Many2one("store.keeper", ondelete="cascade", required=True, string="Store Keeper")

    amenity_ids = fields.Many2many("store.amenity", "store_amenity_rel",
                                   "store_id", "amenity_id", string="Amenity")

    total_store = fields.Integer(string="total availbele stores")


class StoreKeeper(models.Model):
    _name = "store.keeper"

    name = fields.Char(string="Store Keeper Name", required="True", size=30,)
    designation = fields.Selection([('OWN','Owner'),
                                    ('EMP','Employ'),
                                    ('PNT','Patnar'),
                                    ('OTH','Other'),],
                                   )
    store_line = fields.One2many("store.data", "keeper_id", string="Stores")

class StoreAmenity(models.Model):
    _name = "store.amenity"

    name = fields.Char(string="Amenity Name", required="True",)
    quantity = fields.Boolean(string="Tottle Amenity", default="True")

    store_ids = fields.Many2many("store.data","store_amenity_rel",
                                 "amenity_id", "store_id", string="Stores")