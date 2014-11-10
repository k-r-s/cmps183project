def index():
    return dict(posts=db().select(db.post.ALL))

def view_post():
    post = db.post[request.args(0)] or redirect(URL(r=request,f='index'))
    if auth.is_logged_in():
        db.comm.post.default = post.id
        db.comm.author.default = auth.user.id
        form = crud.create(db.comm)
    else:
        form = A("login to comment",_href=URL(r=request,f='user/login'))
    comms = db(db.comm.post==post.id).select(db.comm.ALL)
    return dict(post=post, form=form, comms=comms)
