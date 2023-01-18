from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import requests
import re
from .models import Salaries_in_year
from .models import Vacancies_in_year
from .models import Salary_in_city
from .models import Part_per_city
from .models import Skill_in_year


def index(request):
    return render(request, 'main/index.html')


def demand(request):
    data_sal = Salaries_in_year.objects.all()
    data_vac = Vacancies_in_year.objects.all()
    template = loader.get_template('main/demand.html')
    context = {
        'x': data_sal,
        'y': data_vac,
    }
    return HttpResponse(template.render(context, request))


def geography(request):
    data_sal = Salary_in_city.objects.all()
    data_vac = Part_per_city.objects.all()
    template = loader.get_template('main/geography.html')
    context = {
        'x': data_sal,
        'y': data_vac,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'main/geography.html')


def skills(request):
    data = Skill_in_year.objects.all()
    return render(request, 'main/skills.html', {'data': data})


def recent_vacancies(request):
    vacancies_list = []
    info_list = []
    date_from = f"2022-12-19T00:00:00"
    date_to = f"2022-12-19T23:59:00"
    link = f"https://api.hh.ru/vacancies/?date_from={date_from}&date_to={date_to}"

    params = {
        'text': 'NAME:Менеджер IT-проекта',  # Текст фильтра вакансии
        'area': 113,  # Поиск ощуществляется по РФ
    }

    vacancies = requests.get(link, params).json()["items"]

    i = 0
    for item in vacancies:
        i = i + 1
        vacancy_dict = {}
        info_dict = {}
        id = item["id"]
        if item["salary"] is not None:
            salary_from = 0 if item["salary"]["from"] is None else int(item["salary"]["from"])
            salary_to = 0 if item["salary"]["to"] is None else int(item["salary"]["to"])
            salary = max(salary_to, salary_from) if salary_from == 0 or salary_to == 0 else (salary_from + salary_to) / 2
            salary_currency = item["salary"]["currency"]
        else:
            salary = 0
            link = f"https://api.hh.ru/vacancies/{id}"
            vacancy_data = requests.get(link).json()
            info_dict = {
                'name': item["name"],
                'description': re.sub(r'<[^>]*>', '', vacancy_data["description"]),
                'key_skills': ", ".join([i["name"] for i in vacancy_data["key_skills"]]),
                'area_name': item["area"]["name"],
                'salary': f"{salary} {salary_currency}" if salary != 0 else "не указана",
                'published_at': item["published_at"],
                'employer': item["employer"]["name"],
            }

            info_list.append(info_dict)
            info_list = sorted(vacancies_list, key=lambda x: x["published_at"])
            vacancy_dict["name"] = item["name"]
            vacancy_dict["description"] = re.sub(r'<[^>]*>', '', vacancy_data["description"])
            vacancy_dict["description"] = vacancy_dict["description"].replace('&quot;', '')

            vacancy_dict["key_skills"] = ", ".join([i["name"] for i in vacancy_data["key_skills"]])
            if vacancy_dict["description"] is None:
                vacancy_dict["description"] = "не указаны"
            if len(vacancy_dict["description"]) == 0:
                vacancy_dict["description"] = "не указаны"

            vacancy_dict["area_name"] = item["area"]["name"]
            vacancy_dict["salary"] = f"{salary} {salary_currency}" if salary != 0 else "не указана"

            day = item["published_at"]
            vacancy_dict["published_at"] = day[:4] + '.' + day[5:7] + '.' + day[8:10] + ' в ' + day[11:16]
            vacancy_dict["employer"] = item["employer"]["name"]

            vacancies_list.append(vacancy_dict)

        vacancies_list = sorted(vacancies_list, key=lambda x: x["published_at"])


    to_export = {'all_info': vacancies_list}
    return render(request, 'main/recent_vacancies.html', to_export)



# python manage.py runserver
