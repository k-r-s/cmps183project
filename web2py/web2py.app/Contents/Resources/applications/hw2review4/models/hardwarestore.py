# -*- coding: utf-8 -*-

db.define_table(
    'supplier',
    Field('name', 'string', notnull=True),
    Field('address', 'string', notnull=True),
    format='%(name)s'#references to rows in this table are selected by name
    )

db.define_table(
    'contact_person',
    Field('name', 'string', notnull=True),
    Field('phone', 'string'),
    Field('email', 'string'),
    Field('supplier', 'reference supplier'),
    Field('description', 'string', notnull=True),
    format='%(name)s'#references to rows in this table are selected by name
    )

#validates for proper formating of phone numbers and emails
db.contact_person.phone.requires = IS_MATCH('^1?((-)\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$', error_message='invalid phone number')
db.contact_person.email.requires = IS_EMAIL()

db.define_table(
    'product',
    Field('name', 'string'),
    Field('quantity_in_store', 'integer', notnull=True),
    Field('price', 'float', notnull=True),
    Field('quantity_on_order', 'integer', notnull=True),
    Field('supplier', 'reference supplier'),
    format='%(name)s'#references to rows in this table are selected by name
    )

db.define_table(
    'customer',
    Field('name', 'string', notnull=True),
    Field('phone', 'string', required=False),
    Field('email', 'string'),
    format='%(email)s'#references to rows in this table are selected by email
    )

#validates for proper formating of phone numbers and emails
db.customer.phone.requires = IS_MATCH('^1?((-)\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$', error_message='invalid phone number')
db.customer.email.requires = IS_EMAIL()

db.define_table(
    'purchase',
    Field('customer', 'reference customer'),
    Field('purchase_date', 'date'),
    Field('products', 'list:reference product'),
    Field('costs', 'list:string'),#no such thing as list:float, so prices must be stored as strings
    Field('quantity', 'list:integer'),
    Field('total', 'float')#this will be updated in a controller
    )
