from django.urls import path
from listings import views
urlpatterns =[
    path('', views.listings, name='listings'),
    path('search', views.search,name='search'),
    path('<int:pk>', views.listing, name='listing')
]