from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
data = requests.get(url="https://api.npoint.io/83923fc3eb2956e1b139")
data = data.json()


@app.route('/')
def home():
    list_of_objects = [Post(blog_post) for blog_post in data]
    return render_template("index.html", items=list_of_objects)


@app.route('/post/<int:i>')
def read_post(i):
    print(i)
    list_of_objects = [Post(blog_post) for blog_post in data]
    return render_template("post.html", _data=list_of_objects[int(i) - 1])


if __name__ == "__main__":
    app.run(debug=True)
