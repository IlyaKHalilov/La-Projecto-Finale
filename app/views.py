from django.shortcuts import render
from .models import MyPerson, MyPersonDetail


def render_main(request):
    persons = MyPerson.objects.all()
    return render(request, 'app/index.html', {'persons': persons})


def render_detail(request, pk):
    detailed_person = MyPersonDetail.objects.get(id=pk)
    if len(str(detailed_person.financial_state)) >= 10:
        new_financial_state = str(round(detailed_person.financial_state / 1000000000, 1)) + '$ млрд.'

    elif len(str(detailed_person.financial_state)) >= 7:
        new_financial_state = str(round(detailed_person.financial_state / 1000000, 1)) + '$ млн.'

    elif len(str(detailed_person.financial_state)) >= 4:
        new_financial_state = str(round(detailed_person.financial_state / 1000, 1)) + '$ тыс.'

    try:
        detailed_person.financial_state = new_financial_state

    except:
        pass

    return render(request, 'app/details.html', {'d_person': detailed_person})


def render_explore(request):
    return render(request, 'app/explore.html')


def render_create(request):
    return render(request, 'app/create.html')


def render_author(request):
    return render(request, 'app/author.html')
