from django.contrib import admin
from registration.models import *


class UserAdmin(admin.ModelAdmin):
    pass
search_fields = ('first_name', 'last_name', 'email')
list_display = ('first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TestAdmin(admin.ModelAdmin):
   pass
admin.site.register(Test, TestAdmin)

class QuantitativeTestAdmin(admin.ModelAdmin):
   pass
admin.site.register(QuantitativeTest, QuantitativeTestAdmin)

class TechTestAdmin(admin.ModelAdmin):
   pass
admin.site.register(TechTest, TechTestAdmin)

class ReasoningTestAdmin(admin.ModelAdmin):
   pass
admin.site.register(ReasoningTest, ReasoningTestAdmin)

class AptitudeTestAdmin(admin.ModelAdmin):
   pass
admin.site.register(AptitudeTest, AptitudeTestAdmin)

class EligibilityTestAdmin(admin.ModelAdmin):
   pass
admin.site.register(EligibilityTest, EligibilityTestAdmin)

class VerbalsTestAdmin(admin.ModelAdmin):
   pass
admin.site.register(VerbalsTest, VerbalsTestAdmin)

