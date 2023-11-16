from flask import Flask

app=Flask(__name__)

@app.route('/')
def call() :
    return "raushan Kumar"

if __name__=='__main__':
  app.run(debug=True)    