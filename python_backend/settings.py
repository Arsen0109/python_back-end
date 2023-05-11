def setup(app):
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Backend labs, REST API for finance control"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "supermegasecretkey"