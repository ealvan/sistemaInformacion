from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Diario
# Create your views here.


def principal(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "base.html", {})


class MensajeJsonEnviados(View):
    def get(self, request, *args, **kwargs):
        start = request.GET['start']
        print(start)
        queryset = Diario.objects.filter(id=5)
        return JsonResponse(list(queryset.values()), safe=False)
