from django.db import models


# Create your models here.

class Item:
    def __init__(self, title, body, image, author, status):
        print("This is the constructor method for Item")
        self.title = title
        self.body = body
        self.image = image
        self.author = author
        self.status = status


class User:
    def __init__(self, given_name, family_name, role):
        print("This is the constructor method for User")
        self.givenName = given_name
        self.familyName = family_name
        self.role = role
