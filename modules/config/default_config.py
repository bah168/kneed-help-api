import os

# Application Settings
SITE_NAME = os.getenv("SITE_NAME", "API")
BASE_DIR = os.path.abspath(
    os.path.dirname(os.getenv("FLASK_APP", "modules"))  # Find the root path

)
SECRET_KEY = os.getenv("SECRET_KEY", "secret")  # Uses env variable in prod
CSRF_ENABLED = os.getenv("CSRF_ENABLED", True)

# Development Settings
PRODUCTION_MODE = os.getenv("FLASK_ENV", "development") == 'production'
DEBUG = not PRODUCTION_MODE  # Toggle off during release
DEBUG_TOOLBAR_ENABLED = not PRODUCTION_MODE  # Gives information about routes

# Flask-Mail Settings
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'youremail@example.com')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'yourpassword')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '"noReply" <noreply@example.com>')
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL', True))

# SQLAlchemy Settings
DB_TYPE = os.getenv("DB_TYPE", "")
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', '')
DB_NAME = os.getenv('DB_NAME', '')
DB_PORT = os.getenv('DB_PORT', '')

SQLALCHEMY_DATABASE_URI = '{type}://{user}:{pwd}@{host}:{port}/{name}?charset=utf8mb4'.format(
    type=DB_TYPE, user=DB_USER, pwd=DB_PASSWORD, host=DB_HOST, name=DB_NAME, port=DB_PORT
) if DB_TYPE else 'sqlite:///' + os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    os.path.join(BASE_DIR, 'instance/development_app.db')
)

# Logging
USE_LOGGERS = os.getenv("USE_LOGGERS", False) or PRODUCTION_MODE
LOGS_DIR = os.getenv("LOGS_DIR", "instance/logs")

LDAP_SERVER = os.getenv('LDAP_SERVER', False)

