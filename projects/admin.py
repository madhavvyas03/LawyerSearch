from django.contrib import admin
from .models import Lawyer,Review,Tag,Language,Court
admin.site.register(Language)
admin.site.register(Court)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Lawyer)
# Register your models here.
