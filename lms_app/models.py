from django.db import models



class category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    statesCH = [
        ('Available','Available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    categorys = [
        ('فن','فن'),
        ('تاريخ','تاريخ'),
        ('ثقافة','ثقافة'),
        ('رومانسية','رومانسية'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    author_photo = models.ImageField(upload_to='photos',default='photos/defaultAva/photo1.png' , verbose_name='user avatar')
    book_photo = models.ImageField(upload_to='photos',null=True,blank=True , verbose_name='book photo')
    pages = models.IntegerField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    rental_price_day = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    rental_period = models.IntegerField(max_length=5,null=True,blank=True)
    totalrental = models.DecimalField(max_digits=50, decimal_places=2,null=True,blank=True)
    state_book = models.CharField(max_length=50,choices=statesCH,null=True ,blank=True)
    category = models.ForeignKey(category, on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return self.title


# Create your models here.
