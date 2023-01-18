from django.contrib import admin
from .models import Salaries_in_year
from .models import Vacancies_in_year

from .models import Salary_in_city
from .models import Part_per_city

from .models import Skill_in_year


# Register your models here.


admin.site.register(Salaries_in_year)
admin.site.register(Vacancies_in_year)

admin.site.register(Salary_in_city)
admin.site.register(Part_per_city)

admin.site.register(Skill_in_year)


