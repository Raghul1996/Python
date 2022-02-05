from cProfile import run
from flask import Flask

app=Flask(__name__)
@app.route('/test/<name>/<age>')
def printnew(name,age):
    return 'Hello'+ '\t'+name+age

@app.route('/welcome')
def greet_method():
    return 'raghul'
app.run(debug="True")
