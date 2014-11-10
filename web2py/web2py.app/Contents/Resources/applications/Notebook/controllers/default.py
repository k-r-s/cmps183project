import datetime

@auth.requires_login()
def index():
     notes = db(db.note.created_by ==auth.user.id).select(db.note.id,db.note.title,orderby=~db.note.last_viewed)
     return dict(notes=notes)

@auth.requires_login()
def add():
    form = SQLFORM(db.note).process(next=URL('index'))
    return dict(form=form)

@auth.requires_login()
def read():
    note = db.note(request.args(0, cast=int)) or redirect(URL('index'))
    db(db.note.id == note.id).update(last_viewed=request.now)
    return dict(note=note)

@auth.requires_login()
def delete():
    note = db.note(request.args(0, cast=int)) or redirect(URL('index'))

    form=FORM(INPUT(_value='Yes', _type='submit', _name="bsubmit"),
              INPUT(_value='No', _type='submit', _name="bsubmit"))

    if request.vars.bsubmit == 'Yes':
       db(db.note.id == note.id).delete()
       redirect(URL('index'))
    elif request.vars.bsubmit == 'No':
       redirect(URL('index'))

    return dict(form=form, note=note)

def user():
     return dict(form=auth())
