# -*- coding: utf-8 -*-

db.define_table('category',
                Field('name', requires=(IS_SLUG(), \
                                        # no special symbols, possible URL
                                        IS_LOWER(),\
                                        # lower case
                                        IS_NOT_IN_DB(db, 'category.name'))))

db.define_table('post',
                Field('category', 'reference category', writable=False, readable=False),
                Field('title', 'string', requires=IS_NOT_EMPTY()),
                Field('url', requires=IS_EMPTY_OR(IS_URL())),
                Field('body', 'text', requires=IS_NOT_EMPTY()),
                Field('votes', 'integer', default=0, readable=False, writable=False),
                auth.signature) # created_on, created_by, 
                                # modified_on, modified by,
                                # is_active: check whether to show or not

db.define_table('vote',
                Field('post', 'reference post'),
                Field('score', 'integer', default=+1),
                auth.signature)

# comm = comment; comment is keyword db backend; don't use
db.define_table('comm', 
             Field('post', 'reference post'),
             Field('parent_comm', 'reference comm', default=None),
             Field('score', 'integer', default=+1),
             auth.signature)

POSTS_PER_PAGE = 10 # a constant

from gluon.contrib.populate import populate
"""
if db(db.auth_user).count()<2:
    populate(db.auth_user, 100)
    db.commit()
if db(db.post).count()<2:
    populate(db.post, 500)
    db.commit()
"""
if db(db.comm).count()<2:
    populate(db.comm, 1000)
    db.commit()