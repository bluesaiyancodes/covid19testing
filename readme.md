First Step is to run the flask model in local system
If everything is working correctly plan for deployment.

Heroku Deployment

1. Create a <Procfile> file and add the following code. This is needed as we are using gunicorn for deployment.
	web: gunicorn __init__:app
	- __init__ is the name of the pythonfile and app is the flask object
2. Create a <requirements.txt> file and add the required libraries
3. Create a file named <Aptfile> if you use opencv and add the following
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
