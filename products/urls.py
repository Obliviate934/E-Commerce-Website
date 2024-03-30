
from django.urls import path
from .views import CustomPasswordChangeView
from django.contrib.auth import views as auth_views
from .views import contact
from .views import ProductListView, ProductDetailView, ProductCheckoutView, paymentComplete, SearchResultsListView


urlpatterns = [
    path('', ProductListView.as_view(), name = 'list'),
    path('<int:pk>/', ProductDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', ProductCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('contact/', contact, name='contact'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
]