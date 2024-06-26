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
    photo = models.FileField(upload_to='media/main_photos')
    majority = models.CharField(max_length=200)
    short_description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Краткая инфа о человеке'
        verbose_name_plural = 'Краткая инфа о людях'


class MyPersonDetail(models.Model):
    person = models.ForeignKey(MyPerson, on_delete=models.PROTECT)
    full_description = models.TextField()
    quote = models.TextField()
    financial_state = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'

    class Meta:
        verbose_name = 'Подробная инфа о человеке'
        verbose_name_plural = 'Подробная инфа о людях'


class Application(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    why_you = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Заявка на редактора'
        verbose_name_plural = 'Заявки на редактора'
