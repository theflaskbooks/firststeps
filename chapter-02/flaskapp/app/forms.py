from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from wtforms import StringField
from wtforms.validators import DataRequired

class HelloWorldForm(DynamicForm):
    message = StringField(
            ("Repeat Message"),
            description = " Number of times the messsage needs to be repeated",
            widget = BS3TextFieldWidget()
        )
