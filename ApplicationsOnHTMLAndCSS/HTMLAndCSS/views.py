from django.shortcuts import render
from django.http import HttpRequest

#HTML and CSS Home page
def htmlAndcssHome(request: HttpRequest):
    return render(request, "HTMLAndCSS/htmlcssHome.html")

#Introduction to HTML page
def htmlIntro(request: HttpRequest):
    return render(request, "HTMLAndCSS/htmlIntro.html")

#Introduction to CSS page
def cssIntro(request: HttpRequest):
    return render(request, "HTMLAndCSS/cssIntro.html")

#Advenced HTML and CSS page
def advancedHtmlCssView(request: HttpRequest):
    return render(request, "HTMLAndCSS/advancedHtmlCss.html")