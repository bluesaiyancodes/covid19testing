# AI powered Covid19 Testing using chest XRay Images

Link to the working site, [here](https://github.com/bluesaiyancodes/covid19testing.git).

Video Demo Link - *Click on Image*

[![Covid19Testing](http://img.youtube.com/vi/wiv9H9c-lOk/0.jpg)](http://www.youtube.com/watch?v=wiv9H9c-lOk "Covid19Testing")

The base code model is based on a post by **Adrian Rosebrock**. His post can be found [here](https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/). I have modified the code as per need and deployed it on **Heroku**. The Heroku deployment was a hideous task as there were some pathblocks with OpenCV.

The images are hosted on 'https://in.000webhost.com' and PhP is used for image upload and management. This was helped by [**@JJ0023**].(https://github.com/JJ0023)

### I have listed the steps below for those who want to try this project.

- First Step is to run the flask model in local system

- If everything is working correctly plan for deployment.

#### Heroku Deployment

1. Create a `Procfile` file and add the following code. This is needed as we are using gunicorn for deployment.
	web: gunicorn __init__:app
	- `__init__` is the name of the pythonfile and app is the flask object
2. Create a `requirements.txt` file and add the required libraries
3. Create a file named `Aptfile` if you use opencv and add the following
	libsm6
	libxrender1
	libfontconfig1
	libice6

	- These dependencies will be installed using apt in heroku
4. create a heroku app
	heroku create covid19testing
5. git create, add, commit your repo

6. Set git to heroku app
	heroku git:remote -a covid19testing

7. Add buildpacks as opencv causes trouble - one for apt download, one for python dependencies
	heroku buildpacks:add https://github.com/heroku/heroku-buildpack-python
	heroku buildpacks:add https://github.com/heroku/heroku-buildpack-apt

8. Push Git 
	git push heroku master

9. Deployed
