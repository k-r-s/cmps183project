db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
from datetime import datetime

auth = Auth(db)
auth.define_tables(username=True)
crud = Crud(db)

db.define_table('note',
    Field('title'),
    Field('body', 'text'),
    Field('last_viewed', 'datetime'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')


db.note.title.requires = IS_NOT_IN_DB(db, 'note.title')
db.note.body.requires = IS_NOT_EMPTY()
db.note.created_by.readable = db.note.created_by.writable = False
db.note.created_on.readable = db.note.created_on.writable = False
db.note.last_viewed.readable = db.note.last_viewed.writable =False