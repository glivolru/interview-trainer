# Interview Trainer

Fullstack приложение для тренировки задач с собеседований.

## 🚀 Стек

* Backend: FastAPI (Python)
* Frontend: React (Vite)
* API: REST

---

## 📦 Установка и запуск

### 🔹 1. Клонировать репозиторий

```bash
git clone <your_repo_url>
cd interview-trainer
```

---

## 🟢 Backend (FastAPI)

### 1. Перейти в папку

```bash
cd backend
```

### 2. Создать виртуальное окружение

#### Windows:

```bash
py -m venv venv
venv\Scripts\Activate
```

#### macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Запустить сервер

```bash
python -m uvicorn main:app --reload
```

---

### Backend доступен по адресу:

```
http://127.0.0.1:8000
```

---

## 🔵 Frontend (React)

### 1. Перейти в папку

```bash
cd frontend
```

---

### 2. Установить зависимости

```bash
npm install
```

---

### 3. Запустить приложение

```bash
npm run dev
```

---

### Frontend доступен по адресу:

```
http://localhost:5173
```

---

## 🔗 Как это работает

* Frontend делает запросы к backend (`/tasks`)
* Backend возвращает JSON
* React отображает данные

---

## ⚠️ Важно

* Backend и frontend запускаются **в разных терминалах**
* Не забудь активировать `venv` перед запуском backend
* Не коммитить:

  * `venv/`
  * `node_modules/`

---

## 📌 TODO

* [ ] Страница задачи `/tasks/{id}`
* [ ] Отправка решения (`/submit`)
* [ ] Авторизация
* [ ] База данных
