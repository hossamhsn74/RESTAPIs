from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import serializers
from ..models import Book
from rest_framework import generics, status
from rest_framework.response import Response

# example of using function based views
# @api_view(["GET"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def welcome(request):
#     content = {"message": "Welcome to the BookStore!"}
#     return JsonResponse(content)

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    def create(self, request, *args, **kwargs):
        super(BookCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added to books",
                    "result": request.data}
        return Response(response)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    def retrieve(self, request, *args, **kwargs):
        super(BookDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(BookDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(BookDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
