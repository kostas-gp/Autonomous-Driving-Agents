

import cv2
import numpy as np
from flask import Flask, request, jsonify

# Constants
HOST = '0.0.0.0'
PORT = 5000

# Initialize the Flask application
app = Flask(__name__)


def predict_action(obs):
    '''
    Predicts an action given an observation.

    :param obs: a numpy array with shape (4, 84, 84).
    
    :returns: an action in the form of a list with two values [a, s], where 'a' is the value of
    acceleration (if greater than 0) or brake (if less than 0), and 's' is the value of the
    steering.
    '''
    acceleration = np.random.uniform(-1.0, 1.0)
    steering = np.random.uniform(-1.0, 1.0)
    return [acceleration, steering]


@app.route('/api/', methods=['POST'])
def get_observation_send_action():
    '''
    Receives an observation within an HTTP request and sends an action within an HTTP response.
    '''
    # Extracts the observation from the request.
    obs = request.json['obs']
    obs = np.array(obs)

    # Predicts the action and sends it back. Prints information about what was received and what
    # was sent back as response.
    print(f'Received observation with shape {obs.shape}.')
    action = predict_action(obs)
    print(f'Sending back action {action}.')
    print()
    return jsonify(action=action)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)