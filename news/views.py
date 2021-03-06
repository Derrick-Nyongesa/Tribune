from django.http.response import Http404
from django.shortcuts import render,redirect
from .models import Article
import datetime as dt


# Create your views here.
def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()

    return render(request, 'all-news/today-news.html',{"date":date, "news":news})


def past_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)

    return render(request, 'all-news/past-news.html',{"date":date, "news":news})


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


def article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()

    return render(request, "all-news/article.html", {"article":article})