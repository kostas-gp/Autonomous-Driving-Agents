import cv2
import numpy as np
import requests
import time

# Constants.
API_CALLS_PER_SEC = 3
BASE_ADDR = 'http://localhost:5000'
ENDPOINT = BASE_ADDR + '/api/'
FRAME_STACK_SIZE = 4
IMAGE_HEIGHT = 84
IMAGE_WIDTH = 84


def main():
    '''
    Extracts images from the camera, preprocesses them, stacks them and sends them to a web API
    server.
    '''
    video = cv2.VideoCapture(0)
    initial_time = None

    while video.isOpened():
        stack = []
        # Takes 'n' consecutive frames from the camera, preprocesses them and adds them to a list.
        # 'n' is given by FRAME_STACK_SIZE.
        for i in range(FRAME_STACK_SIZE):
            check, frame = video.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (IMAGE_HEIGHT, IMAGE_WIDTH), interpolation=cv2.INTER_AREA)
            img = (img.astype(np.float32) - 128) / 128
            img = np.expand_dims(img, axis=0)
            stack.append(img)
        
        # Stacks the images into a single numpy array.
        obs = np.concatenate(stack, axis=0)
        data = { 'obs': obs.tolist() }

        # Sets the initial time if this is the first iteration in this loop and calculates how much
        # time has elapsed (since the initial time).
        if initial_time is None:
            initial_time = time.time()
        elapsed_time = time.time() - initial_time

        # Sends request to web API and receive response back. Prints information about what has been
        # sent, what has been received and how much time has passed since the beginning.
        print(f'Sending observation with shape {obs.shape}.')
        response = requests.post(ENDPOINT, json=data)
        response_data = response.json()
        action = response_data['action']
        print(f'Received action {action}.')
        print(f'Time elapsed: {elapsed_time}')
        print()

        # Wait for a certain amount before making the next API call.
        time.sleep(1.0 / API_CALLS_PER_SEC)
    
    # Release resources.
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()