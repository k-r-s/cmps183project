db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
from datetime import datetime

auth = Auth(db)
auth.settings.extra_fields['auth_user']= [Field('profile_picture', 'upload'),Field('description', 'text'),Field('header_picture', 'upload')]
auth.define_tables(username=False, signature=True)
crud = Crud(db)

db.define_table('status',
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', db.auth_user, default=auth.user_id))

db.define_table('friend_connection',
                Field('user', 'reference auth_user'),
                Field('connection', 'reference auth_user'),
                Field('friends', 'boolean', default=False))

db.status.body.requires = IS_NOT_EMPTY()
db.status.created_by.readable = db.status.created_by.writable = False
db.status.created_on.readable = db.status.created_on.writable = False
