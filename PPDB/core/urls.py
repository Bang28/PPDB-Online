from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ====== PATH TO APP ======|
    path('', include('ppdb.urls', namespace="ppdb")),
    path('pengguna/', include('users.urls', namespace="users")),

    # ====== PATH TO DJANGO ADMIN ======|
    path('admin/', admin.site.urls),

    # ====== PATH JET THEME ======|
    # path(r'jet/', include('jet.urls', 'jet')),
    # path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

# CUSTOM DJANGO ADMIN
admin.site.site_header = "Dashboard Admin"
admin.site.site_title = "SMP Miftahul Falah Gandrungmangu"
admin.site.index_title = "Dashboard Admin"

# ERROR HANDLER
handler404 = "ppdb.views.error_404"
handler505 = "ppdb.views.error_505"