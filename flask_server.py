from flask import Flask  
app = Flask(__name__) #creating the Flask class object   
@app.route('/hello/',methods=['GET']) #decorator drfines the   
def home():  
    return "hello, this is our first flask website"; 
@app.route('/postvalue/',methods=['POST'])
def getValue():
    print()
    return 'ok'
if __name__ =='__main__':  
    app.run(debug = True,host='0.0.0.0',threaded=True) 