from django.contrib import admin

from .models import *

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(DemoField)
class DemoFieldAdmin(admin.ModelAdmin):
  fieldsets = [
    (
      '基础字段',
      {
        'fields': [
          'field_bool', 'field_char', 'field_date', 'field_datetime',
          'field_number', 'field_duration', 'field_email', 'field_file',
          'field_image', 'field_int', 'field_ip', 'field_text', 'field_time',
        ]
      }
    ),
    (
      '关联字段',
      {
        'fields': [
          'field_m1', 'field_m2'
        ]
      }
    ),
    (
      '密码字段',
      {'fields': ['field_password']}
    )
  ]
