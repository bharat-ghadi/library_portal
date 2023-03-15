from django.shortcuts import render
from .models import BookData, UserData, Workspace, Genre
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def show_books(request):
    all_books = BookData.objects.all()

    return render(request, 'show_books.html', {'all_books': all_books})


def add_book(request, book_id=0):
    if request.method == 'POST':
        bk_name = request.POST['bk_name']
        author = request.POST['author']
        publication = request.POST['publication']
        price = request.POST['price']

        def clean_price(price):
            if price == "":
                price = 0
                return int(price)
            else:
                return int(price)

        price = clean_price(price)

        genre = request.POST['genre']
        new_book = BookData(bk_name=bk_name, author=author, publication=publication, price=price, genre_id=genre)
        new_book.save()
        all_books = BookData.objects.all()
        message = "New book added to records"
        return render(request, 'add_book.html', {'message': message, 'all_books': all_books})

    elif request.method == "GET":

        all_books = BookData.objects.all()

        return render(request, 'add_book.html', {'all_books': all_books})

    else:
        message = "Exception has occurred"
        return render(request, 'output.html', {'message': message})


def show_gen(request):
    if request.method == "GET":
        all_genres = Genre.objects.all()

        return render(request, 'show_gen.html', {'all_genres': all_genres})
        # return render(request, 'add_user.html')

    if request.method == 'POST':
        genre = request.POST['genre']
        new_genre = Genre(genre=genre)
        new_genre.save()
        message = "New genre is added to records"

        all_genres = Genre.objects.all()
        return render(request, 'show_gen.html', {'message': message, 'all_genres': all_genres})



    else:
        message = "Exception has occurred"
        return render(request, 'output.html', {'message': message})


def add_gen(request):
    pass


def show_users(request):
    all_users = UserData.objects.all()

    return render(request, 'show_users.html', {'all_users': all_users})


def add_user(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = int(request.POST['contact'])
        address = request.POST['address']
        membership = request.POST['membership']

        print("*" * 150, membership)

        def membership_status(membership):
            if membership == 'Active':
                return True
            else:
                return False

        membership = membership_status(membership)
        print("*" * 150, membership)
        new_user = UserData(fname=fname, lname=lname, contact=contact, address=address, membership=membership)
        new_user.save()
        all_users = UserData.objects.all()
        message = "New user added to records"
        return render(request, 'add_user.html', {'message': message, 'all_users': all_users})

    elif request.method == "GET":
        all_users = UserData.objects.all()

        return render(request, 'add_user.html', {'all_users': all_users})

    else:
        message = "Exception has occurred"
        return render(request, 'output.html', {'message': message})


# def remove_user(request, user_id=0):
#     if user_id:
#         try:
#             user_to_be_removed = UserData.objects.get(id=user_id)
#             user_to_be_removed.delete()
#             print(user_to_be_removed)
#             users = UserData.objects.all()
#             message = "user removal successful"
#             return render(request, 'remove_user.html', {'message': message, 'users': users})
#         except:
#             message = "User removal unsuccessful"
#             users = UserData.objects.all()
#             return render(request, 'remove_user.html', {'message': message, 'users': users})
#     users = UserData.objects.all()
#     return render(request, 'remove_user.html', {'users': users})

def remove_user(request, user_id=0):
    if user_id:
        try:
            user_to_be_removed = UserData.objects.get(id=user_id)
            user_to_be_removed.delete()
            print(user_to_be_removed)
            all_users = UserData.objects.all()
            message = "user removal successful"
            return render(request, 'add_user.html', {'message': message, 'all_users': all_users})

        except:
            all_users = UserData.objects.all()
            message = "user removal Unsuccessful"
            return render(request, 'add_user.html', {'message': message, 'all_users': all_users})
    all_users = UserData.objects.all()
    return render(request, 'add_user.html', {'all_users': all_users})


def update_user(request, user_id=0):
    user = UserData.objects.get(id=user_id)
    template = loader.get_template('update_user.html')
    context = {"user": user}

    return HttpResponse(template.render(context, request))


def records(request):
    entries = Workspace.objects.all()

    return render(request, 'records.html', {'entries': entries})


def add_record(request):
    if request.method == 'POST':
        user = request.POST['user']
        book = request.POST['book']
        dt_taken = request.POST['dt_taken']
        dt_returned = request.POST['dt_returned']

        def cleaned_date(dt_returned):
            if dt_returned == "":
                dt_returned = None
                return dt_returned
            else:
                return dt_returned

        dt_returned = cleaned_date(dt_returned)

        if dt_returned == None:
            bk_status = False
        else:
            bk_status = True

        # bk_status = request.POST['bk_status']
        new_record = Workspace(user_id=user, book_id=book, dt_taken=dt_taken, dt_returned=dt_returned,
                               bk_status=bk_status)
        new_record.save()
        entries = Workspace.objects.all()
        message = "New record entry added"
        return render(request, 'add_record.html', {'message': message, 'entries': entries})



    elif request.method == "GET":
        entries = Workspace.objects.all()

        return render(request, 'add_record.html', {'entries': entries})

    else:
        message = "Exception has occurred"
        return render(request, 'add_record.html', {'message': message})
