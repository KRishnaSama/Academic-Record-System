# Academic Record System

A comprehensive web-based academic record management system built with Flask that enables admins, faculty, and students to manage courses, marks, and academic performance.

## Overview

The Academic Record System is a role-based web application designed to streamline the management of academic records in educational institutions. It provides separate dashboards and functionalities for three user types: Administrators, Faculty Members, and Students.

## Features

### 🔐 Authentication & Authorization
- Role-based access control (Admin, Faculty, Student)
- Secure login system with session management
- User credential validation against SQLite database

### 👨‍💼 Admin Dashboard
- Complete user management (add, edit, delete)
- Course management and administration
- Mark management oversight
- Access to both classic and redesigned dashboard interfaces

### 👨‍🏫 Faculty Dashboard
- View assigned courses
- Add and manage student marks
- Monitor academic records

### 👨‍🎓 Student Dashboard
- View enrolled courses and marks
- Track academic performance metrics:
  - Total marks across courses
  - Average marks calculation
  - Pass/Fail status per course
  - Best subject identification
- Overall result summary

### 📊 Grade Calculation
- Automated grade calculation based on marks
- Grade Scale:
  - A: 75+
  - B: 60-74
  - C: 45-59
  - D: 33-44
  - F: Below 33

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Additional**: Java module for grade calculation

## Project Structure

```
Academic Record System/
├── app.py                          # Main Flask application
├── init_db.py                      # Database initialization script
├── database.db                     # SQLite database file
├── java_module/
│   └── GradeCalculator.java       # Grade calculation logic
├── static/
│   ├── css/
│   │   └── style.css              # Application styling
│   ├── js/
│   │   └── faaaa.js               # JavaScript functionality
│   ├── images/                    # Image assets
│   └── videos/                    # Video assets
├── templates/
│   ├── index.html                 # Homepage
│   ├── login.html                 # Login page
│   ├── admin_dashboard.html       # Admin dashboard (classic)
│   ├── admin_dashboard_redesigned.html # Admin dashboard (updated)
│   ├── admin_sidebar.html         # Admin sidebar component
│   ├── faculty_dashboard.html     # Faculty dashboard
│   ├── student_dashboard.html     # Student dashboard
│   ├── add_user.html              # Add user form
│   ├── add_course.html            # Add course form
│   ├── add_marks.html             # Add marks form
│   ├── add_marks_admin.html       # Admin marks entry
│   ├── add_marks_faculty.html     # Faculty marks entry
│   └── view_marks.html            # View marks page
└── README.md                      # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Java (optional, for GradeCalculator module)
- pip (Python package manager)

### Steps

1. **Clone or extract the project**
   ```bash
   cd "Academic Record System"
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Flask**
   ```bash
   pip install flask
   ```

4. **Initialize the database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your web browser and navigate to: `http://localhost:5000`

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
```

### Courses Table
```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
)
```

### Marks Table
```sql
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_username TEXT NOT NULL,
    course_name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
```

## Usage

### Admin Login
1. Go to login page
2. Enter admin credentials
3. Select "Admin" from role dropdown
4. Access full administrative features

### Faculty Login
1. Go to login page
2. Enter faculty credentials
3. Select "Faculty" from role dropdown
4. Add and manage student marks

### Student Login
1. Go to login page
2. Enter student credentials
3. Select "Student" from role dropdown
4. View your marks and academic performance

## Key Functionalities

### User Management
- Add new users with specific roles
- Manage user credentials
- View user information

### Course Management
- Create and manage courses
- Assign courses to students
- Track course enrollment

### Mark Management
- Faculty can add student marks
- Admin can oversee mark entries
- Automatic pass/fail determination
- Grade calculation based on marks

### Academic Performance Tracking
- Calculate average performance
- Identify best performing subjects
- Generate comprehensive academic reports

## Java Grade Calculator

The `java_module/GradeCalculator.java` provides grade calculation functionality:

**Running the Grade Calculator:**
```bash
cd java_module
javac GradeCalculator.java
java GradeCalculator
```

**Input:** Student marks (0-100)
**Output:** Corresponding grade (A-F)

## Configuration

### Secret Key
Update the Flask secret key in `app.py` for production use:
```python
app.secret_key = "your-secret-key-here"
```

### Database Location
The SQLite database is created as `database.db` in the project root. To change the location, modify the connection string in `app.py`:
```python
conn = sqlite3.connect('path/to/database.db')
```

## Security Considerations

⚠️ **Important:** This is a development system. For production deployment:
- Use hashed passwords instead of plain text
- Implement proper session management
- Add CSRF protection
- Use environment variables for sensitive configurations
- Implement proper input validation and sanitization
- Use HTTPS for all communications

## Default Test User

After database initialization, you can add test users manually through the application or by modifying `init_db.py` to include default credentials.

## Troubleshooting

### Database Issues
- If you encounter database errors, delete `database.db` and run `python init_db.py` again
- Ensure you have write permissions in the project directory

### Port Already in Use
- If port 5000 is already in use, modify the app.run() parameters in `app.py`:
  ```python
  app.run(host='localhost', port=5001, debug=True)
  ```

### Template Not Found
- Ensure all files in the `templates/` folder are present
- Check that the `static/` folder structure is intact

## Future Enhancements

- [ ] Password hashing and encryption
- [ ] Email notifications for mark updates
- [ ] Advanced reporting and analytics
- [ ] Mobile app integration
- [ ] API for third-party integrations
- [ ] Attendance tracking
- [ ] GPA calculation
- [ ] Exam scheduling

## License

Developed By Tera Baap 😋

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Verify all files are in the correct locations

---

**Last Updated:** February 2026

**Version:** 1.0.0
