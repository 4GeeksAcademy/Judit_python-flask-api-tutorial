from flask import Flask
from flask import Flask,jsonify
app = Flask(__name__)

from flask import request

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.json
   print("incoming request with the following body", request_body)
   todos.append(request_body)
   
   return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)


todos = [{'label': 'My firts task', 'done': False}]

#@app.route('/todos', methods=['GET'])
#def hello_world():
    #return '<h1>Hello!</h1>'
#puedes convertir variable some_data en una cadena json con:
#json_text = jsonify(some_data)
# y luego devoverlo con:
#return json_text



# todos = [
   # { "label": "My first task", "done": False },
   # { "label": "My second task", "done": False }
#]


# some_data = { "name": "Bobby", "lastname": "Rixer" }

# Esta dis lineas siempre al final del archivo app.py


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)