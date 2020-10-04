from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=50)
    second_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    date_of_birth=models.DateField(blank=True,null=True)

    salutationtype_choices=[(1,'Mr'),
                             (2,'Mrs'),
                             (3,'Miss')]
    salutation_type=models.IntegerField(choices=salutationtype_choices,null=True,blank=True)

    gender_choices=[(1,'male'),
                    (2,'female'),
                    (3,'others')]
    gender=models.IntegerField(choices=gender_choices,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name