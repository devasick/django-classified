from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify




# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    #self.slug = slugify(self.name)
    slug = models.CharField(max_length=200)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE) 

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same 
                                                 #slug 

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Listing(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price       = models.DecimalField(decimal_places=2, max_digits=10000)
	featured    = models.BooleanField(default=False)
	#image = models.ImageField(upload_to='product/%Y/%m/%d', db_column='Image', blank=True, null=True)