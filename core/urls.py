from django.urls import path

from . import views

urlpatterns = [
    path("requests/", views.send_request, name="send-request"),
    # path(
    #     "requests/<int:pk>/", views.RequestDetailView.as_view(), name="request-detail"
    # ),
    path("contact/", views.list_contact, name="list-contact"),
]
