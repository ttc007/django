"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static, settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from demo import  view

urlpatterns = [
    url(r'^admin/', admin.site.urls, name = 'admin'),
    # url(r'^$', view.index),
    url(r'^createProduct', view.create, name = 'createProduct' ),
    url(r'^storeProduct', view.store, name='storeProduct'),
    url(r'^deleteProduct/(?P<id>[0-9]+)/$', view.delete, name='deleteProduct'),
    url(r'^editProduct/(?P<id>[0-9]+)/$', view.edit, name = 'editProduct' ),
    url(r'^updateProduct/(?P<id>[0-9]+)/$', view.update, name = 'updateProduct' ),
    url(r'^buyProduct/(?P<id>[0-9]+)/$', view.buy, name = 'buyProduct' ),

    url(r'^shop', view.shop),


    url(r'^ajaxCategory', view.ajaxCategory),

    
    url(r'^account/', include('login.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^$', view.index, name='index'),
    url(r'^api/', include('api.urls')),
)



