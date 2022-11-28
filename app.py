from flask import Flask


app= Flask(__name__)


@app.route('/v1/sai',methods=['GET'])
def home():
    return "Hello world"


  

app.run(port=5000)    