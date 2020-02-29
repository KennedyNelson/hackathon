from django.urls import path

from . import views

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    #path('myposts', PostListingView.as_view(), name='post-list'),
    path('add', views.add, name='add'),
    path('list', views.view, name='viewfarmers'),
    path('', views.createqr, name='qr')
]
