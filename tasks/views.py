from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#Create new form view (Can add whatever fields availabel)
class NewTaskForm(forms.Form):
	task = forms.CharField(label="New Task")
	#example of another field
	#priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
	#Create a list variable by session rather than global
	if "tasks" not in request.session:
		request.session["tasks"] = []

	#Return view of html page passing the tasks list as tasks for html to use
	return render(request, "tasks/index.html", {
		"tasks": request.session["tasks"]
	})

def add(request):
	#Validation serve side
	if request.method == "POST":
		form = NewTaskForm(request.POST)
		if form.is_valid():
			task = form.cleaned_data["task"]
			request.session["tasks"] += [task]	#add task to list
			return HttpResponseRedirect(reverse("tasks:index"))	#Redirect user to index page using reverse url lookup
		else:
			return render(request, "tasks/add.html",{
				"form": form
			})
	return render(request, "tasks/add.html", {
		"form": NewTaskForm()
	})