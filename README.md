# HMongo
Library to easy work with NoSQL database MongoDB

## Installation

Simply run
```bash
pip install HMongo
```

Download or clone repository into your project folder
```bash
git clone https://github.com/dominon12/HMongo
```

## To start work

- Import class MongoDB from the HMongo module
    
```python 
from HMongo import MongoDB
```
    
- Create an instance of the MongoDB class
    
```python
db = MongoDB(
    cluster_path=CLUSTER_PATH,
    db_name=DB_NAME
)
```
    
## Available methods

- add_one 
    
[Use to add one instance to the db]
    
At first create a python class with fields which must be in the db record of this entity:
    
```python
class User:
"""
Model to represent user
"""
def __init__(self, _id, username, first_name, last_name):
    self._id = _id
    self.username = username
    self.first_name = first_name
    self.last_name = last_name
```
    
Create a new instance of the created class
    
```python
new_user = User(
    _id=1,
    username="HellBoy",
    first_name="Neck",
    last_name="Red"
)
```
    
Add a new user object to the db
    
```python
db.add_one(
    collection_name="Users",
    object=new_user
)
```
    
- add_many
    
[Use to add multiple instances to the db]
    
Create a few instances and pass them to the add_many method using python list
    
```python
db.add_many(
    collection_name="Users",
    objects=[user1, user2]
)
```
    
- get_one & get_many 
    
[Use to get a record/records from the db by filter params]
    
```python
user = db.get_one(
    collection_name="Users",
    _id=_1
)
```
```bash
>>> user
>>> {'_id': 1, 'username': 'HellBoy', 'first_name': 'Neck’', 'last_name': 'Red'}
```
    
Get many will return a list of all the objects that satisfies filter params
    
- get_all 
    
[Use to get all the records from selected collection]
    
```python
all_records = db.get_all(
        collection_name="Users"
    )
```
    
- edit_one 
    
[Use to edit one or few fields in one record in the db which satisfies filter params]
    
```python
# Will change field "username" from "HellBoy" to "NotHellBoyNow" in user's account with _id = 1
db.edit_one(
    collection_name="Users",
    keyword="_id",
    value=1,
    username="NotHellBoyNow"
)
```
    
- delete_one 
    
[Use to delete one record which satisfies to your filter params]
    
```python
db.delete_one(
    colection_name="Users",
    _id=1
)
```
    
- delete_all_data 
    
[Use to delete all the data from selected collection]
    
```python
db.delete_all_data(
    collection_name="Users"
)
```    

## Contributing 
Pull requests are welcome :)
 
## Licence
Creative Commons Zero v1.0 Universal