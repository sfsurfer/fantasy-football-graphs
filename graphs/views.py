from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .yahoo_controller import YahooController

def index(request):
    o = YahooController()
    o.authenticate()
    template = loader.get_template('fff/score_graphs.html')
    return HttpResponse(template.render({'scoreboards': o.scoreboards}), request)
