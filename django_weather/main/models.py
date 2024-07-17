from django.db import models


# Create your models here.
class SearchHistory(models.Model):
    city = models.CharField('Город', max_length=100)
    search_count = models.IntegerField('Количество поисков', default=0)
    last_searched = models.DateTimeField('Последний поиск', auto_now=True)

    def __str__(self):
        return str(self.city) + ' - ' + str(self.search_count) + ' - ' + str(self.last_searched)

    class Meta:
        verbose_name = 'История поиска'
        verbose_name_plural = 'История поиска'
