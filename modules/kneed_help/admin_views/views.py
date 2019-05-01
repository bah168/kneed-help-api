import os
import uuid

from modules.extensions import BaseView
from werkzeug.utils import secure_filename
from flask_admin import form, expose
from flask import send_from_directory, current_app, abort, url_for
from werkzeug.exceptions import BadRequest
from jinja2 import Markup

from modules import app


class BodyPartsView(BaseView):
    allowed_extensions = ('jpeg', 'gif', 'png')
    column_labels = dict(image_name='Image')
    form_create_rules = ('name', 'image_name', 'subparts', 'active')
    form_edit_rules = ('name', 'image_name', 'subparts', 'active')
    column_searchable_list = ('name',)

    def _imagename_uuid1_gen(obj, file_data):
        _, ext = os.path.splitext(file_data.filename)
        uid = uuid.uuid1()
        return secure_filename('{}{}'.format(uid, ext))

    form_extra_fields = {
        'image_name': form.ImageUploadField(
            'Image',
            base_path=app.config['KNEED_HELP_IMAGES_DIR'],
            namegen=_imagename_uuid1_gen
        )
    }

    def _list_thumbnail(view, context, model, name):
        if not model.image_name:
            return ''
        return Markup(
            '<img height="57" width="57" src="%s">' % (
                url_for('.viewImage', image_name=model.image_name)
            ))

    column_formatters = {
        'image_name': _list_thumbnail
    }

    @expose('/viewImage/<string:image_name>')
    def viewImage(self, image_name):
        try:
            return send_from_directory(current_app.config['KNEED_HELP_IMAGES_DIR'], image_name)
        except BadRequest:
            return abort('Filename not found.')


class BodySubpartsView(BaseView):
    form_create_rules = ('name', 'coordinates', 'body_parts', 'conditions', 'active')
    column_searchable_list = ('name', )
    form_edit_rules = ('name', 'coordinates', 'body_parts', 'conditions', 'active')


class ConditionsView(BaseView):
    column_list = ('name', 'active', 'subparts', 'symptoms')
    form_create_rules = ('name', 'subparts', 'symptoms', 'active')
    form_edit_rules = ('name', 'subparts', 'symptoms', 'active')
    column_searchable_list = ('name', )
    column_labels = dict(subparts='Pain Location')

class SymptomsView(BaseView):
    form_create_rules = ('name', 'conditions', 'active')
    form_edit_rules = ('name', 'conditions', 'active')
    column_searchable_list = ('name', )

