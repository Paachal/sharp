# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app instance
app = Flask(__name__)
app.template_folder = 'templates'

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the registration route
@app.route('/register', methods=['POST'])
def register():
    # Process the form data (save to database, etc.)
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    ssn = request.form.get('ssn')

    # You can save the data to a database or perform any other necessary actions here

    # Redirect to a page displaying user details
    return redirect(url_for('user_details', 
                            first_name=first_name, 
                            last_name=last_name, 
                            email=email, 
                            phone=phone, 
                            address=address, 
                            ssn=ssn))

# Define the user details route
@app.route('/user_details')
def user_details():
    # Retrieve user details from URL parameters
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    address = request.args.get('address')
    ssn = request.args.get('ssn')

    return render_template('user_details.html', 
                           first_name=first_name, 
                           last_name=last_name, 
                           email=email, 
                           phone=phone, 
                           address=address, 
                           ssn=ssn)

# Define the deposit route
@app.route('/deposit')
def deposit():
    # Add logic for handling deposit action here
    return "Deposit Page - Add logic here"

# Define the withdraw route
@app.route('/withdraw')
def withdraw():
    # Add logic for handling withdraw action here
    return "Withdraw Page - Add logic here"

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
