from django.contrib import admin
from .models.Tutor import Tutor
from .models.Assessment import Assessment
from .models.Institution import Institution


admin.site.register(Tutor)
admin.site.register(Assessment)
admin.site.register(Institution)
