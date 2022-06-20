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
        ).fetchone()
        return render_template('artist_count.html', artist_count=artist_count)

    @app.route('/tracks/')
    def tracks():
        db = get_db()
        tracks_count = db.execute(
            'SELECT COUNT ( id ) FROM tracks;'
        ).fetchone()
        return render_template('tracks_count.html', tracks_count=tracks_count)

    @app.route('/tracks/<string:genre>')
    def tracks_genre(genre):
        db = get_db()
        that_genre_count = db.execute(
            'SELECT COUNT(id) FROM tracks WHERE genre = ?',
            (genre,)
        ).fetchone()
        return render_template('that_genre_tracks_count.html', that_genre_count=that_genre_count)

    @app.route('/tracks-sec/')
    def tracks_sec():
        db = get_db()
        tracks_titles_duration = db.execute(
            'SELECT title, duration FROM tracks;'
        ).fetchall()
        return render_template('all_tracks_titles_and_their_duration.html', tracks_titles_duration=tracks_titles_duration)

    @app.route('/tracks-sec/statistics/')
    def tracks_sec_stat():
        db = get_db()
        average_sum = db.execute(
            'SELECT AVG(duration), SUM(duration) FROM tracks;'
        ).fetchall()
        return render_template('average_duration_and_total_sum_of_duration.html', average_sum=average_sum)

    from . import db
    db.init_app(app)

    return app
