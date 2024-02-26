from django.contrib import admin
from django.urls import path,include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from boards import views

urlpatterns = [
    path('harshil/home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('boards/<int:pk>/', views.board_topics, name='board'),
    path('harshil/', include("boards.urls")),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-form/', accounts_views.logout_view, name='logout_form'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('reset/', PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='password_reset'),
    path('reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('harshil/home/boards/<int:pk>/topics/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    path('harshil/home/boards/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('new_post/', views.new_post, name='new_post'),
    path('harshil/home/boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',views.PostUpdateView.as_view(), name='edit_post'),
    path('harshil/home/', views.BoardListView.as_view(), name='home'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),
]
