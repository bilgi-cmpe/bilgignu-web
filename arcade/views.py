from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.response import Response

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.money += int(request.data.get("money"))
        instance.save()

        serializer = self.get_serializer(instance, data={}, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class ArcadeView(View):
    def get(self, request):
        try:
            machines = Machine.objects.all()
        except Machine.DoesNotExist:
            return HttpResponse(status=404)
        return render(request, 'arcade/campaign.html', {'machines': machines})
