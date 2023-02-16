from flask import Flask
from flask import render_template
import requests
app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/45ab66b3b9c2c814e976")
data = response.json()

@app.route("/")
def home_page():
    return render_template("index.html", data=data)




@app.route("/about_me")
def about_me():
    return render_template("about.html")



@app.route("/contact")
def contact_me():
    return render_template("contact.html")



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

@app.errorhandler(404)
def page_not_found(e):
    # render your own HTML 404 error page
    return render_template("four-o-four.html"), 404

if __name__ == "__main__":
    app.run(debug=True)