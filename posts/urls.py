from django.urls import path
import posts.views
# for media files in test env
from django.conf import settings
from django.conf.urls.static import static


app_name = 'posts'
urlpatterns = [
    path('', posts.views.index, name='index'),
    path('<slug:slug>', posts.views.detail, name='recipe_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
