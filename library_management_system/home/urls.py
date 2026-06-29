from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name = 'home'),
    path('books/',views.books,name = 'books'),
    path('purchasebook/',views.purchasebook,name = 'purchasebook'),
    path('issuebook/',views.issue_book,name = 'issuebook'),
    path('returnbook/',views.return_book,name = 'returnbook'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
]