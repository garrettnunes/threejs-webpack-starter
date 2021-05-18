import datetime

from flask import Flask, render_template, request

# app = Flask(__name__)

app = Flask(__name__, static_url_path='',
            static_folder='dist', template_folder='dist')
# app.config['STATIC_FOLDER'] = '/dist'

# app.config["APPLICATION_ROOT"] = "/dist"

# app.config.from_object('config')

# # config file has STATIC_FOLDER='/core/static'
# app.static_url_path = app.config.get('STATIC_FOLDER')

# # set the absolute path to the static folder
# app.static_folder = app.root_path + app.static_url_path

# print(app.static_url_path)
# print('here')
# print(app.static_folder)


# app.config.from_object('config')

# config file has STATIC_FOLDER='/core/static'
# app.static_url_path=app.config.get('STATIC_FOLDER')

# set the absolute path to the static folder
# app.static_folder=app.root_path + 'test'
#
# print(app.static_url_path)
# print(app.static_folder)

@app.before_request
def before_request():
    url = request.url
    protocol = request.headers.get('X-Forwarded-Proto')
    if protocol == 'http' or url.startswith('http://www.'):
        url = url.replace('http://', 'https://', 1).replace('www.', '', 1)
        return redirect(url, code=301)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    # dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
    #                datetime.datetime(2018, 1, 2, 10, 30, 0),
    #                datetime.datetime(2018, 1, 3, 11, 0, 0),
    #                ]

    # return render_template('index_construction.html')
    return render_template('index.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run()
    # app.run(host='127.0.0.1', port=8080, debug=True)
