from flask import Flask, render_template
from config import Config
from db.engine import create_tables
from routes import user_blueprint

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    create_tables()
    app.run(debug=app.config['DEBUG'])