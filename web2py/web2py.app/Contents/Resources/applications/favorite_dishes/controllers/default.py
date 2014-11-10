@auth.requires_login()
def index():
    dishes = db(db.dish.user == auth.user.id).select(orderby=~db.dish.last_made)
    return dict(dishes=dishes)

def new():
    # auth.user.id is the user id of the currently logged in user.
    # set the default of dish.user to that user id
    # so that the record entered into the db by form.process()
    # associates this user with the new recipe.
    db.dish.user.default = auth.user.id
    db.dish.last_made.default = request.now
    form = SQLFORM(db.dish)
    if form.process().accepted:
        response.flash = 'Your recipe has been added'
    return dict(form=form)

def show():
    dish = db.dish(request.args(0, cast=int)) or redirect(URL('index'))
    db(db.dish.id == dish.id).update(last_made=request.now)
    return dict(dish=dish)

def delete():
    dish = db.dish(request.args(0, cast=int)) or redirect(URL('index'))

    form=FORM(INPUT(_value='Yes, really', _type='submit', _name="bsubmit"),
              INPUT(_value='Silly me! No!', _type='submit', _name="bsubmit"))

    if request.vars.bsubmit == 'Yes, really':
       db(db.dish.id == dish.id).delete()
       redirect(URL('index'))
    elif request.vars.bsubmit == 'Silly me! No!':
       redirect(URL('index'))

    return dict(form=form, dish=dish)


def user():
    return dict(form=auth())
