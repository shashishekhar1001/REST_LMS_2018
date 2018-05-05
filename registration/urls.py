from django.conf.urls import include, url

urlpatterns = [
    url(r'^user_creation/$', 'registration.views.custom_user_creation', name='custom_user_creation'),  
    url(r'^activate_user/', 'registration.views.activate_user', name='activate_user'),
    url(r'^login/', 'registration.views.my_login', name='login'),
    url(r'^logout/', 'registration.views.logout_view', name='logout'),
    url(r'^trainer_update_profile/', 'registration.views.trainer_update_profile', name='trainer_update_profile'),
    url(r'^edit_course_modules/(?P<course_id>\d+)', 'registration.views.edit_course_modules', name='edit_course_modules'),
    # url(r'^edit_course_modules/(?P<course_id>\d+)', 'registration.views.edit_course_modules', name='edit_course_modules'),
    url(r'^display_courses/', 'registration.views.display_courses', name='display_courses'),
    url(r'^add_course/', 'registration.views.add_course', name='add_course'),
    url(r'^test/', 'registration.views.test_view', name='test_view'),
    url(r'^edit_course_details/(?P<course_id>\d+)', 'registration.views.edit_course_details', name='edit_course_details'),    
]
