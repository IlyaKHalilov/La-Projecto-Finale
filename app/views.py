from django.shortcuts import render


def render_main(request):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, 'app/index.html', {'nums': nums})


def render_detail(request):
    return render(request, 'app/details.html')


def render_explore(request):
    return render(request, 'app/explore.html')


def render_create(request):
    return render(request, 'app/create.html')


def render_author(request):
    return render(request, 'app/author.html')
