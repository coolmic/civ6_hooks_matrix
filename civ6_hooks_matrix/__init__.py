import sys
from flask import Flask
from . import env
from .services.init_flask_loggers import init_flask_loggers
from .services.mapping import parse_mapping_file
from .routes.civ import civ_pages


def usage():
    print('Usage: '+sys.argv[0]+' <rooms-file>')


def _real_main(file):
    parse_mapping_file(file)

    app = Flask(__name__)
    init_flask_loggers(app)

    # add routes to flask
    app.register_blueprint(civ_pages)

    # run the server
    app.run(debug=False, host=env.FLASK_HOST, port=env.FLASK_PORT)


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(2)

    try:
        _real_main(sys.argv[1])
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')


__all__ = ['main']
