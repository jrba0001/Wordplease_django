from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs.api import BlogViewSet, PostViewSet
from blogs.views import HomeView, List_blogs, nuevo, blog_personal, post_detail, newpost
from users.api import UsersAPI, UserDetailAPI
from users.views import LoginView, LogoutView, SignupView, List_users

router = DefaultRouter()
router.register('api_blog', BlogViewSet)
router.register("posts", PostViewSet, base_name="api_post")



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', HomeView.as_view(), name='home'),
    path('blogs', List_blogs.as_view(), name='list_blog'),
    path('nuevo', nuevo.as_view(), name='nuevo'),
    path('list_user', List_users.as_view(), name = 'list_user'),
    path('blogs/<username>/',blog_personal.as_view(),name='blog'),
    path('new_post', newpost.as_view(), name='new_post'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('detalle/<int:pk>', post_detail.as_view(), name='detalle'),
    path('api/v1/', include(router.urls)),
    path('api/v1/users/', UsersAPI.as_view(), name='api-user'),
    path('api/v1/users/<int:pk>/', UserDetailAPI.as_view(), name='api-user-detail'),



# API URLs
#    path('api/v1/users/', UsersAPI.as_view(), name='api-users'),
#    path('api/v1/users/<int:pk>/', UserDetailAPI.as_view(), name='api-user-detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
