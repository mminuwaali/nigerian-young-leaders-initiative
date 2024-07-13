from . import models
from django.shortcuts import render
from django.core.paginator import Paginator


def index_view(req):
    page = req.GET.get("page", 1)
    query = models.Blog.objects.all()
    categories = models.Category.objects.all()

    blogs = Paginator(query, 10).get_page(page)

    context = {"blogs": blogs, "categories": categories}
    return render(req, "blogging/index.html", context)


def category_detail_view(request, id):
    page = request.GET.get("page", 1)
    category = models.Category.objects.get(id=id)
    query = models.Blog.objects.filter(category=category)

    blogs = Paginator(query, 10).get_page(page)

    context = {"blogs": blogs, "category": category}
    return render(request, "blogging/category/detail.html", context)


def detail_view(req, id):
    blog = models.Blog.objects.get(id=id)

    context = {"blog": blog}
    return render(req, "blogging/detail.html", context)
