# -*- coding: utf-8 -*-

from flectra import api, fields, models
from flectra.exceptions import  ValidationError

class StoreData(models.Model):
    _name = "store.data"

    @api.onchange("keeper_id")
    def onchange_store_data(self):
        print("---------------keppers store/ name, ID /----------------", self.name, self.keeper_id)
        self.prod_category = self.keeper_id.prod_category

    _sql_constraints = [('name_uniq', 'unique(prod_code)', 'prod_code must be unique')]


    @api.constrains("store_rent")
    def check_store_rent(self):
        if self.store_rent < 500 or self.store_rent > 5000:
            raise ValidationError("rent must be in between 500 to 5000!!!")

    name = fields.Char(string="Store Name", required="True",)
    store_rent = fields.Integer("Store Rent")
    store_addres = fields.Text(string="Addrres")
    prod_name = fields.Char(string="Product Name", size=50,)
    prod_code = fields.Char(string="Prod Code", size=3,)
    prod_pkg_date = fields.Date(string="Packaging Date",)
    prod_ex_date = fields.Date(string="Expiry Date",)
    is_prod_ex = fields.Boolean( string="ISI Certification", default="True,")
    prod_category = fields.Selection([ ('CL','Cloths'),
                                       ('MB','Mobile Phones'),
                                       ('FT', 'Footwares'),
                                       ('LP', 'laptops'), ], string="Categorys", )
    prod_img = fields.Binary(string="Product Imaage")
    keeper_id = fields.Many2one("store.keeper", ondelete="cascade", required=True, string="Store Keeper")
    amenity_ids = fields.Many2many("store.amenity", "store_amenity_rel",
                                   "store_id", "amenity_id", string="Amenity")




class StoreKeeper(models.Model):
    _name = "store.keeper"


    @api.multi
    @api.depends('store_line')
    def _calculate_store_keeper(self):
        for keepers in self:
            print("----totle_shops-----",len(keepers.store_line))
            self.totle_stores=len(keepers.store_line)

    name = fields.Char(string="Store Keeper Name", required="True", size=30,)
    prod_category = fields.Selection([('CL', 'Cloths'),
                                      ('MB', 'Mobile Phones'),
                                      ('FT', 'Footwares'),
                                      ('LP', 'laptops'), ], string="prod Categorys", default="CL", )


    designation = fields.Selection([('OWN','Owner'),
                                    ('EMP','Employ'),
                                    ('PNT','Patnar'),
                                    ('OTH','Other'),],
                                   )
    store_line = fields.One2many("store.data", "keeper_id", string="Stores", readonly="True")

    totle_stores = fields.Integer(string="totle no of stors that keepers have", compute=_calculate_store_keeper,
                                  store=True)



class StoreAmenity(models.Model):
    _name = "store.amenity"

    name = fields.Char(string="Amenity Name", required="True",)
    quantity = fields.Boolean(string="Tottle Amenity", default="True")

    store_ids = fields.Many2many("store.data","store_amenity_rel",
                                 "amenity_id", "store_id", string="Stores")

    totle_stores = fields.Integer(string="totle no of stors that keepers have")

    @api.multi
    def count_stores(self):
        print("_____Totle  Stores_________",len(self.store_ids))
        self.totle_stores = len(self.store_ids)