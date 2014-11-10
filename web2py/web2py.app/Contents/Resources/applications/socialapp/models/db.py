db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
from datetime import datetime

auth = Auth(db)
auth.define_tables(username=False, signature=True)
crud = Crud(db)

db.define_table('status',
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', db.auth_user, default=auth.user_id),
    format='%(created_by)s')

db.define_table('friends',
                Field('source', db.auth_user),
                Field('connection', 'reference auth_user'))

db.status.body.requires = IS_NOT_EMPTY()
db.status.created_by.readable = db.status.created_by.writable = False
db.status.created_on.readable = db.status.created_on.writable = False
