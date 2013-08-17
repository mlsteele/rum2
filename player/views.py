from django.http import HttpResponse


def example(req):
    return HttpResponse("Hello there.")
