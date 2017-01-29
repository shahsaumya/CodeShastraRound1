from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from disaster import views
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'disaster_management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 5c2b220970ffe2e77b521e8faa5031d1b887f44c

    #url(r'^index/', views.index),
    #url(r'^disaster/', views.disaster),
    #url(r'^about/', views.about),
    #url(r'^donate/', views.packages),
    #url(r'^login/', views.register),
<<<<<<< HEAD
    
    url(r'^register/', views.register),
=======

=======
>>>>>>> 4257bea1432a5ac4b51143ec63dce24ddb4ea4ac
>>>>>>> 5c2b220970ffe2e77b521e8faa5031d1b887f44c
    url(r'^index/', views.index),
    url(r'^disaster/', views.disaster),
    url(r'^about/', views.about),
    url(r'^donate/', views.packages),

    url(r'^animate/', views.animate),
<<<<<<< HEAD
    url(r'^template-alerts/', views.disaster),

=======
<<<<<<< HEAD

=======
>>>>>>> 4257bea1432a5ac4b51143ec63dce24ddb4ea4ac
>>>>>>> 5c2b220970ffe2e77b521e8faa5031d1b887f44c
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
