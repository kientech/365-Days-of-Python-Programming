# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 10

# REST API with CRUD Operations using Flask
# pip install Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
tasks = [
    {"id": 1, "title": "Learn Python", "done": True},
    {"id": 2, "title": "Build a web app", "done": False}
]

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Get a single task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Title is required'}), 400
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    if not request.json:
        return jsonify({'error': 'Invalid request'}), 400
    
    task['title'] = request.json.get('title', task['title'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    # Use a different port to avoid conflict with Day 05
    app.run(debug=True, port=5001) 