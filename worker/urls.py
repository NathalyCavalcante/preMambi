from django.urls import path 
from . import views

app_name = 'worker' 
# criado para facilitar o entendimento, vai agora na urls de premambi

urlpatterns = [
    path('', views.browser, name='browser'),
    path('no_results/', views.no_results, name='no_results'),
    path('new/', views.new, name='new'), 
    path('<int:pk>/', views.profile, name='profile'), 
    path('<int:pk>/delete/', views.delete, name='delete'), 
    # essa pk foi a setada na view (o número da pk é um int)
    path('<int:pk>/edit/', views.edit, name='edit'), 
]