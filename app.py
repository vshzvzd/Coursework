from flask import Flask
from config import Config
from models import db
from routes import main_bp

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db.init_app(app)

# Регистрация blueprint с маршрутами
app.register_blueprint(main_bp)

# Главная страница
@app.route('/')
def index():
    return "Сервер работает! Добро пожаловать в систему учёта инвентаря."

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)



    