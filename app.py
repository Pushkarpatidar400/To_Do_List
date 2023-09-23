from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
tasks = []

class TaskMemento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

class TaskOriginator:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def save_to_memento(self):
        return TaskMemento(self.state)

    def restore_from_memento(self, memento):
        self.state = memento.get_state()


class TaskCareTaker:
    def __init__(self):
        self.mementos = []
        self.current_index = -1  # Track the current state index

    def get_memento(self, index):
        return self.mementos[index]

    def add_memento(self, memento):
        # When a new memento is added, remove all redo actions
        if self.current_index < len(self.mementos) - 1:
            self.mementos = self.mementos[:self.current_index + 1]
        self.mementos.append(memento)
        self.current_index += 1  # Increment the current state index

    def undo(self):
        if 0 <= self.current_index:
            self.current_index -= 1  # Move to the previous state
            return self.mementos[self.current_index]

    def redo(self):
        if self.current_index < len(self.mementos) - 1:
            self.current_index += 1  # Move to the next state
            return self.mementos[self.current_index]

caretaker = TaskCareTaker()
class TaskBuilder:
    def __init__(self):
        self.name = None
        self.description = None
        self.due_date = None
        self.tags = []

    def set_name(self, name):
        self.name = name
        return self

    def set_description(self, description):
        self.description = description
        return self

    def set_due_date(self, due_date):
        self.due_date = due_date
        return self

    def add_tag(self, tag):
        self.tags.append(tag)
        return self

    def build(self):
        return Task(self.name, self.description, self.due_date, self.tags)

class Task:
    def __init__(self, name, description, due_date=None, tags=None):
        self.id = len(tasks)
        self.name = name
        self.description = description
        self.due_date = due_date
        self.tags = tags or []
        self.completed = False
        self.originator = TaskOriginator(self)

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False

    def save_state(self):
        return self.originator.save_to_memento()

    def restore_state(self, memento):
        self.originator.restore_from_memento(memento)

    def __str__(self):
        return f"{self.name} - {self.description} - Due: {self.due_date} - Tags: {', '.join(self.tags)}"


@app.route('/')
def index():
    return render_template('index.html')

# ... existing code ...
caretaker = TaskCareTaker()

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    print(task_id)
    if 0 <= task_id < len(tasks):
        task = tasks[task_id]

        if not task.completed:
            task.complete()

        memento = task.save_state()
        caretaker.add_memento(memento)
        return redirect(url_for('view_tasks', filter='not_completed' if task.completed else 'completed'))
    else:
        return "Task not found", 404


@app.route('/undo/<int:index>')
def undo_task(index):
    if 0 <= index < len(caretaker.mementos):
        memento = caretaker.get_memento(index)
        task = tasks[index]

        if task.completed:
            task.uncomplete()

        task.restore_state(memento)
    return redirect(url_for('view_tasks'))


@app.route('/redo/<int:index>')
def redo_task(index):
    if 0 <= index < len(caretaker.mementos):
        memento = caretaker.get_memento(index)
        task = tasks[index]

        if not task.completed:
            task.complete()

        task.restore_state(memento)
    return redirect(url_for('view_tasks'))


@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    task_description = request.form.get('description')
    due_date = request.form.get('due_date')
    tasks.append(Task(task_name, task_description, due_date))
    return redirect(url_for('index'))


@app.route('/tasks')
def view_tasks():
    filter_param = request.args.get('filter')

    if filter_param == 'completed':
        filtered_tasks = [task for task in tasks if task.completed]
    else:
        filtered_tasks = [task for task in tasks if not task.completed]

    return render_template('tasks.html', tasks=filtered_tasks)


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    del tasks[task_id]
    return redirect(url_for('view_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
