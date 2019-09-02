# store-api

A REST API for store, implemented using Flask-RESTful, Flask-JWT, Flask-SQLAlchemy. 


## Installation

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## REST Principle

 * One PATH, multiple VERBS operating on same resource. Similar to object oriented programming.
 * Sigular vs Plural.

## API Best Practices

 * When method is already GET, don't name any endpoint like, /getstudent
