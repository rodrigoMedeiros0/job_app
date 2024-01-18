from django.urls import path
from app.views import job_list, job_detail

urlpatterns = [
    path('', job_list, name='jobs_home'),
    path('job/<int:id>', job_detail, name='jobs_detail')
]
