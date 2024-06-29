from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.views import Response, APIView


class PlanAPIView(APIView):
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self, pk):
        obj = get_object_or_404(id=pk)

        # def get_object(self):
        #     obj = get_object_or_404(Plan, id=self.kwargs["pk"], user=self.request.user)
        #     return obj

class PlanListCreateAPIView(ListCreateAPIView):
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = Plan.objects.all()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return status.HTTP_201_CREATED

