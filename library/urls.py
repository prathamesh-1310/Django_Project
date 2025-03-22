from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookListCreateView, BookRetrieveUpdateDeleteView
from .views import BookListCreateView
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Set index.html as the landing page
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
]