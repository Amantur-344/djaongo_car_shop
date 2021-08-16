from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cars.forms import CarCreateForm, CarUpdateForm
from cars.models import Category, Car


def main_page(request):
    categories = Category.objects.all()
    cars = Car.objects.all()
    paginator = Paginator(cars, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'cars': page_obj
    }
    return render(request, 'car/main_page.html', context)


@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST)
        if form.is_valid():
            car = form.save()
            car.author = request.user
            car.save()
    form = CarCreateForm()
    context = {
        'form': form
    }
    return render(request, 'car/car_create.html', context)


@login_required
def my_cars(request):
    cars = Car.objects.filter(author=request.user)
    paginator = Paginator(cars, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'car/main_page.html',
                  context={'cars': page_obj})


def category_cars(request, pk):
    category = Category.objects.filter(id=pk).first()
    cars = Car.objects.filter(category=category)
    paginator = Paginator(cars, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'car/main_page.html',
                  context={'category': category, 'cars': page_obj})


def search(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(title__icontains=query)
    return render(request, 'car/main_page.html',
                  context={'cars': cars})


def car_detail(request, pk):
    author = None
    car = Car.objects.filter(id=pk).first()

    not_anonymous = not (isinstance(request.user, AnonymousUser))
    if not_anonymous and request.user == car.author:
        pass
    else:
        car.seen_amount += 1
        car.save()

    if request.user == car.author:
        author = True

    context = {
        'car': car,
        'author': author,
    }

    return render(request, 'car/car_detail.html', context)


def car_update(request, pk):
    car = Car.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = CarUpdateForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("my_car")
    form = CarUpdateForm(instance=car)
    return render(request, 'car/car_update.html',
                  context={'car': car, 'form': form})


def car_delete(request, pk):
    car = Car.objects.filter(id=pk).first()
    car.delete()
    return redirect('my_cars')


def expensive_cars(request):
    cars = Car.objects.order_by('-price')
    context = {
        'cars': cars
    }
    return render(request, 'car/main_page.html', context)
