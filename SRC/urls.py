from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from blog_and_comments import api_views
from registration import api_views as registration_api_views


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'custom_users', api_views.Custom_UserViewSet)
router.register(r'blogs', api_views.BlogViewSet)
router.register(r'registration_users', registration_api_views.UserViewSet)
router.register(r'registration_custom_users', registration_api_views.Custom_UserViewSet)
router.register(r'registration_trainers', registration_api_views.Trainer_ModelViewSet)
router.register(r'registration_learners', registration_api_views.Learner_ModelViewSet)
router.register(r'registration_courses', registration_api_views.CourseViewSet)
router.register(r'registration_courses_modules', registration_api_views.Course_ModuleViewSet)
router.register(r'registration_answer_options', registration_api_views.Answer_OptionsViewSet)
router.register(r'registration_quiz', registration_api_views.QuizViewSet)
router.register(r'registration_quiz_questions', registration_api_views.Quiz_QuestionViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'SRC.views.home', name='home'),
    url(r'^authentication/', include('registration.urls')),
    url(r'^blog/', include('blog_and_comments.urls')),    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)