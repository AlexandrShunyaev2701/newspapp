from django.urls import path
# Импортируем созданные нами представления
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:id>', OnePost.as_view()),
   path('search/', PostSearch.as_view()),
   path('news/create/', PostCreate.as_view()),
   path('articles/create/', NewsCreate.as_view()),
   path('news/<int:pk>/edit', PostEdit.as_view()),
   path('articles/<int:pk>/edit', NewsEdit.as_view(), name='post_list'),
   path('<int:pk>/delete', PostDelet.as_view()),
   path('login/', LoginView.as_view(template_name='login.html'),
        name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'),
        name='logout'),
   path('upgrade/', upgrade_me, name="upgrade"),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
