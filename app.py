from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from


def main():
    """The main function for this script."""
    app.run(host='0.0.0.0', debug=True)

app = Flask(__name__)
app.config['SWAGGER'] = {
  "title": "Tasks API",
  "info": {
    "title": "Tasks API",
    "description": "Manage todo tasks",
    "contact": {
      "responsibleOrganization": "ME",
      "responsibleDeveloper": "Me",
      "email": "me@me.com",
      "url": "www.me.com",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.0.1"
  },
  "schemes": [
    "http",
    "https"
  ]
}

Swagger(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/todo')

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@swag_from('get_tasks.yml')
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks_byID', methods=['GET'])
@swag_from('get_tasks_byID.yml')
def get_tasks_byID():
    try:
        task_id  = int(request.args.get('task_id'))
        done = True if request.args.get('done',False) == 'true' else False
        
        task = [task for task in tasks if task['id'] == task_id and task['done'] == done]
        return jsonify({'task': task[0]})
    except Exception as e:
        return jsonify({'message': str(e), 'task' : []})

@app.route('/todo/api/v1.0/tasks_byID', methods=['POST'])
@swag_from('post_task.yml')
def post_task():
    try:
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': str(request.args.get('title')),
            'description': str(request.args.get('description',"")),
            'done': False
        }
        
        tasks.append(task)
        return jsonify({"status": "New task added", "task": tasks[-1]})
    except Exception as e:
        return jsonify({'message': str(e), 'task' : []})

if __name__== '__main__':
  main()
