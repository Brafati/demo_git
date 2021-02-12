from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

if __name__ == '__hello__':
  app.run()
