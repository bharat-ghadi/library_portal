from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.index, name='index'),
    path("show_genres", views.show_gen, name='show_gen'),
    path('show_books', views.show_books, name='show_books'),
    path('show_users', views.show_users, name='show_users'),
    path('records', views.records, name='records'),
    path('add_book', views.add_book, name='add_book'),
    path('add_user', views.add_user, name='add_user'),
    path('add_record', views.add_record, name='add_record'),
    path('remove_user/<int:user_id>', views.remove_user, name='remove_user/id'),
    path('remove_user', views.remove_user, name='remove_user'),
    path('update_user/<int:user_id>', views.update_user, name='update_user/id'),
    path('update_user', views.update_user, name='update_user'),
    path('remove_record', views.remove_record, name='remove_record'),
    path('remove_record/<int:record_id>', views.remove_record, name='remove_record'),
    path('update_record/<int:record_id>', views.update_record, name='update_record'),
    path('update_record/updater/<int:id>', views.updaterecord, name='updaterecord'),

    # path('add_book/<int:book_id>', views.records, name='records')

]
