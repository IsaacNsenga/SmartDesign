from django.shortcuts import render

def home(request):

    return render(request, "index.html")

def service(request):

    return render(request, "service.html")

def realisation(request):

    return render(request, "realisation.html")

def blog(request):

    return render(request, "blog.html")

def propos(request):

    return render(request, "propos.html")

def contact(request):

    return render(request, "contact.html")

def offre(request):

    return render(request, "offre.html")

def silver(request):

    return render(request, "silver.html")

def gold(request):

    return render(request, "gold.html")

def diamond(request):

    return render(request, "diamond.html")

