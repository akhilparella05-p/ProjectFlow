# ProjectFlow

> A modern Django-based project and task management application for organizing projects, managing tasks, and tracking work progress efficiently.

## 📌 Overview

ProjectFlow is a web-based project management system developed using Django. It provides a simple and user-friendly dashboard where users can create and manage projects, organize tasks, track task progress, assign tasks, and manage their account settings.

## ✨ Features

- 🔐 User Registration and Login
- 📊 Personalized Dashboard
- 📁 Create, Edit, and Delete Projects
- ✅ Create, Edit, and Delete Tasks
- 🔄 Task Status Tracking
  - To Do
  - In Progress
  - Completed
- 👤 Assign Tasks to Users
- 📅 Task Due Dates
- 📋 Project-wise Task Organization
- 👤 User Profile
- ⚙️ Account Settings
- 🌙 Dark Mode / Light Mode
- 📱 Responsive User Interface
- 🚪 Secure Logout

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| HTML5 | Page Structure |
| CSS3 | Styling and Responsive Design |
| JavaScript | Frontend Interactions |
| SQLite | Database |
| Git | Version Control |
| GitHub | Code Hosting |

## 📂 Project Structure

```text
ProjectFlow/
│
├── manage.py
│
├── projectmanager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   ├── static/
│   │   └── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── .gitignore
└── README.md
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/akhilparella05-p/ProjectFlow.git
cd ProjectFlow
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Django

```bash
pip install django
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 💻 Usage

1. Register a new account.
2. Log in to ProjectFlow.
3. Create a new project.
4. Add tasks to your projects.
5. Assign tasks and set due dates.
6. Update task status as work progresses.
7. Monitor project and task statistics from the dashboard.
8. Manage your profile and account settings.
9. Switch between Dark Mode and Light Mode.

## 🔮 Future Enhancements

- Task notifications and reminders
- Advanced search and filtering
- Team collaboration
- Email notifications
- Detailed analytics and reports
- Cloud database integration
- User roles and permissions

## 👨‍💻 Author

**Akhil P.**

GitHub: https://github.com/akhilparella05-p/ProjectFlow

---

⭐ If you find this project useful, consider giving it a star!