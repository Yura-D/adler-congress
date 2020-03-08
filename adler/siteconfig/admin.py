# from solo.admin import SingletonModelAdmin
from django.contrib import admin
from .models import SiteSettings


admin.site.register(SiteSettings)
# class SiteSettingAdmin(SingletonModelAdmin):
#     fields = [
#         'ticket_counter_name',
#         'ticket_counter_date',
#     ]
