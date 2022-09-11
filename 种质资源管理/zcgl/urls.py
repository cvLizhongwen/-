from django.contrib import admin
from django.urls import path, include
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
# from servers.views import IndexView
from apps.servers.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('users/', include(('apps.users.urls', 'users'), namespace='users')),
    path('servers/', include(('apps.servers.urls', 'servers'), namespace='servers')),
    # path('apps.users/', include(('apps.users.urls', 'apps.users'), namespace='users')),
    # path('apps.servers/', include(('apps.servers.urls', 'apps.users'), namespace='servers')),
]
