from flask import Flask

from blueprints.general import app as general_bp
from flask import Flask

from blueprints.general import app as general_bp
from blueprints.admin import app as admin
from blueprints.user import app as user

import config
import fileex



app = Flask(__name__)

app.register_blueprint(general_bp)
app.register_blueprint(user)
app.register_blueprint(admin)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

fileex.db.init_app(app)

with app.app_context():
    fileex.db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
