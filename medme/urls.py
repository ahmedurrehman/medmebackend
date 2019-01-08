from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from medme.views import OrderViewSet, CustomerViewSet, MedicineViewSet
from medme import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'medicines', views.MedicineViewSet)
router.register(r'drugs', views.DrugViewSet)


#
# order_list = OrderViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# order_detail = OrderViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# medicine_detail = MedicineViewSet.as_view({
#     'get': 'retrieve',
# })
#
#


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),


]

# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#
#    path('orders/', order_list, name='order-list'),
#     path('orders/<int:pk>/', order_detail, name='order-detail'),
#
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])
