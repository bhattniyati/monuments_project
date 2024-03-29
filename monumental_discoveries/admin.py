from django.contrib import admin
from monumental_discoveries.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Guide)
admin.site.register(Monuments)
admin.site.register(Audio)
admin.site.register(GuideBooking)
admin.site.register(TicketBooking)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(Complain)
