from django.urls import path 
from . import views
urlpatterns = [
   path('adopt/',views.all_squirrels),
   path('map/',views.map),
   path('adopt/add/', views.add_squirrel),
   path('adopt/stats/',views.stats),
#   path('<str:squirrel_id>/',views.squirrel_details),
   path('adopt/<str:squirrel_id>/',views.edit_squirrel),
]
#the read part tells to capture the specific url parameter.
