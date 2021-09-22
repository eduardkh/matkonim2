from django.shortcuts import render, get_object_or_404
from posts.models import Recipe
# Create your views here.


def index(request):
    recipes = Recipe.objects.all().order_by('-timestamp')
    context = {
        'recipes': recipes
    }
    return render(request, 'posts/index.html', context)


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.all(),
        'techniques': recipe.techniques.all(),
        'categories': recipe.categories.all(),
    }
    return render(request, 'posts/detail.html', context)
