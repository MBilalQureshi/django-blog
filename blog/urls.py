from . import views
from django.urls import path, include

# as we are using class based views we need to add as_view in the
# end of PostList, so that it render this class as view
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]
