from django.shortcuts import render, redirect
from articles.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    Article.objects.create(title=title, content=content)

    # context = {
    #     'title': title,
    #     'content': content
    # }
    #return render(request, 'articles/create.html', context)
    return redirect('articles:index')

# 1. /introduce/ 경로
# 2. h1 태그로 이루어진 제목
# 2-1. 각각의 p 태그에 이름과 나이 작성
# 3. back 링크로 index로 돌아갈 수 있는 링크 하나
# 4. index에서 introduce 이동할 수 있는 링크 하나
# 5. base.html 상속받아서 block body 안에 작성
def introduce(request):
    return render(request, 'articles/introduce.html')

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
        'pk' : article_pk
    }
    
    return render(request, 'articles/detail.html', context)

def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'pk' : article_pk,
        'article' : article
    }
    return render(request,'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect('articles:index')