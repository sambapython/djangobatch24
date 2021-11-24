from django.http import HttpResponse
import os
def get_users(x):
    #return "HELLO"
    return HttpResponse("HELLO")

def get_cpu_cores(request):
    number_cores = os.cpu_count()
    return HttpResponse(number_cores)