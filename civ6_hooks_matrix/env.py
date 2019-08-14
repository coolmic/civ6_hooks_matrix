import sys as _sys
import os as _os
from dotenv import load_dotenv as _load_dotenv

_load_dotenv()

MATRIX_URL = _os.getenv('MATRIX_URL', 'https://matrix.org')
MATRIX_USER_ACCESS_TOKEN = _os.getenv('MATRIX_USER_ACCESS_TOKEN', '')
FLASK_HOST = _os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = _os.getenv('FLASK_PORT', 3000)

if not MATRIX_USER_ACCESS_TOKEN:
    print('Please define an env variable for MATRIX_USER_ACCESS_TOKEN')