from django.db import models

class News(models.Model):

    # preview = models.ImageField (
    #     "Изображение",
    #     null=True,
    #     blank=True,
    #     upload_to='news'
    # ) 

    title = models.CharField(
        "Название",
        max_length=150,
        null=False,
        blank=False
    )

    desc = models.TextField(
        "Контент",
        null=True,
        blank=True
    )

    dtime = models.DateTimeField(
        "Дата и время",
        null=False,
        blank=False,
        auto_now_add=True
    )

    status = models.BooleanField(
        "Статус",
        null=False,
        blank=False,
        choices=[
            (True, "Обликовано"),
            (False, "Не опубликовано"),
        ],
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"
