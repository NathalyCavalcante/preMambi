# URL PRINCIPAIS ONDE REGISTRA AS URLS DE TODOS OS APPS
from django.contrib import admin
from django.urls import path, include
# importações para eibir as imagens na página (já que não tenho statics)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # essa url foi registrada posteriormente na url.py de core
    path('', include('core.urls')),
    # pede para incluir aqui todas as urls de cada app (que serão geradas muitas, por isso nao tem path individual)
    path('inbox/', include('conversation.urls')),
    path('worker/', include('worker.urls')), 
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Isso avisa ao django que nosso static é a pasta MEDIA que criamos
