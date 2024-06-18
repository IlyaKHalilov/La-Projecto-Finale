from django.shortcuts import render


def render_main(request):
    return render(request, 'app/index.html')
