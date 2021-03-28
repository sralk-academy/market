
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('female', views.female, name='female'),
    path('male', views.male, name='male'),
    path('male/<int:pk>', views.MainDetailModelMale.as_view(), name='new-page'),
    path('female/<int:pk>', views.MainDetailModelFemale.as_view(), name='new-page')
] 
