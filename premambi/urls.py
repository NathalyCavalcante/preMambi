"""
URL configuration for premambi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# importações para eibir as imagens na página (já que não tenho statics)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # essa url foi registrada posteriormente na url.py de core
    path('', include('core.urls')),
    path('worker/', include('worker.urls')), # pede para incluir aqui todas as urls da pasta worker (que serão geradas muitas, por isso nao tem path individual)    
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Isso avisa ao django que nosso static é a pasta MEDIA que criamos
