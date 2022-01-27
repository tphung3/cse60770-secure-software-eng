from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Task

from django.core.exceptions import ValidationError


# View functions
def index(request):
	# gets all tasks from the database
	task_list = Task.objects.all() 
	# creates a dictionary to pass this list to the template file
	template_data = {'tasks': task_list}
	# renders the web page
	return render(request, 'index.html', template_data)

# Adds a new task and redirect it back to index page
def add(request):
	# if the form was submitted
	if request.POST:
		title = request.POST['title']
		due_date = request.POST['due_date']
		status = request.POST['status']
		task = Task(title = title, due_date = due_date, status = status)
		try:
		    task.full_clean() 
		    task.save() # if not exception was thrown, form was validated
		except ValidationError as e:
			# renders the web page
			return render(request, 'add.html', {"errors": e.message_dict})
		    
		return HttpResponseRedirect(reverse(f'tasktracker:index'))
	else:
		# renders the web page
		return render(request, 'add.html')


# Deletes a task (based on its primary key) and redirect it back to index page
def delete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return HttpResponseRedirect(reverse(f'tasktracker:index'))