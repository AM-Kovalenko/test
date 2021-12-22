from django.shortcuts import render


def index(request):
    # posts = Women.objects.all()
    # cats = Category.objects.all()

    context = {

        'title': 'Главная страница',

    }
    return render(request, 'test/index.html', context=context)
