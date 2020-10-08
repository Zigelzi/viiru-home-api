from flask import make_response, jsonify, request
from api import app, db
import traceback


# Schemas for serialisation

# Status message descriptions
status_msg_fail = 'fail'
status_msg_success = 'success'

# Routes

# Create new user

# Login user

# Logout user

# Add new Housing Association
@app.route('/api/housing_association', methods=['POST'])
def add_housing_association():
    try:
        response_object = {'status': status_msg_success }
        request_data = request.get_json()
        response_object['test'] = 'Testing!'
        json_response = jsonify(response_object)
        return make_response(json_response, 200)
    except Exception as e:
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Failed'
        json_response = jsonify(response_object)
        return make_response(json_response, 500)
# Edit one housing association

# Get one housing association

# Add user to housing 

# Add repair to housing association

# Edit repair 