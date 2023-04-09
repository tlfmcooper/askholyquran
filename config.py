import secrets
import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Flask-WTF configuration
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')
    WTF_CSRF_TIME_LIMIT = None
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    
    
    # Flask-Bootstrap configuration
    BOOTSTRAP_SERVE_LOCAL = True
