from django.shortcuts import render,redirect
from.models import book,issuebook, purchasebook
from.forms import BookingForm,PurchaseBookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')


@login_required
def books(request):
    dict_book = {
        'book': book.objects.all
    }
    return render(request,'books.html',dict_book)


@login_required
def purchasebook(request):
    if request.method == 'POST':
        form = PurchaseBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PurchaseBookForm()
    return render(request,'purchasebook.html',{'form': form})

@login_required
def issue_book(request):
    data = issuebook.objects.all
    dict_issuebook = {
        'books': data
    }
    return render(request,'issuebook.html',dict_issuebook)


@login_required
def return_book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            stud_name = form.cleaned_data['stud_name']
            book_name = form.cleaned_data['book_name']

            issued = issuebook.objects.filter(
                stud_name=stud_name,
                book_name=book_name
            ).exists()

            if not issued:
                form.add_error(
                    'book_name',
                    'This book was not issued to this student.'
                )
            else:
                form.save()
                return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'returnbook.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

