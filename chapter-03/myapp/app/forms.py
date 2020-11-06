from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from wtforms import StringField
from wtforms.validators import DataRequired


class TextForm(DynamicForm):
    text_field1 = StringField(
            ("Text to Convert"),
            description="Enter the text to convert to Speech",
            validators=[DataRequired()],
            widget=BS3TextFieldWidget(),
    )
