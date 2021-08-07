from django.urls import path
from . import views


urlpatterns = [

    path('', views.services, name='services'),
    # path('<int:servicesdescription_id/>', views.services_details, name='servicesdescription'),
    path('<int:servicesdescription_id>/', views.services_details, name='services_details'),
]


