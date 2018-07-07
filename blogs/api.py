from django.db.models import Q
from django.db.models.functions import Lower
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404


from blogs.models import blog, post
from blogs.permissions import BlogPermission, PostPermission
from blogs.serializers import blogSerializer, postSerializer




class BlogViewSet(ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = blogSerializer
    permission_classes = [BlogPermission]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("owner__username",)
    ordering_fields = ("owner__first_name",)

class PostViewSet(ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer
    permission_classes = (PostPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    filter_fields = ('blog_id', )
    search_fields = ("titulo", "cuerpo")
    ordering_fields = ("titulo", "fpublicacion")
    ordering =('-fpublicacion',)

    def get_serializer_class(self):
        return postSerializer if self.action == "list" else postSerializer

    def get_queryset(self):
        queryset = super(PostViewSet, self).get_queryset()

        print(self.kwargs)
        if 'blog_id' in self.kwargs:
            blogid = get_object_or_404(blog, Q(pk=self.kwargs['blog_id']))
            queryset = queryset.filter(blog=blog)

            if not (blog.user == self.request.user or self.request.user.is_superuser):
                queryset = queryset.filter(public=True)

        queryset.order_by(Lower('-fpublicacion'))

        return queryset