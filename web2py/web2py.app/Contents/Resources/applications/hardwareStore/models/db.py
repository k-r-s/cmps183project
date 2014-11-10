db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
from datetime import datetime

auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

db.define_table('supplier',
                Field('name'),
                Field('address', 'text'),
                format='%(name)s')

db.define_table('product',
                Field('name'),
                Field('quantityInStore', 'integer'),
                Field('price', 'double'),
                Field('supplier', 'reference supplier'),
                Field('quantityOnOrder', 'integer'),
                format='%(name)s')

db.define_table('contactPerson',
                Field('name'),
                Field('phone'),
                Field('email'),
                Field('employer', 'reference supplier'),
                Field('description', 'text'),
                format='%(name)s')

db.define_table('customer',
                Field('name'),
                Field('phone'),
                Field('email'),
                format='%(name)s')

db.define_table('purchase',
                Field('purchaser', 'reference customer'),
                Field('purchaseDate', 'datetime'),
                Field('total', 'double'),
                format='%(purchaser)s')

db.define_table('itemBought',
                Field('item', 'reference product'),
                Field('purchaseID', 'reference purchase'),
                Field('price', 'double'),
                Field('quantity', 'integer'),
                format='%(item)%s')
