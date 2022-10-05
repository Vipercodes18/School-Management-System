from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "School Management System Admin"
admin.site.site_title = "School Management System Admin Portal"
admin.site.index_title = "Let's Manage Student's Data!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Student.urls'))
]

urlpatterns = patterns('',
    (r'^myadmin/', include(admin_site.urls)),
)