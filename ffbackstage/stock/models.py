from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Products(models.Model):
    code = models.IntegerField(unique=True, db_index=True)
    article = models.CharField(max_length=24)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=24, blank=True)
    description = models.TextField(blank=True)
    initial_qua = models.IntegerField(default=0)
    base_price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_supplied = models.BooleanField(default=True)
    is_promo = models.BooleanField(default=False)
    markup = models.DecimalField(max_digits=10, decimal_places=5, default=1)
    discount = models.DecimalField(max_digits=10, decimal_places=5, default=1)
    brand = models.ForeignKey('Brands', on_delete=models.PROTECT, related_name='brand_prod')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    tags = models.ManyToManyField('TagsProducts', blank=True, related_name='tags')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/%Y/%m/%d',
                              default='product_photos/skincare_icon.png',
                              verbose_name='Фото', blank=True, null=True)
    history = HistoricalRecords()

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_card', kwargs={'product_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Brands(models.Model):
    name = models.CharField(max_length=100)
    name_short = models.CharField(max_length=24, blank=True)
    markup = models.DecimalField(max_digits=10, decimal_places=5, default=1)
    discount = models.DecimalField(max_digits=10, decimal_places=5, default=1)
    vat = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    history = HistoricalRecords()

    objects = models.Manager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('brands', kwargs={'brand_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class TagsProducts(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        ordering = ['tag']
        verbose_name = 'Тег товара'
        verbose_name_plural = 'Теги товаров'


# class Vendors(models.Model):
#     name_short = models.CharField(max_length=24, blank=True)
#     name_full = models.CharField(max_length=255, blank=True)
#     legal_address = models.CharField(max_length=255, blank=True)
#     physical_address = models.CharField(max_length=255, blank=True)
#     inn = models.CharField(max_length=24, blank=True)
#     kpp = models.CharField(max_length=24, blank=True)
#     ogrn = models.CharField(max_length=24, blank=True)
#     payment_account = models.CharField(max_length=24, blank=True)
#     bank_name = models.CharField(max_length=255, blank=True)
#     correspondent_account = models.CharField(max_length=24, blank=True)
#     bik = models.CharField(max_length=24, blank=True)
#
#
# class DebitDoc(models.Model):
#     datetime_import = models.DateTimeField(auto_now_add=True)
#     number_doc = models.IntegerField(blank=True)
#     date_doc = models.DateField(blank=True)
#     total_qua = models.IntegerField(blank=True)
#     sum_without_VAT = models.DecimalField(max_digits=11, decimal_places=2)
#     sum_VAT = models.DecimalField(max_digits=11, decimal_places=2)
#     sum_with_VAT = models.DecimalField(max_digits=11, decimal_places=2)
#     vendor = models.ForeignKey('Vendors', on_delete=models.PROTECT, related_name='debit_doc')
#     comment = models.CharField(max_length=255, blank=True)
#
#     def __str__(self):
#         return self.number_doc
#
#
# class DebitDocItems(models.Model):
#     code = models.ForeignKey('Products', on_delete=models.PROTECT, to_field='code')
#     article = models.CharField(max_length=24)
#     name = models.CharField(max_length=255)
#     sum_without_VAT = models.DecimalField(max_digits=11, decimal_places=2)
#     sum_VAT = models.DecimalField(max_digits=11, decimal_places=2)
#     sum_with_VAT = models.DecimalField(max_digits=11, decimal_places=2)
#     qua = models.IntegerField()
#     debit_doc = models.ForeignKey('DebitDoc', on_delete=models.PROTECT, related_name='number_doc')
