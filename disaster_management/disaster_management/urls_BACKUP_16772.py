from django.conf.urls import include, url
from django.contrib import admin
from disaster import views
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'disaster_management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^disaster/', views.disaster),
    url(r'^about/', views.about),
    url(r'^donate/', views.packages),
    url(r'^login/', views.register),
]

urlpatterns = format_suffix_patterns(urlpatterns)
<<<<<<< HEAD

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOTT)
	
=======
>>>>>>> c75a2747164eb742dbcb06e80cd9ca197b855fcd
