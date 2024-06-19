from django.shortcuts import render, redirect
from .models import MyPerson, MyPersonDetail
from django.contrib.auth.decorators import user_passes_test
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout


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


def render_logout(request):

    logout(request)
    return redirect('index')


def render_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('lmlkmlkmlk')
            user = form.save()
            login(request, user)
            return redirect('index')

    else:
        form = UserRegisterForm()

    return render(request, 'app/register.html', {'form': form})

