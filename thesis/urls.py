from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from thesis import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Todo API', description='RESTful API for Todo')),

    url(r'^', include(('unodosmattress.urls', 'unodosmattress'),namespace='unodosmattress')),
    url(r'^$', views.api_root),
]
