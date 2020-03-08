from flask import Flask
from flask_restful import Api

from controllers.todo_controller.todo import TodoController


app = Flask(__name__)
api = Api(app)

api.add_resource(TodoController, "/api/todo")

if __name__ == "__main__":
    app.run(debug=True)
