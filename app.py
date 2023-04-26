from flask import Flask as fl

app = fl(__name__)

@app.route("/")
def hello_world():
  return "hare krishna !"
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)