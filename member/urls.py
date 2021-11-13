from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberView, EnteranceView

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
enterance_list = EnteranceView.as_view({
    'post': 'create',
    'get': 'list'
})
enterance_detail = EnteranceView.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('members/', member_list, name='member_list'),
    path('members/<int:pk>/', member_detail, name='member_detail'),
    path('enterance/', enterance_list, name= 'enterance_list'),
    path('enterance/<int:pk>/', enterance_detail, name= 'enterance_detail'),
    path('enterance/<word>/', enterance_detail, name = 'enterance_date') # form : 21-10-15 형식
])