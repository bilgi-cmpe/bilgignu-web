from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Machine
from .serializers import MachineSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@csrf_exempt
def api_machine_list(request):
    machines = Machine.objects.all()
    serializer = MachineSerializer(machines, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view()
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def api_machine_detail(request, pk):
    try:
        machine = Machine.objects.get(pk=pk)
    except Machine.DoesNotExist:
        return HttpResponse(status=404)
    machine.money += 1
    machine.save()
    serializer = MachineSerializer(machine)
    return JsonResponse(serializer.data, safe=False)


def arcade(request):
    try:
        machines = Machine.objects.all()
    except Machine.DoesNotExist:
        return HttpResponse(status=404)
    return render(request,'arcade/campaign.html', {'machines':machines})