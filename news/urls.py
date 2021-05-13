from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.news_today, name='newsToday'),
    path('archives/<str:past_date>/',views.past_news, name='pastNews'),
    path('search/',views.search_results, name='search_results'),
    #url(r'^article/(\d+)',views.article,name ='article'),
    path('article/<int:article_id>',views.article,name ='article')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)