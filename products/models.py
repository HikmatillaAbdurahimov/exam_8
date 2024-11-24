from django.db import models



class Categories(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='products/categories')
    create_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['id']


    def __str__(self):
        return self.title



class Products(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()
    image=models.ImageField(upload_to='products/products')
    price=models.BigIntegerField(default=0,blank=True)
    old_price=models.BigIntegerField(default=0,blank=True)
    categories=models.ManyToManyField(Categories)
    create_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['id']


    def __str__(self):
        return self.title
