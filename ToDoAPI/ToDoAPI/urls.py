from django.contrib import admin
from django.urls import path, include
from ToDoApiSystem import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('todoapi',views.ToDoView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
