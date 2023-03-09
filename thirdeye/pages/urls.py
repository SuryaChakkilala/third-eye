from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('menu/', views.menu, name='menu'),
    path('orders/', views.orders, name='orders'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:food_id>', views.add_cart, name='add_item'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),    
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('search/', views.search, name='search'),
    path('recommendation_form/', views.recommendation_form, name='ml'),
    path('thanks/', views.thanks, name='thanks'),
    path('temp/', views.temp, name='temp'),
    path('doctors/', views.doctors, name='doctors'),
    path('book_appointment/<int:doctor_id>', views.book_appointment, name='book_appointment'),
    path('appointments/', views.doctor_appointment_requests, name='appointment_requests'),
    path('approve_appointment/<int:appointment_id>', views.approve_appointment, name='approve_appointment'),
    path('approved_appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('patient_appointments/', views.patient_appointments, name='patient_appointments'),
    path('patient_prescriptions/', views.patient_prescriptions, name='patient_prescriptions'),
    path('doctor_suggest_patient/<int:appointment_id>', views.doctor_suggest_patient, name='doctor_suggest_patient'),
]

handler404 = 'pages.views.error_404'