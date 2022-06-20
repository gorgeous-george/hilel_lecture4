import os
from flask import Flask, render_template
from flaskr.db import get_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello/')
    def hello():
        return render_template('hello.html')

    @app.route('/names/')
    def names():
        db = get_db()
        artist_count = db.execute(
            'SELECT COUNT ( DISTINCT artist ) FROM tracks;'
        ).fetchone()[0]
        return render_template('artist_count.html', artist_count=artist_count)

    @app.route('/tracks/')
    def tracks():
        return render_template('tracks_count.html')

    @app.route('/tracks/', methods=['GET'])
    def tracks_genre():
        return render_template('that_genre_tracks_count.html')

    @app.route('/tracks-sec/')
    def tracks_sec():
        return render_template('all_tracks_titles_and_their_duration.html')

    @app.route('/tracks-sec/statistics/')
    def tracks_sec_stat():
        return render_template('average_duration_and_total_sum_of_duration.html')

    from . import db
    db.init_app(app)

    return app
