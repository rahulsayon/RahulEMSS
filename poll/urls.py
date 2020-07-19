from django.urls import path,include
from poll.views import index,details,poll


urlpatterns = [
    path('' , index , name='polls-list'),
    path('<int:id>/details' , details , name="poll_details"),
    path('<int:id>/' , poll , name="poll_vote"),

]