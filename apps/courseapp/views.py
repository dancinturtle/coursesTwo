from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
      "courses" : Course.objects.all(),
      "descriptions" : Description.objects.all()
    }
    for desc in context['descriptions']:
        print desc.text
    return render(request, 'courseapp/index.html', context)

def create(request):
    course = Course.objects.create(name = request.POST['name'])
    description = Description.objects.create(text = request.POST['desc'], course = course)
    print "JUST ADDED!!!", course.id, description.id

    return redirect ('/')

def confirmDelete(request, id):
    doomed = Course.objects.get(id = id)
    context = {
        "doomed": doomed
    }

    return render(request, 'courseapp/confirmdelete.html', context)

def delete(request, id):

    course = Course.objects.get(id=id)
    messages.warning(request, "The course '{}' has been deleted.".format(course.name))
    course.delete()
    return redirect ('/')

def viewComments(request, id):
    course = Course.objects.get(id = id)
    comments = Comment.objects.filter(course = course)
    context = {
      'course' : course,
      'comments' : comments
    }
    return render(request, 'courseapp/comments.html', context)

def addComment(request):
    courseid = request.POST['courseid']
    course = Course.objects.get(id = courseid)
    comment = Comment.objects.create(comment=request.POST['comment'], commenter = request.POST['name'], course = course)
    return redirect('/courses/comment/{}'.format(courseid))
