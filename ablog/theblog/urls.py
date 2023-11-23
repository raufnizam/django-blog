from django.urls import path
from .views import (HomeView, ArticleDetailView, AddPostView, UpdatePostView, 
                                DeletePostView, AddCAtegoryView, category_view, likeView, AddCommentView)

app_name = "blog"

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCAtegoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', category_view, name='category'),
    path('like/<int:pk>', likeView, name="like_post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),

]
