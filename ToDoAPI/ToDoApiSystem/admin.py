from django.contrib import admin
from ToDoApiSystem.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['description', 'duedate', 'status']

admin.site.register(ToDo, ToDoAdmin)
