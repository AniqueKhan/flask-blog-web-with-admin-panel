from flask import Blueprint,render_template,request,flash,redirect,url_for
from models import *
from .forms import PostFrom
from app import db
from flask_security import login_required

posts = Blueprint("posts",__name__,template_folder="templates")


@posts.route("/create" ,methods=['POST','GET'])
@login_required
def post_create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        try:
            post = Post(title=title,body=body)
            db.session.add(post)
            db.session.commit()
        except:
            flash("Invalid Input",category="error")

        flash("Post Created Successfully",category="success")
        return redirect(url_for("posts.post_detail",slug=post.slug))
    form = PostFrom()

    return render_template("posts/post_create.html",form=form)


#localhost:5000/blog/
@posts.route("/")
def posts_list():
    query = request.args.get("query")
    if query:
        posts = Post.query.filter(Post.title.contains(query) | Post.body.contains(query))
    else:    
        posts = Post.query.order_by(Post.created.desc())

    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    
    pages = posts.paginate(page=page,per_page=3)
    return render_template("posts/posts.html",posts=posts,query=query,pages=pages)


@posts.route("/<slug>")
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    return render_template("posts/post_detail.html",post=post)

@posts.route('/tags/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first_or_404()
    return render_template("posts/tag_detail.html",tag=tag)

@posts.route('/<slug>/edit',methods=['GET','POST'])
@login_required
def post_update(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    if request.method == "POST":
        form = PostFrom(formdata=request.form,obj=post)
        form.populate_obj(post)
        db.session.commit()
        flash("Post Updated Successfully",category="success")
        return redirect(url_for("posts.post_detail",slug=post.slug))
    form = PostFrom(obj=post)
    return render_template("posts/edit.html",post=post,form=form)

@posts.route("/<slug>/delete")
def post_delete(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    db.session.delete(post)
    db.session.commit()
    flash("Post Deleted Successfully",category="success")
    return redirect('/blog')
