from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from .models import Book
#viewset default rest view for apis : to research more
from rest_framework import viewsets
from .serializers import BookSerializer
#authentification
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#template engine example jinja2
def first(request):
    books = Book.objects.all()
    return render(request,'first_template.html',{'books':books})

# class Another(View):
#     """
#     model_name.objects.method =>
#     method = all => return all
#     method = get => return one element with specific condition
#     method = filter => return all elements that match specific condition
#     """
#     book = Book.objects.get(id=1)
#     output = ''
#
#     output += f" we have {book.title} with ID: {book.id} in our DB <br>"
#     def get(self,resquest):
#         return HttpResponse(self.output)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)