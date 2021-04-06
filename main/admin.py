from django.contrib import admin

from .models import male_clothes
from .models import female_clothes
from .models import children_clothes
from .models import accessories_clothes

admin.site.register(male_clothes)
admin.site.register(female_clothes)
admin.site.register(children_clothes)
admin.site.register(accessories_clothes)