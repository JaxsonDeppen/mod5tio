from django.urls import path

from . import views
app_name = 'crud'
urlpatterns = [
    path("", views.events, name="events"),
    path("thank-you", views.thank_you),
    path("review.html", views.ReviewView.as_view(),name='review'),
    path("events",views.events, name="events"),
    path('update_review/<str:pk>/', views.update_review, name="update_review"),
    path('delete_review/<str:pk>/', views.delete_review, name="delete_review")
]
