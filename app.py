from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

app.secret_key = "secret123"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE username=? AND password=? AND role=?',
            (username, password, role)
        ).fetchone()
        conn.close()

        if user:
            session['username'] = username
            session['role'] = role

            if role == 'Admin':
                return redirect(url_for('admin_dashboard_redesigned'))
            elif role == 'Faculty':
                return redirect(url_for('faculty_dashboard'))
            else:
                return redirect(url_for('student_dashboard'))
        else:
            return render_template(
                'login.html',
                error="Invalid username, password, or role"
            )

    return render_template('login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

@app.route('/admin-dashboard-redesigned')
def admin_dashboard_redesigned():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    return render_template('admin_dashboard_redesigned.html')

@app.route('/faculty-dashboard')
def faculty_dashboard():
    if session.get('role') != 'Faculty':
        return redirect(url_for('login'))
    return render_template('faculty_dashboard.html')

@app.route('/student-dashboard')
def student_dashboard():
    student_username = "krishna"

    conn = get_db_connection()
    raw_records = conn.execute(
        'SELECT course_name, marks FROM marks WHERE student_username = ?',
        (student_username,)
    ).fetchall()

    records = []
    for row in raw_records:
        status = "Pass" if row["marks"] >= 40 else "Fail"
        records.append({
            "course_name": row["course_name"],
            "marks": row["marks"],
            "status": status
        })

    conn.close()

    if records:
        total_marks = sum(row["marks"] for row in records)
        average_marks = round(total_marks / len(records), 1)

        best_subject = max(
            records,
            key=lambda x: x["marks"]
        )["course_name"]
    else:
        average_marks = 0
        best_subject = "N/A"

    overall_result = "Pass"
    for r in records:
        if r["status"] == "Fail":
            overall_result = "Fail"
            break

    return render_template(
        'student_dashboard.html',
        student=student_username,
        records=records,
        average_marks=average_marks,
        best_subject=best_subject,
        overall_result=overall_result
    )

@app.route('/add-course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['course_name']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO courses (course_name) VALUES (?)',
            (course_name,)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('admin_dashboard_redesigned'))

    return render_template('add_course.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
            (username, password, role)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('admin_dashboard'))

    return render_template('add_user.html')

@app.route('/add-marks', methods=['GET', 'POST'])
def add_marks():
    if request.method == 'POST':
        student_username = request.form['student_username']
        course_name = request.form['course_name']
        marks = request.form['marks']

        conn = get_db_connection()

        existing = conn.execute(
            'SELECT * FROM marks WHERE student_username = ? AND course_name = ?',
            (student_username, course_name)
        ).fetchone()

        if existing:
            conn.close()
            return "Marks already exist for this student and course", 400

        conn.execute(
            'INSERT INTO marks (student_username, course_name, marks) VALUES (?, ?, ?)',
            (student_username, course_name, marks)
        )
        conn.commit()
        conn.close()

        if session.get('role') == 'Admin':
            return redirect(url_for('admin_dashboard_redesigned'))
        else:
            return redirect(url_for('faculty_dashboard'))

    role = session.get('role')
    return render_template(
        'add_marks_admin.html' if role == 'Admin' else 'add_marks_faculty.html'
    )

@app.route('/view-marks')
def view_marks():
    if 'role' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    records = conn.execute(
        'SELECT rowid AS id, student_username, course_name, marks FROM marks'
    ).fetchall()
    conn.close()

    return render_template(
        'view_marks.html',
        records=records,
        role=session['role']
    )

@app.route('/delete-marks', methods=['POST'])
def delete_marks():
    if session.get('role') != 'Admin':
        return "Unauthorized", 403

    record_id = request.form['id']

    conn = get_db_connection()
    conn.execute(
        'DELETE FROM marks WHERE rowid = ?',
        (record_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('view_marks'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/test')
def test():
    return "Flask is working"

if __name__ == '__main__':
    app.run(debug=True)
