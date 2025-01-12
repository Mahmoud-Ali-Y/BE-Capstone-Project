from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('user_list/', views.users_view, name='user_list'),
    path('all_list/', views.all_product_list_view, name='all_product_list'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('create/', views.product_create_view, name='product_create'),
    path('list/', views.product_list_view, name='product_list'),
    path('list/serialize_list', views.product_list_class_view.as_view(), name='product_serialize_list'),
    path('update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
    path('update/<username>/', views.user_update_view, name='user_update'),
    path('delete/<username>/', views.user_delete_view, name='user_delete'),
    path('delete_profile/<username>/', views.profile_delete_view, name='profile_delete'),
]