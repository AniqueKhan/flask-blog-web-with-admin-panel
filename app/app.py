from flask import Flask,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore,Security,current_user

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = "secret_key"

db= SQLAlchemy(app)

from models import *

migrate =  Migrate(app,db)
manager = Manager(app)

manager.add_command("db",MigrateCommand)


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role("admin")
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for("security.login",next=request.url))

class AdminView(AdminMixin,ModelView):
    pass

class HomeAdminView(AdminMixin,AdminIndexView):
    pass

class BaseModelView(ModelView):
    def on_model_change(self,form,model,is_created):
        if is_created:
            model.generate_slug()
        return super().on_model_change(form,model,is_created)

class PostAdminView(AdminMixin,BaseModelView):
    pass
class TagAdminView(AdminMixin,BaseModelView):
    pass

admin = Admin(app,"FlaskApp",url="/",index_view=HomeAdminView(name="Home"))
admin.add_view(PostAdminView(Post,db.session))
admin.add_view(TagAdminView(Tag,db.session))

# Flask Security
user_datastore = SQLAlchemyUserDatastore(db,User,Role)
security = Security(app,user_datastore)
