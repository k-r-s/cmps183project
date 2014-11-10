# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    notes = db(db.note.user == auth.user.id).select(orderby=~db.note.last_made)
    return dict(notes=notes)

def new():
    db.note.user.default = auth.user.id
    db.note.last_made.default = request.now
    form = SQLFORM(db.note)
    if form.process().accepted:
        response.flash = 'Your note has been added'
    return dict(form=form)

def show():
    note = db.note(request.args(0, cast=int)) or redirect(URL('index'))
    db(db.note.id == note.id).update(last_made=request.now)
    return dict(note=note)

def delete():
    note = db.note(request.args(0, cast=int)) or redirect(URL('index'))

    form=FORM(INPUT(_value='Yes', _type='submit', _name="bsubmit"),
              INPUT(_value='No', _type='submit', _name="bsubmit"))

    if request.vars.bsubmit == 'Yes':
       db(db.note.id == note.id).delete()
       redirect(URL('index'))
    elif request.vars.bsubmit == 'No':
       redirect(URL('index'))

#    return dict(form=form, note=note)
    return dict(form=form, note=note)


def user():
    return dict(form=auth())
