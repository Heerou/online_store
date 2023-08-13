from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Cateories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category =  models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description =  models.TextField(blank=True, null=True)
    price =  models.FloatField()
    image =  models.ImageField(upload_to='items_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    create_by =  models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name