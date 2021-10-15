from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberView

member_list = MemberView.as_view({
    'post': 'create',
    'get': 'list'
})
member_detail = MemberView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('members/', member_list, name='member_list'),
    path('members/<int:pk>/', member_detail, name='member_detail'),
])