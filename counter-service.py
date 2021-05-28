#!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
counter = 0
@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    if request.method == "POST":
        counter+=1
        return "Hmm, Plus 1 please "
    else:
        return str(f"Our counter is: {counter} ")
if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')

# Add line for saving the counter in file
# Mount the file
# Crate new persistence_storage yaml file for k8s: https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/
# Using global won't work for anything but very small/debug deployments. A production webserver will use multiple processes, each with their own global variables.
# We probably should use a Database or similar external data store to have one authorative location and value.
