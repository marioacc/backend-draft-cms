from djongo import models


# Create your models here.
class User(models.Model):
    """This class represents a user in the CMS"""
    given_name = models.CharField(max_length=255,blank=False) 
    family_name = models.CharField(max_length=255,blank=False)
    role = models.PositiveSmallIntegerField(blank=False)
    def __init__(self, given_name, family_name, role):
        self.givenName = given_name
        self.familyName = family_name
        self.role = role

class ItemStatus(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

class Item(models.Model):
    """This class represents the most basic unit in CMS

    """

    title = models.CharField(max_length=255, blank=False, unique=True)
    body = models.TextField(max_length=500,blank=True,unique=False)
    author =models.ForeignKey(User,on_delete= models.CASCADE)
    status = models.ForeignKey(ItemStatus,on_delete = models.CASCADE)
    image = models.ImageField()

    def __init__(self, title, body, image, author, status):
        self.title = title
        self.body = body
        self.image = image
        self.author = author
        self.status = status

class UserRoles(models.Model):
    """This models maps the fields contained by every user role available
    """
    name = models.CharField(max_length=255, blank=False)

