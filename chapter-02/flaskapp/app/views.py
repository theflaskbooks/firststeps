from flask import render_template, request, redirect, url_for, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, SimpleFormView

from . import appbuilder, db
from .forms import HelloWorldForm

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View","
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

class HelloFormView(SimpleFormView):
    form = HelloWorldForm
    form_title = "HeLLoWorLd View form"

    def form_get(self, form):
        form.message.data = "0"

    def form_post(self, form):
        nums = form.message.data
        if nums:
            return redirect(url_for("HelloView.world", num=nums))


class HelloView(BaseView):

    route_base = "/hello"
    default_view = "world"

    @expose("/world")
    @expose("/world/<int:num>")
    def world(self, num=''):
        message =  "<b>Hello, World! {}</b> from Flask"
        if num and num >= 1:
            messages = [ message.format(m+1) for m in range(num)]
        else:
            messages = [ message.format(num) ]

        return render_template(
            "hello.html", messages=messages, 
            base_template=appbuilder.base_template, appbuilder=appbuilder
        )


# Add views to to the Application Menu
appbuilder.add_view(
        HelloView,
        "World",
        category="HelloWorld",
        )

appbuilder.add_link("Method1", href="/hello/world/1", category="HelloWorld")
appbuilder.add_link("Method2", href="/hello/world/2", category="HelloWorld")

appbuilder.add_view(
        HelloFormView,
        "Hello World Form",
        category="Hello Forms"
        )


"""
appbuilder.add_view_no_menu(HelloView())
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    # import pdb;pdb.set_trace()
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
            ),
        404,
    )


db.create_all()
