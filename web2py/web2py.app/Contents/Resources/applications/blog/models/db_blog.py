db.define_table('post',
   Field('title',length=256),
   Field('body','text',requires=IS_NOT_EMPTY()),
   Field('author',db.auth_user))

db.define_table('comm',
   Field('post',db.post,writable=False,readable=False),
   Field('author',db.auth_user,writable=False,readable=False),
   Field('body','text',requires=IS_NOT_EMPTY()))
