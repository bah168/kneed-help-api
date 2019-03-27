# modules/models.py
import logging
from flask import abort, redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin
from sqlalchemy.event import listens_for

Base = declarative_base(name="Model")


logger = logging.getLogger("app")


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True

    @classmethod
    def find(cls, p_key):
        if p_key:
            return cls.query.filter(cls.id == int(p_key)).first()
        else:
            return None


class BaseView(ModelView):
    can_delete = False
    can_create = False
    can_edit = False

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        else:
            self.can_create = True
            self.can_edit = True
            self.can_delete = False
            return True


    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
        else:
            logger.warning(
                "User: [ {username} ] accessed [ {resource} ] resource.".format(
                    username=current_user.username, resource=self.name
                )
            )

    def search_placeholder(self):
        return 'Search'


@listens_for(BaseModel, "after_insert", propagate=True)
def after_insert_listener(mapper, connection, target):
    warn_msg = "Inserted Record: {}".format(target)
    logger.warning(warn_msg)


@listens_for(BaseModel, "after_update", propagate=True)
def after_update_listener(mapper, connection, target):
    warn_msg = "Updated Record: {}".format(target)
    logger.warning(warn_msg)


@listens_for(BaseModel, "after_delete", propagate=True)
def after_delete_listener(mapper, connection, target):
    warn_msg = "Deleted Record: {}".format(target)
    logger.warning(warn_msg)


def get_class_by_tablename(tablename):
    """
    Return class reference mapped to table.
    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in BaseModel._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c
