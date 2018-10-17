from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config["DEBUG"] = True

# users registration datastructure
users = [
    
]

'''
    View all users by admin
'''
class AllUsers(Resource):
    def get(self):
        return jsonify({'All users available': users})

class CreateUser(Resource):
    # creating a new user
    def post(self, userId):
        if next(filter(lambda x: x['userId'] == userId, users), None) is not None:
            return {'message': "A new user with user id '{}' already exists." .format(userId)}, 400

        data = request.get_json()
        user = {'userId': userId,
                 'fname': data['fname'],
                 'lname': data['lname'],
                 'email': data['email'],
                 'password': data['password']
                 }
        users.append(user)
        return user, 201



api.add_resource(AllUsers, '/')
api.add_resource(CreateUser, '/reg/<int:userId>')
app.run()
