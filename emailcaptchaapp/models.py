from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.CharField(max_length = 255)
    # timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Enquiry from ' + self.name