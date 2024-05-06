from django.db import models
from django.core.files import File
from django.contrib.auth.models import User

from io import BytesIO
# Create your models here.
 
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
   
    def __str__(self):
        return self.name

class Item(models.Model):
        category = models.ForeignKey(Category, related_name='items' , on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        description = models.TextField(blank=True,null=True)
        price = models.FloatField()
        image = models.ImageField(upload_to='item_images', blank=True,null=True)
        is_sold = models.BooleanField(default=False)
        created_by = models.ForeignKey(User , related_name='items' , on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        class Meta:
                ordering = ('-created_at',)
            
        def __str__(self):
            return self.name

        def get_display_price(self):
            return self.price / 100
        
        def get_thumbnail(self):
            if self.thumbnail:
                return self.thumbnail.url
            else:
                if self.image:
                    self.thumbnail = self.make_thumbnail(self.image)
                    self.save()

                    return self.thumbnail.url
                else:
                    return 'https://via.placeholder.com/240x240x.jpg'   
            
