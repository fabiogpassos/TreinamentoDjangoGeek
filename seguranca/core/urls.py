from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('update/<int:pk>/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('delete/<int:pk>/', DeleteProdutoView.as_view(), name='del_produto'),
]