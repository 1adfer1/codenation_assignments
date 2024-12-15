from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)

@my_view.route("/", methods=["GET"])
def home():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)

@my_view.route("/add", methods=["POST"])
def add():
    task = request.form.get("task", "").strip()
    if not task:
        flash("Task cannot be empty.")
        return redirect(url_for("my_view.home"))
    if Todo.query.filter_by(task=task).first():
        flash("Task already exists.")
        return redirect(url_for("my_view.home"))
    try:
        new_todo = Todo(task=task, complete=False)
        db.session.add(new_todo)
        db.session.commit()
    except Exception as e:
        flash(f"An error occurred: {e}")
        db.session.rollback()
    return redirect(url_for("my_view.home"))

@my_view.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    try:
        db.session.commit()
    except Exception as e:
        flash(f"An Error occured: {e}")
        db.session.rollback()  # Rollback in case of error
    return redirect(url_for("my_view.home"))

@my_view.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo =Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/edit/<int:todo_id>", methods=["POST"])
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    new_task_name = request.form["new_task"]
    todo.task = new_task_name
    db.session.commit()
    return redirect(url_for("my_view.home")) 