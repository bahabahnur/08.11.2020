from django.shortcuts import render
# from django.http import HttpResponse


def posts_list(request):
   n = ["Oleg", "Masha", "Olja", "Ksu"]
   return render(request, 'blog/index.html', context={"names": n})
# Create your views here.
