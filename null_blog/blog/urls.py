from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('post/', views.createPost, name='create'),
    path('post/<int:post_id>/', views.postDetailView, name='detail'),
    path('post/<int:post_id>/delete/', views.deletePostView, name='delete'),
    path('profile/<int:user_id>', views.profileView, name='profile'),
    path('profile/<int:user_id>/delete', views.profileDeleteView, name='profile-delete'),
    path('comment/', views.createCommentView, name='comment-create'),
    path('comment/delete/', views.deleteCommentView, name='comment-delete'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
