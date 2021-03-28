from django.contrib import admin

from .models import male_clothes
from .models import female_clothes

admin.site.register(male_clothes)
admin.site.register(female_clothes)
