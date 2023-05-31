from django.db import models

class Currency(models.Model):
    name_currency = models.CharField(
        max_length=50,
        verbose_name="Название валюты"
    )

    def __str__(self) -> str:
        return self.name_currency
    
    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

# Create your models here.
class Products(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название продукта"
    )
    description = models.CharField(
        max_length=300,
        verbose_name= "Описание продукта"
    )
    product_image = models.ImageField(
        upload_to= 'product_images/',
        verbose_name="Фотография продукта"
    )
    price = models.PositiveBigIntegerField(
        verbose_name="Цена"
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="product_currency",
        verbose_name="Название валюты"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия"
    )
    email = models.EmailField(
    max_length=254, 
    unique=True,  
    blank=False,  
    null=False, 
    verbose_name="Email Address" 
    )
    tel = models.CharField(
        max_length=20,
        verbose_name="телефонный номер"
    )
    message = models.TextField(
        verbose_name="Отправить сообщение"
    )

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class OSP(models.Model):
    parent_images = models.ImageField(
        upload_to= 'parent_images/',
        verbose_name="Ваша фото",
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name="Ваш отзыв",
        blank=True,null=True
    )
    def __str__(self) -> str:
        return "Отзывы"
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"