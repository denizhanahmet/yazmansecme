from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import os

app = Flask(__name__)

TEACHERS_FILE = "teachers.txt"

def load_teachers():
    if not os.path.exists(TEACHERS_FILE):
        return []
    with open(TEACHERS_FILE, "r", encoding="utf-8") as f:
        teachers = [line.strip() for line in f if line.strip()]
    return sorted(teachers, key=lambda x: x.lower())

def save_teachers(teachers):
    teachers = sorted(teachers, key=lambda x: x.lower())
    with open(TEACHERS_FILE, "w", encoding="utf-8") as f:
        for t in teachers:
            f.write(t + "\n")

@app.route('/')
def index():
    teachers = load_teachers()
    return render_template('index.html', teachers=teachers)

@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    name = request.form['teacher_name'].strip()
    teachers = load_teachers()
    if name and name not in teachers:
        teachers.append(name)
        save_teachers(teachers)
    return redirect(url_for('index'))

@app.route('/remove_teacher', methods=['POST'])
def remove_teacher():
    name = request.form['teacher_name'].strip()
    teachers = load_teachers()
    if name in teachers:
        teachers.remove(name)
        save_teachers(teachers)
    return redirect(url_for('index'))

@app.route('/select_teachers', methods=['POST'])
def select_teachers():
    data = request.get_json()
    num = int(data['num_to_select'])
    teachers = data['selected_teachers']
    selected = random.sample(teachers, min(num, len(teachers)))
    return jsonify(selected_teachers=selected)

if __name__ == '__main__':
    app.run(debug=True)