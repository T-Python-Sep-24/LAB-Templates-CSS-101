from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

photos = [
    {
        'id': 1,
        'photoName': 'images/Cloud.jpg',
        'captions': [
            "Clouds have amazing details where the colorful blue sky meets the edge of the cloud and make magnificent abstraction which makes the cloud looks close to us. ",
            "when the cloud start to form, it looks like a white volcano."
        ],
        'likes': 55,
    },
    {
        'id': 2,
        'photoName': 'images/rollerCoaster.jpg',
        'captions': [
            "Roller Coasters is an amazing experience and becomes a great scene when build with consideration to how people see it. ",
            "Lights can be gorgeous at nights. "
        ],
        'likes': 25,
    },
    {
        'id': 3,
        'photoName': 'images/sand.jpg',
        'captions': [
            "Peaches are a great place for families and friends to relax. ",
            "Waves Sounds makes it more enjoyable and comforting time. "
        ],
        'likes': 85,
    },
    {
        'id': 4,
        'photoName': 'images/sea.jpg',
        'captions': [
            "When the sunset meets the sea they become a glorious due, where the golden colors start reflecting on the waves. "
        ],
        'likes': 34,
    },
    {
        'id': 5,
        'photoName': 'images/Sky.jpg',
        'captions': [
            "plants like the palms adds to the picture more stable green color",
            "Combined with the blueness of the sky makes the picture more compatible"
        ],
        'likes': 44,
    },
    {
        'id': 6,
        'photoName': 'images/stad.jpg',
        'captions': [
            "Football is pretty popular around the world, and what make it beautiful is how the fans cheer with enthusiasm",
        ],
        'likes': 12,
    },
    {
        'id': 7,
        'photoName': 'images/sunset.jpg',
        'captions': [
            "When the sunset also meets the clouds it gives a nice gradient of the yellow and blue colors which generate other colors",
            "These colors make combinations scenes, especially on the golden hour which is the last hour of the sunset. "
        ],
        'likes': 75,
    }
]

def main_view(request: HttpRequest):

    return render(request, 'main.html')


def html_view(request: HttpRequest):

    return render(request, 'htmlPage.html', context={'photos': photos})


def css_view(request: HttpRequest):

    return render(request, 'cssPage.html', context={'photos': photos})


def ai_article_view(request: HttpRequest):

    return render(request, 'aiArticle.html')


def cv_view(request: HttpRequest):

    return render(request, 'cv.html')