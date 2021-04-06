
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('female', views.female, name='female'),
    path('male', views.male, name='male'),
    path('children', views.children, name='children'),
    path('accessories', views.accessories, name='accessories'),
    path('male/<int:pk>', views.MainDetailModelMale.as_view(), name='new-page'),
    path('female/<int:pk>', views.MainDetailModelFemale.as_view(), name='new-page'),
    path('children/<int:pk>', views.MainDetailModelChildren.as_view(), name='new-page'),
    path('accessories/<int:pk>', views.MainDetailModelAccessories.as_view(), name='new-page')  
] 
