db = DAL("sqlite://storage.sqlite")

db.define_table('supplier',
                Field('name', 'string'),                 # Supplier's name
                Field('address', 'string'),              # Supplier's address
                )

db.define_table('product',
                Field('quantityInStore', 'integer'),     # Quantity in-store of product
                Field('price', 'float'),                 # Price of product
                Field('quantityOnOrder', 'integer'),     # Quantity on order of product
                Field('supplier', 'reference supplier'), # Supplier of product
                )

db.define_table('contact',
                Field('name', 'string'),                 # Contact's name
                Field('phone', 'string'),                # Contact's phone
                Field('email', 'string'),                # Contact's email
                Field('note', 'string'),                 # Note on Contact
                )

db.define_table('contactPersons',
                Field('supplier', 'reference supplier'), # Supplier
                Field('contact', 'reference contact'),   # Supplier's contact
                )

db.define_table('purchase',
                Field('date', 'datetime'),               # Date of purchase
                Field('product', 'reference product'),   # Product purchased
                Field('pricePaid', 'float'),             # Price paid for product
                Field('quantity', 'integer'),            # Quantity of product purchased
                Field('total', 'float'),                 # Total paid for purchase
                )

db.define_table('customer',
                Field('name', 'string'),                 # Customer's name
                Field('phone', 'string'),                # Customer's phone
                Field('email', 'string'),                # Customer's email
                Field('purchases', 'reference purchase'),# Customer's purchases
                )