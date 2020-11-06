from flask import render_template, flash, url_for, redirect
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, SimpleFormView

from . import appbuilder, db
from .models import TextToSpeech
from .forms import TextForm
from .tts_script import run_tts

import os
import uuid
import config


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


"""

class TextToSpeechModelView(ModelView):
    datamodel = SQLAInterface(TextToSpeech)

    label_columns = {"download": "Audio"}
    list_columns = ["text", "download"]
    show_columns = ["text", "download"]

class TextFormView(SimpleFormView):
    form = TextForm
    form_title="Text to Speech form"
    message = "Your text is submitted for speech coversion.. Please wait."
    errormessage = "There is some error encountered...Try again"

    def form_post(self, form):
        flash(self.message, "info")
        try:
            # Create details to be saved in database
            # A synchronous way to saving the details into the database
            ttsModel = TextToSpeech()
            ttsModel.text = form.text_field1.data
            outfile = str(uuid.uuid4()) + "_sep_" + form.text_field1.data[0:20] + ".mp3"
            ttsModel.audio_file = outfile

            tts_response = run_tts(form.text_field1.data, 'female')
            with open(os.path.join(config.UPLOAD_FOLDER, outfile), "wb") as audiof:
                audiof.write(tts_response.audio_content)

            db.session.add(ttsModel)
            db.session.commit()

            return redirect(url_for("TextToSpeechModelView.list"))
        except Exception as e:
            print(e)

        flash(self.errormessage, "info")


# Next, register your Views::


appbuilder.add_view_no_menu(
    TextToSpeechModelView
)

appbuilder.add_view(
        TextFormView,
        "Text Form",
        category="ToSpeech")


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
