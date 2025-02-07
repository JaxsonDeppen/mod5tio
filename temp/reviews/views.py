from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Review

from .forms import ReviewForm

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})
    
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect("/events")
        
        return render(request, "reviews/review.html", {"form": form})

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect("/events")
    else:
        form = ReviewForm()
    
    return render(request, "reviews/review.html", {
                "form": form
            })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
def events(request):
    events = Review.objects.all()
    context = {'events': events}
    return render(request, 'reviews/events.html',context)
def update_review(request, pk):
    res = Review.objects.get(id=pk)
    form = ReviewForm(instance=res)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/events")
    context = {'form': form}
    return render(request, 'reviews/review.html',context)
def delete_review(request, pk):
    res = Review.objects.get(id=pk)
    if request.method == "POST":
        res.delete()
        return HttpResponseRedirect("/events")
    context ={'item': res}
    return render(request, "reviews/delete.html", context)
