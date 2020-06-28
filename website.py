from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import requests

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")

@app.route("/about.html")
def form():
	return render_template("about.html")

#@app.route("/courses.html")
#def courses():
	#return render_template("courses.html")

@app.route("/course-details.html")
def course_details():
	return render_template("course-details.html")

@app.route("/contacts.html")
def register():
	return render_template("contacts.html")

@app.route("/elements.html")
def elements():
	return render_template("elements.html")

#@app.route("/blog-home.html")
#def blog_home():
	#return render_template("blog-home.html")

#@app.route("/blog-single.html")
#def blog_single():
	#return render_template("blog-single.html")

if __name__ == '__main__':
	app.run(debug=True)
