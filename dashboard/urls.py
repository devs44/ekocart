from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [

    # login
    path('login/', LoginView.as_view(), name="login"),
    # logout
    path('logout/', LogoutView.as_view(), name="logout"),
    # password reset
    path('recoverpassword/', RecoverPasswordView.as_view(), name="recover-password"),
    # password change
    path('changepassword/', PasswordsChangeView.as_view(), name="change-password"),

    # user list
    path('user/create', UserCreateView.as_view(), name='user-create'),
    path('user/list', UsersListView.as_view(), name="user-list"),
    path('userdisable/<int:pk>/',
         UserToggleStatusView.as_view(), name='user-disable'),
    # dashboard view
    path('dashboard/', AdminDashboardView.as_view(), name="dashboard"),

    # Category
    path('dashboard/category/', CategoryListView.as_view(), name="category"),
    path('dashboard/category/create/',
         CategoryCreateView.as_view(), name="category-create"),
    path('dashboard/category/<slug:slug>/update/',
         CategoryUpdateView.as_view(), name="category-update"),
    path('dashboard/category/<slug:slug>/delete/',
         CategoryDeleteView.as_view(), name="category-delete"),

    # image create
    path('dashboard/product/image/create/',
         ProductImageCreateView.as_view(), name='product-image-create'),

    # product urls here
    path('dashboard/product/specific-list/',
         SpecificProductList.as_view(), name='specific-product-list'),
    path('dashboard/product/list/',
         ProductListView.as_view(), name='product-list'),
    path('dashboard/product/create/',
         ProductCreateView.as_view(), name='product-create'),
    path('dashboard/product/<slug:slug>/update/',
         ProductUpdateView.as_view(), name='product-update'),

    path('dashboard/product/<slug:slug>/delete,',
         ProductDeleteView.as_view(), name='product-delete'),

    # brand urls
    path('dashboard/brand/list/', BrandListView.as_view(), name='brand-list'),
    path('dashboard/brand/create/', BrandCreateView.as_view(), name='brand-create'),
    path('dashboard/brand/<int:pk>/update/',
         BrandUpdateView.as_view(), name='brand-update'),
    path('dashboard/brand/<int:pk>/delete/',
         BrandDeleteView.as_view(), name='brand-delete'),


    # size urls
    path('dashboard/size/list/', SizeListView.as_view(), name='size-list'),
    path('dashboard/size/create/', SizeCreateView.as_view(), name='size-create'),
    path('dashboard/size/<int:pk>/update/',
         SizeUpdateView.as_view(), name='size-update'),
    path('dashboard/size/<int:pk>/delete/',
         SizeDeleteView.as_view(), name='size-delete'),

    # customer urls
    path('dashboard/customer/list/',
         CustomerListView.as_view(), name='customer-list'),
    path('dashboard/customer/create/',
         CustomerCreateView.as_view(), name='customer-create'),
    path('dashboard/customer/<int:pk>/update/',
         CustomerUpdateView.as_view(), name='customer-update'),
    path('dashboard/customer/<int:pk>/delete/',
         CustomerDeleteView.as_view(), name='customer-delete'),

    
    # contact urls
    path('dashboard/contact/list/', ContactListView.as_view(), name='contact-list'),
    path('dashboard/contact/create/', ContactCreateView.as_view(), name='contact-create'),
    path('dashboard/contact/<int:pk>/update/',
         ContactUpdateView.as_view(), name='contact-update'),
    path('dashboard/contact/<int:pk>/delete/',
         ContactDeleteView.as_view(), name='contact-delete'),

     # service urls
    path('dashboard/service/list/', ServiceListView.as_view(), name='service-list'),
    path('dashboard/service/create/', ServiceCreateView.as_view(), name='service-create'),
    path('dashboard/service/<int:pk>/update/',
         ServiceUpdateView.as_view(), name='service-update'),
    path('dashboard/service/<int:pk>/delete/',
         ServiceDeleteView.as_view(), name='service-delete'),

   
     # message urls
    path('dashboard/message/list/', MessageListView.as_view(), name='message-list'),
    path('dashboard/message/create/', MessageCreateView.as_view(), name='message-create'),
    path('dashboard/message/<int:pk>/update/',
         MessageUpdateView.as_view(), name='message-update'),
    path('dashboard/message/<int:pk>/delete/',
         MessageDeleteView.as_view(), name='message-delete'),
]
