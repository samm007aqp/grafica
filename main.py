import os
import urllib.request
from flask import Flask, render_template, request , redirect, url_for
from werkzeug.utils import secure_filename
import two as ope

#import cv2
#import math

app=Flask(__name__)

posts = [
	{
		'author':'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'first post content',
		'date_posted': 'April'
	},
	{
		'author':'Marco Aurelio',
		'title': 'Blog Post 2',
		'content': 'La nina',
		'date_posted': 'August'
	}
]
 
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts) 
	#we are passing "post " argument to de template


@app.route("/about")
def about():
	return render_template('about.html',title='About')

#UPLOADS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static/images/upload/')
app.config["IMAGE_UPLOADS"] = "C:/Flask_Proyect/static/images/upload"
#app.config["IMAGE_UPLOADS"] = UPLOADS_PATH

app.config["ALLOWED_IMAGE_EXTENSIONS"]=["PNG","JPG","JPEG","GIF"]

def allowed_image(filename):
	if not "." in filename:
		return False 
	ext = filename.rsplit(".",1)[1]
	if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
		return True
	else: 
		return False 

filename = " "

@app.route("/upload-image", methods=["GET","POST"])
def upload_image():
	global filename
	if request.method =="POST":
		if request.files:
			image = request.files["image"]
			if image.filename ==" ":
				print("Image must have a filename")
				return redirect(request.url)
			if not allowed_image(image.filename):
				print("That image extension is not allowed")
				return redirect(request.url)
			else:
				filename = secure_filename(image.filename)
				image.save(os.path.join(app.config["IMAGE_UPLOADS"],filename))
			print("image saved")
			return redirect(request.url) 
	if filename == " ":
		return render_template('upload_image.html')
	else:
		return render_template('upload_image.html',filename=filename)

	

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='images/upload/' + filename), code=301)

@app.route("/expo-link")
def expo_link():
	if not filename ==" ":
		print(filename)
		fs = 'salida'+filename
		print(fs)
		ope.OperadorExponencial(filename)
		print('I got clicked!')
		return render_template('upload_image.html',salida= fs)
	else:
		return 'Carga una imagen'




if __name__ == '__main__':
	app.run(debug=True)