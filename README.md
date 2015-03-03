歐低點菜
======

[![Build Status](https://travis-ci.org/fxxkit/OD-survey.svg?branch=develop)](https://travis-ci.org/fxxkit/OD-survey) 
[![GitHub version](https://badge.fury.io/gh/fxxkit%2FOD-survey.svg)](http://badge.fury.io/gh/fxxkit%2FOD-survey)

## prerequisite

1. Python: including `pip` and `virtualenvwrapper`
2. [Heroku toolbelt](https://toolbelt.heroku.com/)
3. Git/[Github](github.com)

## setup develop env

```
$ git clone git@github.com:fxxkit/OD-survey.git
$ cd OD-survery
$ mkvirtualenv od
$ pip install -r requirements.txt
```

```
$ foreman start
$ python server.py -d
```

## workflow

1. Fork this repository <iframe src="https://ghbtns.com/github-btn.html?user=twbs&repo=bootstrap&type=fork&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>

* Clone from your own Github repo

	```
	git clone <your-git-repo-url>
	git remote rename origin self
	git remote add origin git@github.com:fxxkit/OD-survey.git
	```

* update to the last version: 

	```
$ git checkout develop
$ git pull origin develop
	```

* work on the issues and make some changes, you can check the status using 

	```
$ git status
	```

* add changes to stage, make a commit and push to self

	```
$ git add <files>
$ git commit -m "<messages about this change>"
	```

* go to your own page, send __Pull Request__ (__PR__) via Github

* release master will reviewer the code changes and merge the PR if everything is fine (including the Travis CI build)

## Update tags

```
git tag -a vx.x.x -m "version description"
git push origin --tags 
``` 

## links
- [Herokuapp](https://od-survey.herokuapp.com/)
- [Trello](https://trello.com/b/kaVf0D3t/product-backlog)
- [Travis CI](https://travis-ci.org)
- [Badge](https://badge.fury.io)
