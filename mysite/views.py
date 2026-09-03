from django.http import HttpResponse


def my_index(request):
    return HttpResponse("Hello Index Page!")

def contact_us(request):
    return HttpResponse("<h1>This is contact us</h1>")


# home
# index
# contact us
# admin
# my_resume