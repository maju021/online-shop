from flask import Flask
from blueprints.general import app as general_bp
from blueprints.admin import app as admin
from blueprints.user import app as user
app = Flask(__name__)

app.register_blueprint(general_bp)
app.register_blueprint(user)
app.register_blueprint(admin)
if __name__ == "__main__":
    app.run(debug=True)
