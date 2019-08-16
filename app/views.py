from django.shortcuts import render
from app.models import Article, Case, Navigation, FriendlyLink, SiteInfo, Slide

# Create your views here.


def index(request):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    article_list = Article.objects.all()
    slide_list = Slide.objects.all()
    friendly_link_list = FriendlyLink.objects.all()
    category_list = Navigation.objects.filter(
        parent_id=4).order_by('sort').all()
    case_dict = {}
    for item in category_list:
        case_dict[item.name] = Case.objects.filter(navigation_id=item.id).all()
    site_info = SiteInfo.objects.order_by('id')[0:1].get()
    return render(request, "index.html", {
        'navigations': navigation,
        'article': article_list,
        'slide': slide_list,
        'cases': case_dict,
        'siteInfo': site_info,
        'links': friendly_link_list
    })


def news_list(request, page=1, size=10):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    start = (page - 1) * size
    end = start + size
    news_list = Article.objects.all()[start:end]
    return render(request, "news/list.html", {
        'navigations': navigation,
    })


def news_detail(request, id):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    news = Article.objects.get(pk=id)
    return render(request, "news/detail.html",
                  {'navigations': navigation,
                   'article': news})


def product(request):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    return render(request, "product/index.html", {'navigations': navigation})


def case_list(request, page=1, size=10):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    return render(request, "case/list.html", {'navigations': navigation})


def about(request):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    return render(request, "about.html", {'navigations': navigation})


def case_detail(request):
    navigation = Navigation.objects.filter(parent_id=0).order_by('sort').all()
    return render(request, "case/detail.html", {
        'navigations': navigation,
    })


def page_not_found(request):
    return render(request, 'error/not-found.html')


def server_error(request):
    return render(request, 'error/server-error.html')


def forbidden(request):
    return render(request, 'error/forbidden.html')
