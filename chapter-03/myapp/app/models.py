from flask import Markup, url_for
from flask_appbuilder.models.mixins import AuditMixin, FileColumn

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class TextToSpeech(Model):
    id = Column(Integer, primary_key=True)
    text = Column(String(150), nullable=False)
    audio_file = Column(FileColumn)

    def download(self):
        return Markup(
            '<a href="'
            + url_for("TextToSpeechModelView.download", filename=str(self.audio_file))
            + '">Download</a>'
        )

    def __repr__(self):
        return self.text[:25]

    def __str__(self):
        return self.text[:25]

