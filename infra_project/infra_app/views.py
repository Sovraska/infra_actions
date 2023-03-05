from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'У меня получилось! ДА РЕальн '
        'оДЕплой по пушу РОБИТ  АЛИлуя'
    )


def second_page(request):
    return HttpResponse('А это вторая страница')
