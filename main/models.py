from django.db import models

# Create your models here.


class Salaries_in_year(models.Model):
    year = models.CharField('Год', max_length=4)
    all_professions = models.IntegerField('Доход всех профессий')
    it_manager = models.IntegerField('Доход менеджера IT-проекта')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'доход по году'
        verbose_name_plural = 'доход по годам'


class Vacancies_in_year(models.Model):
    year = models.CharField('Год', max_length=4)
    all_professions = models.IntegerField('Доля всех профессий')
    it_manager = models.IntegerField('Доля менеджера IT-проекта')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'количества вакансий по году'
        verbose_name_plural = 'количества вакансий по годам'


class Salary_in_city(models.Model):
    citis = models.CharField('Название городов', max_length=30)

    city_collum_1 = models.CharField('Город колонка 1', max_length=15)
    salary_collum_1 = models.IntegerField('Доход всех профессий колонка 1')

    city_collum_2 = models.CharField('Город колонка 2', max_length=15)
    salary_collum_2 = models.IntegerField('Доход всех профессий колонка 2')

    def __str__(self):
        return str(self.citis)

    class Meta:
        verbose_name = 'доход по городу'
        verbose_name_plural = 'доход по городам'


class Part_per_city(models.Model):
    citis = models.CharField('Название городов', max_length=30)

    city_collum_1 = models.CharField('Город колонка 1', max_length=30)
    salary_collum_1 = models.IntegerField('количество вакансий в городе колонка 1')
    part_collum_1 = models.CharField('Доля 1', max_length=4)

    city_collum_2 = models.CharField('Город колонка 2', max_length=30)
    vacancies_collum_2 = models.IntegerField('Количество вакансий колонка 2')
    part_collum_2 = models.CharField('Доля 2', max_length=15)

    def __str__(self):
        return str(self.citis)

    class Meta:
        verbose_name = 'количество вакансий по городу'
        verbose_name_plural = 'количество вакансий по городам'


class Skill_in_year(models.Model):
    year = models.CharField('Год', max_length=4)
    skill = models.CharField('Навык', max_length=50)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Навык по году'
        verbose_name_plural = 'Навыки по годам'



#class Basement_text(models.Model):
#    text = models.CharField('Текст в footer', max_length=50)
#
#    def __str__(self):
#        return str(self.text)
