# 1
from django.shortcuts import render, render_to_response
# 2
from .models import Article, Comment
# 3
from django.http import HttpResponse, HttpResponseRedirect
# 4
from .forms import ArticleForm
# 5
from django.template.context_processors import csrf

# Create your views here.


def articles_all(request):
    language = "en-gb"
    session_language = "en-gb"

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))
    args['articles_all'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles_all.html', args)


def article_get(request, article_id):
    return render_to_response('article_get.html', {'article_get': Article.objects.get(id=article_id)})


def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response


def create_article(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all/')

    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html', args)


def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/get/%s' % article_id)


def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles_search = Article.objects.filter(title__contains=search_text)

    return render_to_response('ajax_search.html', {'articles_search': articles_search})


def learn_ajax(request):
    name1 = 'Amit'
    return render_to_response('Learn_ajax.html', {'name1': name1})


def learn_ajax1(request):
    ajax_data = open(
        'C:\\Users\\52038474\\Documents\\LEARNING\\PYTHON 3\\Django\\Articles_Django\\assets\\js\\ajax_info.txt', 'r')
    fd = ajax_data.read()

    return render_to_response('Learn1.html', {'name': fd})
