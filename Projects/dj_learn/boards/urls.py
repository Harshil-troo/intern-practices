from django.contrib import admin
from django.urls import path,include


from boards import views
appname = "home"
urlpatterns = [
  path("home/ ", views.home,name='home'),
  path("about/", views.about, name='about'),
  path('about/company/', views.about_company, name='about_company'),
  path('about/author/', views.about_author, name='about_author'),
  path('about/author/vitor/', views.about_vitor, name='about_vitor'),
  path('about/author/erica/', views.about_erica, name='about_erica'),
  path('privacy/', views.privacy_policy, name='privacy_policy'),
  path('/', views.user_profile, name='user_profile'),
  path('boards/', views.board_topics, name='board_topics')

]
