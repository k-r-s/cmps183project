# -*- coding: utf-8 -*-

db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth

auth = Auth(db)
# instead of email (default) we'll use username for login
auth.define_tables(username=True)

db.define_table('note',
   Field('title'),
   Field('contents', 'text'),
   Field('user', db.auth_user),        # foreign key
   Field('last_made', 'datetime'),
   format = '%(title)s',
   redefine=True)

db.note.title.requires = IS_NOT_EMPTY()
db.note.contents.requires = IS_NOT_EMPTY()

# note.user not shown in any form (input or read only)
db.note.user.writable = db.note.user.readable = False
# last_made date cannot be modified by user
db.note.last_made.writable = False
