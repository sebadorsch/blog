from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, \
    DeletePostView, AddCategoryView, CategoryView, LikeView, DislikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('dislike/<int:pk>', DislikeView, name='dislike_post'),
    path('article/<int:pk>/add_comment/', AddCommentView.as_view(), name="add_comment"),
    ]
