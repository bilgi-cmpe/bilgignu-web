from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView, ListAPIView

from .serializers import MachineSerializer
from .models import Machine


class MachineListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MachineSerializer

    def get_queryset(self):
        return Machine.objects.all()


class MachineUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MachineSerializer

    def get_queryset(self):
        return Machine.objects.filter(id=self.kwargs["pk"])


class ArcadeView(View):
    def get(self, request):
        try:
            machines = Machine.objects.all()
        except Machine.DoesNotExist:
            return HttpResponse(status=404)
        return render(request, 'arcade/campaign.html', {'machines': machines})
