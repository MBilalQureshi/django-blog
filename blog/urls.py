from . import views
from django.urls import path, include

# as we are using class based views we need to add as_view in the
# end of PostList, so that it render this class as view
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # first slug is path converter, second slug is keywordname which can be anything
    # https://docs.djangoproject.com/en/3.2/topics/http/urls/#how-django-processes-a-request
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
