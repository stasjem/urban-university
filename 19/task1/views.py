from django.http import HttpResponse


def homepageview(request):
    return HttpResponse('Hello world')