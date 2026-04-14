"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os

from flask import jsonify, render_template, send_from_directory, url_for
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
from app import app
from app.forms import MovieForm
from app.models import Movie, db


###
# Routing for your application.
###


@app.route("/")
def index():
    return jsonify(message="This is the beginning of our API")


@app.route("/api/v1/csrf-token", methods=["GET"])
def get_csrf_token():
    return jsonify({"csrf_token": generate_csrf()})


###
# The functions below should be applicable to all Flask apps.
###


def form_errors(form):
    """Collect form errors from Flask-WTF."""
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = "Error in the {field} field - {error}".format(
                field=getattr(form, field).label.text,
                error=error,
            )
            error_messages.append(message)

    return error_messages


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send static text files from the Flask static directory."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)

@app.route("/api/v1/movies", methods=["GET"])
def get_movies():
    movies = Movie.query.all()

    movie_list = []

    for movie in movies:
        movie_list.append({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "poster": url_for("get_poster", filename=movie.poster)
        })

    return jsonify({
        "movies": movie_list
    })
    
@app.route("/api/v1/posters/<filename>")
def get_poster(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/api/v1/movies", methods=["POST"])
def movies():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster_file = form.poster.data

        filename = secure_filename(poster_file.filename)
        upload_folder = app.config["UPLOAD_FOLDER"]
        os.makedirs(upload_folder, exist_ok=True)

        poster_path = os.path.join(upload_folder, filename)
        poster_file.save(poster_path)

        new_movie = Movie(
            title=title,
            description=description,
            poster=filename,
        )

        db.session.add(new_movie)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "Movie successfully added",
                    "title": title,
                    "poster": filename,
                    "description": description,
                }
            ),
            201,
        )

    return jsonify({"errors": form_errors(form)}), 400

@app.after_request
def add_header(response):
    """
    Add headers to force the latest rendering engine and disable caching.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Render a custom 404 page."""
    return render_template("404.html"), 404
