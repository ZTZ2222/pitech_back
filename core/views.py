from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Request
from .serializers import RequestSerializer


# class RequestListCreateView(generics.ListCreateAPIView):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer


# class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def send_request(request):
    serializer = RequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)