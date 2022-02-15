from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from allauth import *
from .send_mail import *
from .inventory_checker import *
from threading import Thread
import json

# Create your views here.


def home(request):

    return render(request, 'home.html')


def new_query(request):

    push = False
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form2 = CategoryForm(request.POST)
        if form.is_valid() and form2.is_valid():
            new2 = form2.save(commit=False)
            new2.user = request.user.email
            new = form.save(commit=False)
            new.email = request.user.email
            new.category = new2.category
            json_response = check_p(new.url)
            # print(json_response)
            # json_response = json_response.json()
            # print(json_response, '@@@@@@@@@@@@@@@@@@@@@@@@')
            if json_response['text'] != 'Sold out':
                return HttpResponseRedirect('/failed?push=True')

            new.product_name = json_response['product_name']
            new.save()
            new2.save()
            
            pcheck = Thread(target=check, args=(0, new.url, new.product_name, new.email))
            pcheck.start()
            
            # print(new.url, new.product_name)
            
            # sendMail(request.user.email, 'New Request from "Is It in Stock?"',
            #          f'Sup, \n You currently placed a query in our app, for "{new.product_name}" from target.com. \n We are currently checking the url and the product, we will send you a confirmation email when the request gets posted. \n If that was not you contact us at contact@jorgecaridad.dev')

            return HttpResponseRedirect('/currentqueries?push=True')
    else:
        form = OrderForm()
        form2 = CategoryForm()
        
        if 'push' in request.GET:
            push = True

    form = OrderForm
    form2 = CategoryForm

    return render(request, 'queries/new_query.html', {
        'form': form,
        'push': push,
        'form2': form2
    })


def new_user(request):

    push = False
    if request.method == 'POST':
        form = User

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registeruser?push=True')
    else:
        form = User()
        if 'push' in request.GET:
            push = True

    form = User

    render(request, 'queries/register_user.html', {'form': form, 'push': push})


class Current_Queries(ListView):

    def get(self, request):

        queryset = Order.objects.filter(email=request.user.email, active=True)
        queryset2 = Product.objects.filter(user=request.user.email)
        context = {'order_list': queryset, 'product_list': queryset2}
        return render(request, 'queries/current_queries.html', context)

    def post(self, request):
        push = False
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                new = form.save(commit=False)
                new.active = False
                new.save()

                return HttpResponseRedirect('/pastqueries?push=True')
        else:
            form = OrderForm()
            if 'push' in request.GET:
                push = True

        form = OrderForm
        return render(request, 'queries/past_queries.html', {
            'form': form,
            'push': push
        })


class Past_Queries(ListView):

    def get(self, request):
        queryset = Order.objects.filter(email=request.user.email, active=False)

        context = {'order_list': queryset}
        return render(request, 'queries/past_queries.html', context)
    
def faq(request):
    

    return render(request, 'faq.html')

def failed(request):
    
    return render(request, 'queries/failed.html')

def deactivate_query(request, pk):
    
    query = Order.objects.get(id=pk)
    print(pk, query)
    if request.method == "POST":
        query.active = False
        query.save()
        return redirect('/pastqueries')
    
    context = {'query':query}
    
    return render(request, 'queries/deactivate.html', context)
        
