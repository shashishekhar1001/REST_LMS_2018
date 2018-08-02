from django.contrib import admin
from .models import *
# Register your models here.
from guardian.admin import GuardedModelAdmin

# class Course_ModuleInline(admin.StackedInline):
#     model = Course_Module

# class CourseAdmin(admin.ModelAdmin):
#     inlines = [
#         Course_ModuleInline
#     ]

#     model = Course

class CourseAdmin(GuardedModelAdmin):
    model = Course

admin.site.register(Custom_User)
admin.site.register(Trainer_Model)
admin.site.register(Answer_Options)
admin.site.register(Quiz)
admin.site.register(Quiz_Question)
admin.site.register(Course, CourseAdmin)
admin.site.register(Learner_Model)
admin.site.register(LearnerQnA)
admin.site.register(Subscription)