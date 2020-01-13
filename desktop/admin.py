from django.contrib import admin
from .models import ToDo
# Register your models here.
    
class ToDoAdmin(admin.ModelAdmin):
	list_display = ('text', 'completed')

admin.site.register(ToDo, ToDoAdmin)