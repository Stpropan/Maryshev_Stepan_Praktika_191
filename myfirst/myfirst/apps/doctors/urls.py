from django.urls import path

from . import views

app_name = 'doctors'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:doctor_id>/', views.doc_info, name = 'doc_info'),
]