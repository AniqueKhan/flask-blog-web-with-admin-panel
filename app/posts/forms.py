from wtforms import Form ,StringField,TextAreaField

class PostFrom(Form):
    title = StringField("Title")
    body = TextAreaField("Body")