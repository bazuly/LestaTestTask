from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tf_idf/', include('tf_idf.urls'), name='tf_idf'),
]
