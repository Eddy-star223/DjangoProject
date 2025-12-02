from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('carts', views.CartViewSet, basename='carts'),
router.register('orders', views.OrderViewSet, basename='orders'),

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='reviews')

cart_router = routers.NestedSimpleRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='carts-items')

urlpatterns = router.urls + product_router.urls + cart_router.urls
