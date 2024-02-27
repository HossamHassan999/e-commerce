from django.urls import path

from . import views

app_name = "testapp"

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/login/', views.login_view, name='login'),
    
    path('logout/', views.custom_logout, name='logout'),

    path("about", views.about, name="about"),

    path("product", views.product, name="product"),

    path("why", views.why, name="why"),

    path("cart", views.cart, name="cart"),

    path("testimonial", views.testimonial, name="testimonial"),

    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),


]