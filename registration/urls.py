from django.conf.urls import include, url
from registration.views import PromoCodeList, PromoCodeUpdate, PromoCodeCreate, PromoCodeDetail, PromoCodeDelete

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
    url(r'^browse_courses/', 'registration.views.browse_courses', name='browse_courses'),   
    url(r'^browse_course_details/(?P<course_id>\d+)', 'registration.views.browse_course_details', name='browse_course_details'),         
    url(r'^update_cart_session/', 'registration.views.update_cart_session', name='update_cart_session'),         
    url(r'^checkout/', 'registration.views.checkout', name='checkout'),         
    url(r'^checkout_error/', 'registration.views.checkout_error', name='checkout_error'),               
    url(r'^list_promocode/', PromoCodeList.as_view(), name='list_promocode'),         
    url(r'^update_promocode/(?P<id>\d+)', PromoCodeUpdate.as_view(), name='update_promocode'),         
    url(r'^create_promocode/', PromoCodeCreate.as_view(), name='create_promocode'),       
    url(r'^detail_promocode/(?P<id>\d+)', PromoCodeDetail.as_view(), name='detail_promocode'),         
    url(r'^delete_promocode/(?P<id>\d+)', PromoCodeDelete.as_view(), name='delete_promocode'),         
    url(r'^login_as_admin/', 'registration.views.login_as_admin', name='login_as_admin'),         
]
