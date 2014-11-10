db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth

auth = Auth(db)
# instead of email (default) we'll use username for login
auth.define_tables(username=True)

db.define_table('dish',
   Field('title', unique=True),
   Field('recipe', 'text'),
   Field('user', db.auth_user),        # foreign key
   Field('last_made', 'datetime'),
   format = '%(title)s',
   redefine=True)

# dish titles must be unique; redundant with above
db.dish.title.requires = IS_NOT_IN_DB(db, db.dish.title)
db.dish.recipe.requires = IS_NOT_EMPTY()

# dish.user not shown in any form (input or read only)
db.dish.user.writable = db.dish.user.readable = False
# last_made date cannot be modified by user
db.dish.last_made.writable = False
