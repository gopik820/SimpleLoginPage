from flask import Flask, request, render_template,redirect,url_for
import csv
from csv import writer
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       name = request.form.get("username")
       email = request.form.get("email")
       number = request.form.get("number")
       header = ['Name', 'Email', 'Number']
       data = [name, email, number]
       with open('data.csv', 'a',newline='') as f:
            writer_object = writer(f)
            writer_object.writerow(data)
            f.close()
       return redirect('/login')
    return render_template("signup.html")

@app.route('/login',methods =["GET", "POST"])
def home():
    if request.method == "POST":
       username = request.form.get("username")
       email = request.form.get("email")
       number = request.form.get("number")
       flag=0
       with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == username:
                    if row[1] == email:
                            if row[2] == number:
                                flag=1                        
            if flag:
                return redirect('/success')
            else:
                return redirect('/error')
    return render_template('login.html')

@app.route('/error',methods =["GET", "POST"])
def error(): 
    return render_template('error.html')

@app.route('/success',methods =["GET", "POST"])
def success(): 
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
