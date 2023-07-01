from django.urls import path
from Student.views import *

urlpatterns = [
  path('' , get_students , name='student'),
  path('see_marks/<int:std_id>/' ,see_marks, name='marks'),
]