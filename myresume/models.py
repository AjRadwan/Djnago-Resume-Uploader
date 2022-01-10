from django.db import models
 
# Create your models here.
STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Arunachal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)

 
class Resume(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=(STATE_CHOICE),max_length=100)
    mobile = models.PositiveIntegerField()
    emaill = models.EmailField()
    jobcity = models.CharField(max_length=100)
    profilel_img = models.ImageField(upload_to='profileimg', blank=True)
    
    def __str__(self):
        return self.name
