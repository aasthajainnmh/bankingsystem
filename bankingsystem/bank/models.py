from django.db import models

class customerList(models.Model):
    CATEGORY_CHOICES=(
        ('Aaranshi','Aaranshi'),
        ('LAtika','Latika'),
        ('Shivin','Shivin'),
        ('Keshav','Keshav'),
        ('Geetanjali','Geetanjali'),
        ('Kiara','Kiara'),
        ('Aarav','Aarav'),
        ('Vian','Vian'),
        ('Shamita','Shamita'),
    )
    name = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    currentbalance = models.IntegerField(default=0)

    def __str__(self):
        return self.name
