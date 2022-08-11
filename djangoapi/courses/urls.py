
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseView) # the link is localhost:800/courses because the name is added here

urlpatterns = [
    path('', include(router.urls)),
]