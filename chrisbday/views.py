import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
	now = datetime.datetime.now()
	return render(request, "chrisbday/index.html", {
		"chrisbday": now.month == 5 and now.day == 31
	})