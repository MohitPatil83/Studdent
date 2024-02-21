from django.contrib import admin
from django.urls import path,include
from enroll import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include('enroll.urls')),
    path('addandshow/',views.add_show),
    path('index/',views.student),
    path('delete/<rid>',views.delete_data),
    path('edit/<rid>',views.update_date),
]
