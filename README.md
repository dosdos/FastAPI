# FastAPI endpoints

A set Python FastAPI endpoint hosted on Heroku.

You can try it online on: [fastapy.herokuapp.com](https://fastapy.herokuapp.com/docs)

### Run the project locally ###

Clone the project and setup the virtualenv:
```
$ git clone git@bitbucket.org:Dosdos/fast-api.git
$ mkvirtualenv -p python3 fast-api
$ workon fast-api
$ cd fast-api
$ pip3 install -r requirements.txt
```

Then, run via uvicorn:
```
$ uvicorn main:app --reload
```

### Deploy the project on Heroku ###

```
$ heroku login
$ heroku git:remote -a fastapy
$ git push heroku main
$ heroku open
```

### Run tests ###

To run unit tests simply type:

```
$ pytest
```

### Contribution guidelines ###

Feel free to:

* Writing more tests
* Doing code review
* Add comments

### Who do I talk to? ###

* Repo owner or admin: dosdos
* Contact: dav.santucci@gmail.com

### Further Readings ###

* [Official FastAPI Docs](https://fastapi.tiangolo.com/)
* [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
