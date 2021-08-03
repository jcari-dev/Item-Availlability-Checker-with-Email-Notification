from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    
    path('', views.home, name='home'),
    path('newquery/', views.new_query, name="new_query"),
    path('currentqueries/', views.Current_Queries.as_view(), name="current_queries"),
    path('pastqueries/', views.Past_Queries.as_view(), name="past_queries" ),
    path('registeruser/', views.new_user, name="new_user" ),

]