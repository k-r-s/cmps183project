db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

db.define_table('supplier',
    Field('name'),
    Field('address', 'string'),
    Field('contact', 'string'),
    format='%(name)s')

db.define_table('product',
    Field('quantity_in_store', 'integer'),
    Field('price', 'float'),
    Field('quantity_on_order', 'integer'),
    Field('supplier_id', db.supplier),
    )

db.define_table('contact',
    Field('supplier_id', db.supplier),
    Field('name'),
    Field('phone', 'string'),
    Field('email', 'string'),
    Field('note', 'text'),
    format='%(name)s')

db.define_table('customer',
    Field('name'),
    Field('phone', 'string'),
    Field('email', 'string'),
    Field('purchase', 'string'),
    format='%(name)s')

db.define_table('purchase',
    Field('most_recent', 'datetime', default=request.now),
    Field('product_id', db.product),
    Field('customer_id', db.customer),
    Field('price', 'float'),
    Field('total', 'float'),
    )