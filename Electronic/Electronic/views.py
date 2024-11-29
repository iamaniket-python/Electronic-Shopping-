from django.shortcuts import render,redirect
from store.models import Product,Categories,Filter_price,Color,Brand,Contact
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import razorpay


client =razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))


def Index(request):

    return render(request,'main/index.html')


def Home(request):
    product= Product.objects.filter(status='Publish')

    context={
        'product':product
        
    }
    return render(request,'main/home.html',context)


def Productt(request):
    product= Product.objects.filter(status='Publish')
    categories= Categories.objects.all()
    filter_price =Filter_price.objects.all()
    color =Color.objects.all()
    brand=Brand.objects.all()


    CATID= request.GET.get('categories')
    BRANDID=request.GET.get('brand')
    COLORID=request.GET.get('color')
    PRICE_FILTER_ID =request.GET.get('filter_price')
    
    if CATID:
        product= Product.objects.filter(Category= CATID, status='publish')
    elif PRICE_FILTER_ID:
        product= Product.objects.filter(filter_price= PRICE_FILTER_ID, status='publish')
    elif COLORID:
        product= Product.objects.filter(color= COLORID, status='publish')
    elif BRANDID:
        product= Product.objects.filter(Brand= BRANDID, status='publish')
    else:
        product= Product.objects.filter(status='Publish')

    context={
        'product':product,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,

    }
    return render(request,'main/product.html',context)


def Search(request):
    qyery=request.GET.get('query')
    product= Product.objects.filter(name__icontains = qyery)
    
    context={
        'product':product
    }

    return render(request, 'main/search.html',context)
    
def Product_details(request,id):

    prod= Product.objects.filter(id=id).first()
    context={
        'prod':prod,
    }

    return render(request,'main/singleproduct.html',context)

def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(
            name=name, 
            email=email, 
            subject=subject, 
            message=message
            
        )
        subject =subject
        message = message
        from_email = settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, from_email, ['aniketsrivastava57@gmail.com'])
            contact.save()
            return redirect('contact')
        except:
            return redirect('contact')

    return render(request,'main/contact.html')
  
def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)


        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return redirect('Login')

    return render(request,'register/login.html')



def SingupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        customer= User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('Login')

    return render(request,'register/singup.html')


def LogoutPage(request):
    logout(request)
    return redirect('Home')


# ---------------------------------------------Cart----------------------------------------------------------------------------


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("Home")


@login_required(login_url="/Login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_detail.html')


def Checkout(request):
    # payment =client.order.create({
    #     'amount' : 500,
    #     'currency' : 'INR',
    #     'payment_captured':"1"
    # })     
    # order_id=payment['id']
    # context ={
    #     'order_id':order_id,
    #     'payment':payment,
    # }
    return render(request,'Cart/checkout.html')


def Placeholder(request):
    if request.method == 'POST':
        firstname =request.POST.get('firstname')
    return render(request,'Cart/placeholder.html')


def About(request):
    return render(request,'main/about.html')