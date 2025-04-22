from flask import Flask
from config import Config
from models import db
from routes import task_routes

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the task manager routes
app.register_blueprint(task_routes)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
