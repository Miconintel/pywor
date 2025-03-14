from flask import Flask, render_template,request,redirect
import csv

# this is the name of the module/package that is calling this script
app = Flask(__name__)
print(__name__ )

# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template("index.html",name=username)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<page_name>')
def about(page_name):
    return render_template(page_name)


def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    
    with open('database.txt', mode="a") as database:

        data_text = email + subject + message + "\n"

        database.write(data_text)


def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    with open('database.csv', mode="a", newline='\n') as database2:
        # data_text = email + subject + message + "\n"
        csv_write =  csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return "something went wrong"


