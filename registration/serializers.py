from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')




class Custom_UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Custom_User
        fields = ('url', 'user', 'mobile', 'primary_registration_type')




class Trainer_ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer_Model
        fields = ('url', 'user', 'city', 'state', 'country', 'profile_picture', 'courses_tutoring', 'describe_yourself', 'linked_in_url', 'skills', 'cv')


class Learner_ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Learner_Model
        fields = ('url', 'user', 'profile_picture', 'courses_learning')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url', 'part_of', 'topic_name')


class Answer_OptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer_Options
        fields = ('url', 'text')



class Quiz_QuestionSerializer(serializers.HyperlinkedModelSerializer):
    possible_answers = Answer_OptionsSerializer(many=True, read_only=True)
    correct = Answer_OptionsSerializer(read_only=True)
    class Meta:
        model = Quiz_Question
        fields = ('url', 'quiz', 'q_type', 'text', 'possible_answers', 'selected', 'correct')



class QuizSerializer(serializers.HyperlinkedModelSerializer):
    questions = Quiz_QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ('url', 'quiz_name', 'module_referred', 'questions')


class Course_ModuleSerializer(serializers.HyperlinkedModelSerializer):
    video = serializers.FileField(max_length=None, use_url=True, required=False)
    quiz = QuizSerializer(many=True, required=False)
    class Meta:
        model = Course_Module
        fields = ('id', 'url', 'part_of', 'name', 'video', 'Presentation', 'Assignment', 'topics', 'order', 'quiz')

    def create(self, validated_data):
        quiz_data = validated_data.pop('quiz')
        module = Course_Module.objects.create(**validated_data)
        for qd in quiz_data:
            Quiz.objects.create(module_referred = module, **qd)
        return module

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.part_of = validated_data.get('part_of', instance.part_of)
        instance.video = validated_data.get('video', instance.video)
        instance.Presentation = validated_data.get('Presentation', instance.Presentation)
        instance.Assignment = validated_data.get('Assignment', instance.Assignment)
        instance.topics = validated_data.get('topics', instance.topics)
        instance.order = validated_data.get('order', instance.order)
        try:
            quiz_data = validated_data.get('quiz')
        except:
            pass
        if quiz_data:
            # instance.quiz.clear()
            Quiz.objects.bulk_create(
               [
                 Quiz(module_referred=instance, **quiz)
                 for quiz in quiz_data
               ],
            )
        print instance.video
        instance.save()
        return instance 


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    modules = Course_ModuleSerializer(many=True)
    class Meta:
        model = Course
        fields = ('url', 'thumbnail', 'course_by', 'course_name', 'description', 'prerequisite', 'requirements', 'modules')
        
