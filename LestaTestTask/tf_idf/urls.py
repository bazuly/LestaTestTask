from django.urls import path
from .views import *

app_name = 'tf_idf'

urlpatterns = [
    path('upload/', upload_text_file, name='upload_text_file'),
    path('list-files/', list_files, name='list_files'),
    path('calculate-tf-idf/<int:file_id>/', calculate_tf_idf_view, name='calculate_tf_idf'),
    path('result-tf-idf/<int:file_id>/', calculate_tf_idf_view, name='calculate_tf_idf_result')
]
