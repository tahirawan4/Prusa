import math
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.conf import settings

# from orders.models import Order, OrderItem


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])


class Product(models.Model):
    ACCESSORY = 'accessory'
    PRODUCT = 'product'
    PRODUCT_TYPES = ((ACCESSORY, 'Accessory'), (PRODUCT, 'Product'))

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    total_views = models.IntegerField(default=0)
    parent = models.ForeignKey('Product', null=True, blank=True, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100, choices=PRODUCT_TYPES, default=PRODUCT)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def total_likes(self):
        return ProductLike.objects.filter(product=self).count()

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])

    def get_like_url(self):
        return reverse('products:product_like', args=[self.id, self.slug])

    def get_rate_url(self):
        return reverse('products:product_rate', args=[self.id, self.slug])

    def total_items_sold(self):
        return self.order_items.all().aggregate(total=Sum("quantity"))["total"] or 0

    def average_ratings(self):
        if self.rating_set.all().count() > 0:
            return math.ceil(
                self.rating_set.all().aggregate(total=Sum('rate'))['total'] / self.rating_set.all().count())
        return 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    def __str__(self):
        return str(self.id)


class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class CustomContent(models.Model):
    title = models.CharField(max_length=50, default='')
    content = RichTextUploadingField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    COMMENT = 'comment'
    RATE = 'RATE'
    RATE_TYPE = (
        (COMMENT, 'Comment'),
        (RATE, 'Rate')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField()
    rate_type = models.CharField(choices=RATE_TYPE, default=RATE, max_length=20)
    rate = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
