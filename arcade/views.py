from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Machine
from .serializers import MachineSerializer

@csrf_exempt
def api_machine_list(request):
    machines = Machine.objects.all()
    serializer = MachineSerializer(machines, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_machine_detail(request, pk):
    try:
        machine = Machine.objects.get(pk=pk)
    except Machine.DoesNotExist:
        return HttpResponse(status=404)
    serializer = MachineSerializer(machine)
    return JsonResponse(serializer.data, safe=False)


def arcades(request):
    return render(request, 'arcade/arcade.html')
