from flask import Flask, render_template

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue="Ricardo"
    myage=37
    
    mylist=[10,20,30,40,50]
    return render_template("index.html", myvalue=myvalue, myage=myage, mylist=mylist)

if __name__=='__main__':
    app.run(host='127.0.0.1', debug=True)