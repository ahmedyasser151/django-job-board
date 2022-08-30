from django.urls import path
from .views import PostListView, post_list

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('fbv_post_list/', post_list, name="fbv_post_list")
]
