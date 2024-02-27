from django.http import HttpResponse
from django.shortcuts import render
from . models import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Q

def index(request):



    return render(request , 'index.html' )


def about(request):



    return render(request , 'about.html' )




def product(request):
    search=Product.objects.all()

    name = None

    if 'search_name' in request.GET:

        name = request.GET['search_name']

        if name :

            search = search.filter(name__icontains=name)



    context = {

        'products': search

    }
    return render(request, 'product.html', context)



# def product(request):
#     query = request.GET.get('q')  # Get the query parameter 'q' from the URL
#     if query:
#         products = Product.objects.filter(Q(name__icontains=query))
#     else:
#         products = Product.objects.all()
    
#     context = {'products': products}
#     return render(request, 'product.html', context)






def why(request):



    return render(request , 'why.html' )



def testimonial(request):






    return render(request , 'testimonial.html' )





@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart , created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, user=request.user)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart')



@login_required
def cart(request):
    # Assuming your CartItem model has a foreign key to the User model named 'user'
    user_cart_items = CartItem.objects.filter(user=request.user)

    total_quantity = user_cart_items.aggregate(total=Sum('quantity'))['total'] or 0

  
    
   
     

    cart_items_count = user_cart_items

    context = {
        'cart_item': user_cart_items,
        'items_count':total_quantity
    }

    return render(request, 'cart.html', context)




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/cart')  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')



from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def custom_logout(request):
    # Perform any additional operations here (e.g., logging)
    messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
    logout(request)
    return redirect('/')  # Redirect to a desired URL
