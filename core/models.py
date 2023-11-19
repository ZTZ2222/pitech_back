from django.db import models


class Request(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email", max_length=100)
    phone = models.CharField("Телефон", max_length=50)
    message = models.TextField("Сообщение")
    timestamp = models.DateTimeField("Дата заявки", auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-timestamp", "email"]
