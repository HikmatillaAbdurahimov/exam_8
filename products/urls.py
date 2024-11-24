
from django.urls import path
from .views import CategoriesView,ProductsView,DetailView

urlpatterns=[
    path('',CategoriesView.as_view(),name='categories'),
    path('product/<int:id>/',ProductsView.as_view(),name='products'),
    path('detail/<int:id>/',DetailView.as_view(),name='detail')
]
