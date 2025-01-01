from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Sample data representing a simple user database
users = {
    1: {'id': 1, 'name': 'Peter Parker'},
    2: {'id': 2, 'name': 'Batman'},
    3: {'id': 3, 'name': 'Superman'}
}

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users
    ---
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to retrieve
    responses:
      200:
        description: User found
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
      404:
        description: User not found
    """
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User  not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user
    ---
    parameters:
      - name: user
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      201:
        description: User created
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
      400:
        description: Bad request
    """
    new_user = request.json
    if 'name' not in new_user:
        return jsonify({'error': 'Name is required'}), 400

    user_id = max(users.keys()) + 1
    users[user_id] = {'id': user_id, 'name': new_user['name']}
    return jsonify(users[user_id]), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to update
      - name: user
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: User updated
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
      404:
        description: User not found
      400:
        description: Bad request
    """
    user = users.get(user_id)
    if user:
        updated_user = request.json
        if 'name' not in updated_user:
            return jsonify({'error': 'Name is required'}), 400
        users[user_id]['name'] = updated_user['name']
        return jsonify(users[user_id]), 200
    else:
        return jsonify({'error': 'User  not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to delete
    responses:
      204:
        description: User deleted
      404:
        description: User not found
    """
    if user_id in users:
        del users[user_id]
        return '', 204
    else:
        return jsonify({'error': 'User  not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)