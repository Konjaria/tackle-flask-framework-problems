# Import necessary libraries
from flask import Flask, render_template, request
import requests
import smtplib

# Initialize Flask app and get data from external API
app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/45ab66b3b9c2c814e976")
data = response.json()

# Define home page
@app.route("/")
def home_page():
    return render_template("index.html", data=data)

# Define about me page
@app.route("/about_me")
def about_me():
    return render_template("about.html")

# Define search by post ID page
@app.route("/post/<post_id>")
def search_id(post_id):
    necessary_post = None
    for post in data:
        if post["id"] == int(post_id):
            necessary_post = post
            break
    if necessary_post is None:
        return render_template("four-o-four.html", post_info=None)
    return render_template("post.html", post_info=necessary_post)

# Define custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    # render your own HTML 404 error page
    return render_template("four-o-four.html"), 404

# Define contact form page and handle form submission
@app.route("/contact", methods=["GET", "POST"])
def contact_form():
    if request.method == "POST":
        # Get user input from form
        username = request.form["username"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        message = request.form["message"]

        # Send email with user input
        my_email = "your_email_address" # replace with your email address
        password = "your_email_password" # replace with your email password
        text = f'Subject:Email from {username}\n\n' \
               f'phone_number: {phone_number}\n' \
               f'msg_body below\n{message}'.encode("utf-8")
        with smtplib.SMTP("your_smtp_provider", 587) as connection: # replace with your SMTP provider and port number
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=my_email,
                msg=text
            )

        # Display confirmation page after successful form submission
        return render_template("contact.html", msg_sent=True)
    
    # Display contact form page if request method is GET
    return render_template("contact.html", msg_sent=False)

# Run app if this file is executed as main program
if __name__ == "__main__":
    app.run(debug=True)
