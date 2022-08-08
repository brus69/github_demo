import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///asa.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

db.drop_all()
db.create_all()

user_john = User(id=1, name="John", age=30)
user_kate = User(id=2, name="Kate", age=31)

users = [user_john, user_kate]
db.session.add_all(users)

db.session.commit()


@app.route("/user/first")
def get_first_user():
    user = User.query.first()

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })

@app.route("/users/count")
def get_users_count():
    user_count = User.query.count()

    return json.dumps(user_count)

@app.route("/users")
def get_users():
    user_list = User.query.all()

    user_response = []

    for user in user_list:
        user_response.append(
            {
                "id": user.id,
                "name": user.name,
                "age": user.age,
            }
        )
    return json.dumps(user_response)

@app.route("/users/<int:sid>")
def get_user(sid: int):
    user = User.query.get(sid)

    if user is None:
        return "user not found"

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })

if __name__ == '__main__':
     app.run(debug=True)