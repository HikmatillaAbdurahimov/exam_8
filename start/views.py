# from msilib.schema import ListView
#
from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import DeleteView
#
# from start.models import Cart

#
# class CartView(ListView):
#     template_name = 'cart.html'
#     context_object_name = 'cart_products'
#     extra_context = {
#         'footer_fixed': True
#     }
#
#     def get_queryset(self):
#         return self.request.user.cart_set.all()
#
# class CartProductDeleteView(DeleteView):
#     model = Cart
#     success_url = reverse_lazy('cart')
#     pk_url_kwarg = 'cart_product_id'


def account(request):
    return render(request,'account.html')

def cart(request):
    return render(request,'cart.html')


