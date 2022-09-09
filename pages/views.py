from django.shortcuts import render

from listings.models import Listing
from teams.models import Team


def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context={
        'listings':listings
    }

    return render(request, 'pages/index.html',context)


def about(request):
    # get all teammates
    team_realtors=Team.objects.order_by('-hire_date')

    # get mvp
    mvp_team_realtors=Team.objects.all().filter(is_mvp=True)

    context={
        'team_realtors':team_realtors,
        'mvp_team_realtors':mvp_team_realtors
    }

    return render(request, 'pages/about.html',context)
