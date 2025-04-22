from flask import Blueprint, jsonify, request
from services import create_task, list_tasks, get_task, delete_task

task_routes = Blueprint('task_routes', __name__)

# List all tasks
@task_routes.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = list_tasks()
    return jsonify([{
        'id': task.id,
        'name': task.name,
        'status': task.status,
        'created_at': task.created_at
    } for task in tasks])

# Create a new task
@task_routes.route('/tasks', methods=['POST'])
def create_new_task():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Task name is required'}), 400

    task = create_task(name)
    return jsonify({
        'id': task.id,
        'name': task.name,
        'status': task.status,
        'created_at': task.created_at
    }), 201

# Get details of a specific task
@task_routes.route('/tasks/<task_id>', methods=['GET'])
def get_single_task(task_id):
    task = get_task(task_id)
    if task:
        return jsonify({
            'id': task.id,
            'name': task.name,
            'status': task.status,
            'created_at': task.created_at
        })
    return jsonify({'error': 'Task not found'}), 404

# Delete a task
@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
def delete_single_task(task_id):
    task = delete_task(task_id)
    if task:
        return jsonify({'message': f'Task {task_id} deleted'}), 200
    return jsonify({'error': 'Task not found'}), 404
