import os
import sqlite3
from functools import wraps
from flask import (
    Flask, render_template, request, redirect,
    url_for, flash, session, g
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'todo.db')


# ─── Database helpers ───────────────────────────────────────────────────────────

def get_db():
    """Open a new database connection if there is none yet for the current app context."""
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Close the database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    """Create users and todos tables if they don't already exist."""
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    db.commit()


# ─── Auth decorator ─────────────────────────────────────────────────────────────

def login_required(f):
    """Redirect to login page if the user is not authenticated."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ─── Auth routes ─────────────────────────────────────────────────────────────────

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('index'))

        flash('Invalid username or password.', 'error')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Username and password are required.', 'error')
            return render_template('register.html')

        db = get_db()
        existing = db.execute(
            'SELECT id FROM users WHERE username = ?', (username,)
        ).fetchone()

        if existing:
            flash('Username already exists.', 'error')
            return render_template('register.html')

        db.execute(
            'INSERT INTO users (username, password_hash) VALUES (?, ?)',
            (username, generate_password_hash(password))
        )
        db.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


# ─── Todo routes ─────────────────────────────────────────────────────────────────

@app.route('/')
@login_required
def index():
    db = get_db()
    todos = db.execute(
        'SELECT * FROM todos WHERE user_id = ? ORDER BY id DESC',
        (session['user_id'],)
    ).fetchall()
    return render_template('index.html', todos=todos, username=session['username'])


@app.route('/add', methods=['POST'])
@login_required
def add_task():
    task = request.form.get('task', '').strip()
    if task:
        db = get_db()
        db.execute(
            'INSERT INTO todos (user_id, task) VALUES (?, ?)',
            (session['user_id'], task)
        )
        db.commit()
    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>')
@login_required
def complete_task(todo_id):
    db = get_db()
    db.execute(
        'UPDATE todos SET completed = 1 WHERE id = ? AND user_id = ?',
        (todo_id, session['user_id'])
    )
    db.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
@login_required
def delete_task(todo_id):
    db = get_db()
    db.execute(
        'DELETE FROM todos WHERE id = ? AND user_id = ?',
        (todo_id, session['user_id'])
    )
    db.commit()
    return redirect(url_for('index'))


# ─── Startup ─────────────────────────────────────────────────────────────────────

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
