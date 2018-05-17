from django.contrib.auth.models import User
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from rest_framework.pagination import PageNumberPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class Custom_UserViewSet(viewsets.ModelViewSet):
    queryset = Custom_User.objects.all()
    serializer_class = Custom_UserSerializer



class Trainer_ModelViewSet(viewsets.ModelViewSet):
    queryset = Trainer_Model.objects.all()
    serializer_class = Trainer_ModelSerializer
    



class Learner_ModelViewSet(viewsets.ModelViewSet):
    queryset = Learner_Model.objects.all()
    serializer_class = Learner_ModelSerializer
    


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Course_ModuleViewSet(viewsets.ModelViewSet):
    queryset = Course_Module.objects.all()
    serializer_class = Course_ModuleSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class Answer_OptionsViewSet(viewsets.ModelViewSet):
    queryset = Answer_Options.objects.all()
    serializer_class = Answer_OptionsSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class Quiz_QuestionViewSet(viewsets.ModelViewSet):
    queryset = Quiz_Question.objects.all()
    serializer_class = Quiz_QuestionSerializer



# PAGINATION BASED SETTINGS (SMALL, STANDARD, LARGE)
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10  #Change the number of objects per page to be visible over here
    page_size_query_param = 'page_size'
    max_page_size = 100


# PAGINATED COURSES VIEW


class PaginatedCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = SmallResultsSetPagination