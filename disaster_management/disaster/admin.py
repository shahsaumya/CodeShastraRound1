from django.contrib import admin
from .models import Person,HelpGiver,IndividualDetails,GroupDetails

admin.site.register(Person)
admin.site.register(HelpGiver)
admin.site.register(IndividualDetails)
admin.site.register(GroupDetails)

# Register your models here.
