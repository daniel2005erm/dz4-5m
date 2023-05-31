from django.db import models

# Create your models here.
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