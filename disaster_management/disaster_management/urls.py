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
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOTT)
	