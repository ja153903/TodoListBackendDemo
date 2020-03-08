from flask_restful import Resource
from flask import request
import datetime
import time

from database.utils import get_session
from models.todo import Todo


class TodoController(Resource):
    def get(self):
        session = get_session()
        return {
            "data": [
                {
                    "id": row.id,
                    "title": row.title,
                    "description": row.description,
                    "created_at": str(row.created_at)
                }
                for row in session.query(Todo).all()
            ]
        }

    def post(self):
        data = request.get_json(force=True)
        title = data["title"]
        description = data["description"]

        created_at = datetime.date.fromtimestamp(time.time())

        try:
            session = get_session()

            to_add = Todo(title=title, description=description, created_at=created_at)
            session.add(to_add)
            session.commit()

            return {
                "message": "Successfully inserted a value"
            }, 200
        except:
            return {
                "message": "Failed to insert a value"
            }, 500


