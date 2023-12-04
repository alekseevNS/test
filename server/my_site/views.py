import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from my_site.forms import CalcForm
from my_site.models import CalcHistory


def get_default_menu() -> tuple:
    return (
        {"link": '/', "text": "Главная"},
        {"link": "/calc/", "text": "Калькулятор"}
    )


def index_page(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "Главная", "menu": get_default_menu(), "current_link": '/'}

    return render(request, "index.html", context)


def calc_page(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "Калькулятор", "menu": get_default_menu(), "current_link": "/calc/"}

    if request.method == "POST":
        calc_form_get = CalcForm(request.POST)

        # Тут по хорошему надо проверить форму на валидность -- но мы это опустим (если на предыдущем занятии)

        first_number = calc_form_get.data["first_number"]
        second_number = calc_form_get.data["second_number"]

        result_number = int(first_number) + int(second_number)

        CalcHistory(first_number=first_number, second_number=second_number, result_number=result_number,
                    date=datetime.datetime.now()).save()

        context["calc_form"] = calc_form_get
    else:
        context["calc_form"] = CalcForm()

    context["calc_history"] = CalcHistory.objects.all()

    return render(request, "calc.html", context)
