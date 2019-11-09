import os
from src import create_app

app = create_app()


def run():
    debug = app.config['DEBUG']
    host = app.config['HOST_NAME']
    port = app.config['PORT']

    app.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    run()
