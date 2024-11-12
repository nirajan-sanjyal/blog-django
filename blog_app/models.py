from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=256)
    content= models.TextField()
    author= models.ForeignKey("auth.User",on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    published_at= models.DateTimeField(null=True, blank=True )


    def __str__(self):
        return self.title

# 1 -1 Relationship
# 1 user can have only 1 profile => 1
# 1 profile is associated to only 1 user => 1
# OneToOneField()=> Any models

#  1- M Relationship
# 1 user can add M post => M
# 1 ppst is associated to only 1 user => 1
# In Django use Foreignkey()=> Use in many side models

# M-M relationship

# 1 student can learn from M teachers=>M
# 1 teacher can teacj M stuedents =>M
# ManyToManyField()=> Any Place