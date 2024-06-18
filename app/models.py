from django.db import models


class MyPerson(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    gender = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Не указано'),
            (2, 'Мужчина'),
            (3, 'Женщина'),
        )
    )
    photo = models.FileField(upload_to='main_photos/')
    majority = models.CharField(max_length=200)
    short_description = models.TextField()


class MyPersonDetail(models.Model):
    person = models.ForeignKey(MyPerson, on_delete=models.PROTECT)
    full_description = models.TextField()
    quote = models.TextField()
