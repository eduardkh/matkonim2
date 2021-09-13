from django.urls import path
import posts.views


app_name = 'posts'
urlpatterns = [
    path('', posts.views.index, name='index'),
    path('<slug:slug>', posts.views.detail, name='recipe_detail'),

]
