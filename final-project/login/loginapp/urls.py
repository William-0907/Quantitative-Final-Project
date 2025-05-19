from django.urls import path
from .views import login_view,users_view,stats_view,logout_view,graph_view

urlpatterns = [
    path('', login_view,name='login'),
    path('users', users_view,name='users',),
    path('stats', stats_view,name='stats'),
    path('graph', graph_view,name='graph'),
    path('logout', logout_view,name='logout'),
]