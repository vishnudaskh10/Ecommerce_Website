from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shop.models import product
from cart.models import Cart,Account,Order
from django.http import HttpResponse
@login_required
def cart_view(request):
    total=0
    try:
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total +=i.quantity*i.products.price
    except Cart.DoesNotExist:
        pass
    return render(request,'addcart.html',{'cart':cart,'total':total})

@login_required
def Addcart(request,p):
     Product=product.objects.get(id=p)
     user=request.user
     try:
        cart=Cart.objects.get(products=Product,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity += 1
        cart.save()
     except Cart.DoesNotExist:
        cart=Cart.objects.create(products=Product,user=user,quantity=1)
        cart.save()

     return redirect('cart:cart_view')

@login_required
def decreaser(request,p):
    Product = product.objects.get(id=p)
    user=request.user
    try:
      cartitem=Cart.objects.get(products=Product,user=user)
      if cartitem.quantity>1:
         cartitem.quantity-=1
         cartitem.save()
      else:
          cartitem.delete()
    except:
        pass
    return redirect('cart:cart_view')

def dele(request,p):
    Product = product.objects.get(id=p)
    user=request.user
    try:
       item= Cart.objects.get(products=Product,user=user)
       item.delete()
    except:
        pass
    return redirect('cart:cart_view')

@login_required
def accnt(request):
    total=0
    items=0
    msg=0
    if (request.method=='POST'):
        a = request.POST['a']
        ph = request.POST['p']
        ac = request.POST['num']
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total +=i.quantity*i.products.price
            items +=i.quantity
        ac = Account.objects.get(acctnumber=ac)
        if float(ac.amount) >= total:
            ac.amount = ac.amount - total
            ac.save()
            for i in cart:
                o = Order.objects.create(user=user, products=i.products, address=a, phone=ph, order_status="paid",
                                         noofitems=i.quantity)
                o.save()
            cart.delete()
            msg = "Order Placed Successfully"
            return render(request, 'orderdetail.html', {'msg': msg, 'total': total, 'items': items})
        else:
            msg = "Insufficient Amount.You can't place your order"
            return render(request, 'orderdetail.html', {'msg': msg})
    return render(request, 'accnt.html')

def orderview1(request):
    user = request.user
    o = Order.objects.filter(user=user, order_status="paid")
    return render(request,'orderview.html',{'o':o,'name':user})

# def subtotal(request):
