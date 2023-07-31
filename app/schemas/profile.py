from tortoise.models import Model
from tortoise import fields
class Profile(Model):
    # Primary key field is created automatically
    # id = fields.IntField(pk=True) 
    name = fields.CharField(max_length=255)
    age = fields.TextField()
    email = fields.TextField(max_length = 500)
    dob = fields.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
class Demo(Model):
    # Primary key field is created automatically
    # id = fields.IntField(pk=True) 
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    def __str__(self):
        return self.name

class Job(Model):
    # Primary key field is created automatically
    # id = fields.IntField(pk=True) 
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    def __str__(self):
        return self.name