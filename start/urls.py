from django.urls import path
from . import views
from .views import account,cart

urlpatterns = [
    path('account/', account, name='account'),
    path('cart/',cart,name='cart'),
    # path('cart/', views.CartView.as_view(), name='cart'),
    # path('cart-product-delete/<int:cart_product_id>/', views.CartProductDeleteView.as_view(), name='cart_product_delete'),
    # # path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]