from django.contrib import admin
from apps.models import Contact
from apps.models import product
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('email','password')
admin.site.register(Contact,contactAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('title','description','img')
admin.site.register(product,productAdmin)