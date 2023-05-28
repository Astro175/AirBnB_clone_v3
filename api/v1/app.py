#!/usr/bin/python3
"""module that creates a flask skeleton
   for blueprints
"""

from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def close():
    storage.close()

if __name__ == '__main__':
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
