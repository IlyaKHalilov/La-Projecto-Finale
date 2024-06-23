from django.shortcuts import render, redirect
from .models import MyPerson, MyPersonDetail, Application
from django.contrib.auth.decorators import user_passes_test, permission_required
from .forms import (UserRegisterForm, UserLoginForm, UserApplicationForm, AddMyPerson, AddMyPersonDetail,
                    PersonUpdateForm, PersonDetailUpdateForm)
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser
from django.http import HttpResponseNotFound


def render_main(request):
    persons = MyPerson.objects.all()
    return render(request, 'app/index.html', {'persons': persons})


@user_passes_test(lambda u: u.is_authenticated, login_url='/login/')
def render_detail(request, pk):
    detailed_person = MyPersonDetail.objects.get(person=pk)

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


@user_passes_test(lambda u: u.is_authenticated, login_url='/login/')
def render_application(request):
    if request.method == 'POST':
        form = UserApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    user = CustomUser.objects.get(id=request.user.id)
    initial_data = {'email': user.email if user else ''}
    form = UserApplicationForm(initial=initial_data)

    return render(request, 'app/application.html', {'form': form})


@user_passes_test(lambda u: u.status == 3 or u.is_admin, login_url='/access_denied/')
def render_applications(request):
    if request.method == 'POST':
        appl = Application.objects.get(id=request.POST['id'])

        if request.POST['status'] == 'Принять':
            users = CustomUser.objects.all()

            if appl.email in [str(user) for user in users]:
                user_redactor = users.get(email=appl.email)
                user_redactor.status = 2

                user_redactor.save()
                appl.delete()

        elif request.POST['status'] == 'Отклонить':
            appl.delete()

    applications = Application.objects.all()

    return render(request, 'app/applications.html', {'applications': applications})


@user_passes_test(lambda u: u.is_authenticated, login_url='/login/')
@user_passes_test(lambda u: u.status >= 2 or u.is_admin, login_url='/access_denied/')
def render_create(request):
    if request.method == 'POST':
        form1 = AddMyPerson(request.POST, request.FILES)
        form2 = AddMyPersonDetail(request.POST)

        if form1.is_valid():
            form1.save()
            return redirect('create')

        if form2.is_valid():
            form2.save()
            return redirect('create')

    form1 = AddMyPerson()
    form2 = AddMyPersonDetail()

    return render(request, 'app/create.html', {'form1': form1, 'form2': form2})


def render_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')

    form = UserLoginForm()

    return render(request, 'app/login.html', {'form': form})


@user_passes_test(lambda u: u.is_authenticated, login_url='/login/')
def render_logout(request):

    logout(request)
    return redirect('index')


def render_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    else:
        form = UserRegisterForm

    return render(request, 'app/register.html', {'form': form})


def render_access_denied(request):
    return render(request, 'app/access_denied.html')


@user_passes_test(lambda u: u.status >= 2 or u.is_admin, login_url='/access_denied/')
def render_update(request, pk):
    person = MyPerson.objects.get(id=pk)
    person_detail = MyPersonDetail.objects.get(person=pk)

    if request.method == 'POST':
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.age = request.POST['age']
        person.gender = request.POST['gender']

        if request.POST['photo']:
            person.photo = request.POST['photo']

        person.majority = request.POST['majority']
        person.short_description = request.POST['short_description']

        person_detail.full_description = request.POST['full_description']
        person_detail.quote = request.POST['quote']
        person_detail.financial_state = request.POST['financial_state']

        person.save()
        person_detail.save()

        return redirect('index')

    form1 = PersonUpdateForm(instance=person)
    form2 = PersonDetailUpdateForm(instance=person_detail)

    return render(request, 'app/update.html', {'form1': form1, 'form2': form2})


def page_not_found(request, exception):
    return render(request, 'app/404.html', status=404)


@user_passes_test(lambda u: u.status >= 2 or u.is_admin, login_url='/access_denied/')
def render_delete(request, pk):
    person = MyPerson.objects.get(id=pk)
    person_detail = MyPersonDetail.objects.get(person=pk)

    person_detail.delete()
    person.delete()

    return redirect('index')


def custom_500(request):
    return render(request, 'app/404.html', status=500)
