from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'У меня получилось! ДА РЕальн '
        'Тест Сообщения в тг после деплоя'
    )


def second_page(request):
    return HttpResponse('А это вторая страница')
