from flask import Flask
from db.engine import create_tables, engine
from routes import user_blueprint

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # Не сортировать ключи JSON

# Регистрируем Blueprint 
app.register_blueprint(user_blueprint)

# Главная страница 
@app.route('/')
def index():
    return "<h1>Flask API для управления пользователями</h1><p>Доступные маршруты: <code>/users</code>, <code>/users/&lt;id&gt;</code></p>"

if __name__ == '__main__':
    # Создвем таблицы при запуске
    create_tables()
    app.run(debug=True)