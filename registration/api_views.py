from django.contrib.auth.models import User
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404

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


# Learner QnA's API for POST
class LearnerQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = LearnerQnA.objects.all()
    serializer_class = LearnerQuestionAnswerSerializer


# Learner QnA's List
class LearnerQuestionAnswerList(viewsets.ModelViewSet):
    serializer_class = LearnerQuestionAnswerSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            try:
                print "Inside Queryset"
                custom_user = Custom_User.objects.get(user = self.request.user)
                print custom_user
                if str(custom_user.primary_registration_type) == "Learner":
                    print "Learner"
                    learner = Learner_Model.objects.get(user=custom_user)
                    print learner
                    try:
                        quiz_id = self.kwargs['quiz_id']
                        print quiz_id
                        quiz = get_object_or_404(Quiz, id=quiz_id)
                        if quiz:
                            print quiz
                            return LearnerQnA.objects.filter(quiz_question__quiz=quiz, learner=learner)                                            
                    except Exception as e:
                        print e
            except Exception as e:
                print e
                print "Not a Learner or an unauthorized user or not a subscribed person."
                pass
        else:
            pass