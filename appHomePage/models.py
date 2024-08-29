from django.db import models

class ReturnRequest(models.Model):
    first_name = models.CharField(
        "Имя",
        max_length=150,
        null=False,
        blank=False
    )
    email = models.EmailField(
        "Почта",
        null=False,
        blank=False
    )
    phone = models.CharField(
        "Номер телефона",
        max_length=20,
        null=False,
        blank=False
    )
    comment = models.TextField(
        "Комментарий",
        null=True,
        blank=True
    )
    status = models.BooleanField(
        "Статус",
        choices=[
            (True, "Обработано"),
            (False, "Не обработано"),
        ],
        default=False
    )
    dtime = models.DateTimeField(
        "Дата и время",
        auto_now_add=True # автомат. заполнение
    )
    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name = "обращение"
        verbose_name_plural = "Обращения на сайте"
        
