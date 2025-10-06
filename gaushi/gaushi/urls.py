from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BMI/', views.BMIcalc, name="BMIcalc"),
    path('', views.BMIcalc, name="BMIcalcroot"),  
]


