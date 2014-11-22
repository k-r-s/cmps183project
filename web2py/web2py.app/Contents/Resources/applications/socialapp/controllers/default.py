import datetime

@auth.requires_login()
def index():
    friends_list = db(db.friend_connection.user==auth.user.id)(db.friend_connection.friends==True).select(db.friend_connection.connection)
    statuses = db((db.status.created_by==auth.user.id)|(db.status.created_by==db.friend_connection.connection)&(db.friend_connection.user==auth.user.id)&(db.friend_connection.friends==True)).select(db.status.id, db.status.created_by, db.status.created_on, db.status.body, orderby=~db.status.created_on, distinct=True)
    return locals()
    
@auth.requires_login()
def new():
    form = SQLFORM(db.status).process(next=URL('index'))
    return dict(form=form)

@auth.requires_login()
def edit():
     current_status = db.status(request.args(0,cast=int)) or redirect(URL('index'))
     form = SQLFORM(db.status, current_status).process(
         next = URL('show',args=request.args))
     return dict(form=form)

@auth.requires_login()
def show():
    status = db.status(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(status=status)

@auth.requires_login()
def delete():
    status = db.status(request.args(0, cast=int)) or redirect(URL('index'))

    form=FORM(INPUT(_value='Yes', _type='submit', _name="bsubmit"),
              INPUT(_value='No', _type='submit', _name="bsubmit"))

    if request.vars.bsubmit == 'Yes':
       db(db.status.id == status.id).delete()
       redirect(URL('index'))
    elif request.vars.bsubmit == 'No':
       redirect(URL('index'))

    return dict(form=form, status=status)

def download():
    return response.download(request, db)

def user():
    return dict(form=auth())
