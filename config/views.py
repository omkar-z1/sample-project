from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Kubernetes! changes done after k8s deploy 🚀")
