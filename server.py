from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # Instantiate the Flask web app


@app.route('/')  # The root / the home page
def my_home():  # None is default value
    return render_template('./index.html')


@app.route('/<string:page_name>')  # Generic page navigation function
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Delimiter is the separator of info
        # QUOTE_MINIMAL means don't put quotes unless needed
        csv_writer.writerow([email, subject, message])  # Insert info as a list


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # Take form data and turn it into a python dictionary
            write_to_csv(data)  # Write the info to a csv file
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'


if __name__ == '__main__':
    app.run()
