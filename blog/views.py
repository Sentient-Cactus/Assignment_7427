
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

from blog.forms import DogForm, UpdateDogForm, ActivityForm, UpdateActivityForm, AddCommentForm, UpdateCommentForm
from blog.models import Dog, Activity, Breed, Comment


class HomePage(ListView):
    model = Dog
    template_name = 'home.html'
class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"
    def get_context_data(self, **kwargs):
        context = super(DogDetail, self).get_context_data(**kwargs)
        dog = get_object_or_404(Dog, id=self.kwargs['pk'])
        context["age"] = dog.age()
        return context
class AddDog(CreateView):
    model = Dog
    form_class = DogForm
    template_name = 'add_dog.html'
class UpdateDog(UpdateView):
    model = Dog
    form_class = UpdateDogForm
    template_name = 'update_dog.html'
class DeleteDog(DeleteView):
    model = Dog
    template_name = 'delete_dog.html'
    success_url = reverse_lazy('home')
class BreedDetail(ListView):
    model = Breed
    template_name = 'breed/breed_details.html'
class AddBreed(CreateView):
    model = Breed
    template_name = 'breed/add_breed.html'
    fields = ['name']
class UpdateBreed(UpdateView):
    model = Breed
    template_name = 'breed/update_breed.html'
    fields = '__all__'
class DeleteBreed(DeleteView):
    model = Breed
    template_name = 'breed/delete_breed.html'
    success_url = reverse_lazy('home')

class ActivityPage(ListView):
    model = Activity
    template_name = "activity/activity_page.html"
class ActivityDetail(DetailView):
    model = Activity
    template_name = "activity/activity_detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ActivityDetail, self).get_context_data(**kwargs)
        activity = get_object_or_404(Activity, id=self.kwargs['pk'])
        joined = False
        if activity.join.filter(id=self.request.user.id).exists():
            joined = True
        context["total_joins"] = activity.total_joins()
        context["joined"] = joined
        return context
class CreateActivity(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity/create_activity.html'
class UpdateActivity(UpdateView):
    model = Activity
    form_class = UpdateActivityForm
    template_name = 'activity/update_activity.html'
class DeleteActivity(DeleteView):
    model = Activity
    template_name = 'activity/delete_activity.html'
    success_url = reverse_lazy('activity')
def JoinView(request, pk):
    activity = get_object_or_404(Activity, id=request.POST.get('activity_id'))
    joined = False
    if activity.join.filter(id=request.user.id).exists():
        activity.join.remove(request.user)
    else:
        activity.join.add(request.user)
        joined = True
    return HttpResponseRedirect(reverse('activity-detail', args=[str(pk)]))

class AddComment(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'comment/add_comment.html'

    def form_valid(self, form):
        form.instance.dog_id = self.kwargs['pk']
        return super().form_valid((form))

class MyDog(ListView):
    model = Dog
    template_name = 'my_dog.html'