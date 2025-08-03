# Flash is a lightweight Web Framework for Python. It used for developing web applicattion such as routing, request handling
from flask import Flask
# This refers to an instance of the Flask class
app = Flask(__name__) 
#@app.route('/') tells Flask: "When a user accesses the root URL (/) of this application eg: http://localhost:5000/ or https://www.example.com/ 
#execute the Python function immediately following this decorator and return its result as the response */
@app.route('/')
def home():
return "Hello from Azure DevOps pipeline World"
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80)
