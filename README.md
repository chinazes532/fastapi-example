  <h1>📚 Books And Authors API — FastAPI + SQLAlchemy + SQLite</h1>

  <p>RESTful API для управления данными авторов и их книг. Реализовано с использованием асинхронного стека FastAPI и SQLAlchemy 2.0 с поддержкой типизации и модульной архитектурой.</p>

  <h2>🚀 Описание проекта</h2>
  <p>Проект предоставляет API-эндпоинты для:</p>
  <ul>
    <li>Создания автора (<code>POST /authors</code>)</li>
    <li>Получения списка авторов (<code>GET /authors</code>)</li>
    <li>Получения автора по ID (<code>GET /authors/{id}</code>)</li>
    <li>Создания книги (<code>POST /books</code>)</li>
    <li>Получения списка книг (<code>GET /books</code>)</li>
    <li>Получения книги по ID (<code>GET /books/{id}</code>)</li>
    <li>Получения книг по ID автора (<code>GET /books/author/{author_id}</code>)</li>
  </ul>
  <p>Асинхронный подход обеспечивает высокую производительность, а тестирование через <code>pytest</code> и <code>httpx</code> гарантирует корректную работу ручек.</p>

  <h2>⚙️ Стек технологий</h2>
  <table border="1" cellspacing="0" cellpadding="6">
    <thead>
      <tr>
        <th>Компонент</th>
        <th>Назначение</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>FastAPI</td><td>Разработка API</td></tr>
      <tr><td>SQLAlchemy 2.0</td><td>Асинхронная ORM</td></tr>
      <tr><td>SQLite + aiosqlite</td><td>Лёгкая БД для разработки</td></tr>
      <tr><td>Pydantic v2</td><td>Валидация и сериализация</td></tr>
      <tr><td>Uvicorn</td><td>ASGI сервер</td></tr>
      <tr><td>pytest + httpx</td><td>Тестирование эндпоинтов</td></tr>
      <tr><td>environs</td><td>Управление конфигурацией через переменные окружения</td></tr>
    </tbody>
  </table>

  <h2>📦 Установка</h2>
  <pre><code>git clone https://github.com/chinazes_532/fastapi_example.git
cd fastapi-authors-api
python -m venv .venv
source .venv/bin/activate  # для Windows: .venv\Scripts\activate
pip install -r requirements.txt
</code></pre>

  <h2>▶️ Запуск сервера</h2>
  <pre><code>uvicorn src.main:app --reload</code></pre>

  <h2>📂 Структура проекта</h2>
  <pre><code>.
├── src/
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   ├── handlers/
│   │   └── author_repository.py
│   │   └── book_repository.py
│   ├── routers/
│   │   └── authors.py
│   │   └── books.py
│   ├── schemas/
│   │   └── authors.py
│   │   └── books.py
│   ├── config.py
│   └── main.py
├── tests/
│   └── test_authors.py
│   └── test_books.py
└── requirements.txt
</code></pre>

  <h2>🧪 Покрытие тестами</h2>
  <ul>
    <li>✅ Тест получения всех авторов (<code>GET /authors</code>)</li>
    <li>✅ Тест создания нового автора (<code>POST /authors</code>)</li>
    <li>✅ Тест получения автора по ID (<code>GET /authors/{id}</code>)</li>
    <li>✅ Тест получения всех книг (<code>GET /booka</code>)</li>
    <li>✅ Тест создания новой книги (<code>POST /books</code>)</li>
    <li>✅ Тест получения книги по ID (<code>GET /books/{id}</code>)</li>
    <li>✅ Тест получения книг по ID автора (<code>GET /books/author/{author_id}</code>)</li>
    <li>✅ Проверка структуры данных и типов</li>
    <li>✅ Проверка статус-кодов: <code>200</code>, <code>404</code>, <code>422</code></li>
  </ul>

  <h2>🧾 requirements.txt</h2>
  <details>
    <summary>Развернуть</summary>
    <pre><code>aiosqlite==0.21.0
annotated-types==0.7.0
anyio==4.9.0
certifi==2025.7.9
click==8.2.1
environs==14.2.0
fastapi==0.115.12
greenlet==3.2.3
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
iniconfig==2.1.0
marshmallow==4.0.0
packaging==25.0
pluggy==1.6.0
pydantic==2.11.5
pydantic_core==2.33.2
Pygments==2.19.2
pytest==8.4.1
pytest-asyncio==1.0.0
python-dotenv==1.1.0
sniffio==1.3.1
SQLAlchemy==2.0.41
starlette==0.46.2
typing-inspection==0.4.1
typing_extensions==4.14.0
uvicorn==0.34.3</code></pre>
  </details>

<h2>🧑‍💻 Автор</h2>
<p>Разработано с ❤️ на FastAPI<br>
Telegram: <a href="https://t.me/psych0ce00">@psych0ce00</a></p>
