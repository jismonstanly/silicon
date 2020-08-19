from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
import datetime
from django.core.files.storage import FileSystemStorage
import pytz

def home(request):
    return render(request,'home.html')

def customer_home(request):
    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd,ds)
    k = zip(idd, ds)
    return render(request, 'customer_home.html', {'d': d,'k':k})

def admin_home(request):
    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd, ds)
    k = zip(idd, ds)
    zx = zip(idd, ds)
    kf = zip(idd, ds)
    return render(request, 'admin_home.html', {'d': d, 'k': k,'zx':zx,'kf':kf})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        hy = Registration.objects.all()
        for i in hy:
            if i.Email == email:
                messages.success(request, 'You are already registered. Please login')
                return render(request, 'home.html')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        psw = request.POST.get('psw')
        reg = Registration()
        reg.First_name = first_name
        reg.Last_name = last_name
        reg.Email = email
        reg.Password = psw
        reg.State = state
        reg.City = city
        reg.Pincode = pincode
        reg.Address = address
        reg.Phone = phone
        reg.Lock = 'opened'
        reg.save()
        messages.success(request, 'You have successfully registered')
        return render(request, 'home.html')
    else:
        return render(request, 'register.html')

def news(request):
    page = requests.get('https://www.indiatoday.in/education-today')
    soup = BeautifulSoup(page.content,'html.parser')
    week = soup.find(class_ = 'special-top-news')
    wm = week.find(class_ = 'itg-listing')
    w = wm.find_all('a')
    ww = []
    for x in w:
        ww.append(x.get_text())
    x = datetime.datetime.now()
    return render(request,'news.html',{'ww':ww,'x':x})


def login(request):
    if request.method == 'POST':
        username = request.POST.get("email")
        password = request.POST.get("pword")
        if (Registration.objects.filter(Email=username, Password=password).exists()):
            regs = Registration.objects.filter(Email=username, Password=password)
            for value in regs:
                user_id = value.id
                usertype  = value.Email
                lck = value.Lock
                pwd = value.Password
                if usertype == 'admin@gmail.com' and pwd == 'admin123':
                    request.session['logg'] = user_id
                    dd = Category_product.objects.all()
                    idd = []
                    ds = []
                    for i in dd:
                        if i.Category_name not in ds:
                            ds.append(i.Category_name)
                            idd.append(i.id)
                    d = zip(idd, ds)
                    k = zip(idd, ds)
                    zx = zip(idd, ds)
                    kf = zip(idd, ds)
                    return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
                elif str(lck) == 'blocked':
                    messages.success(request, 'Your account is blocked')
                    return render(request, 'login.html')
                else:
                    request.session['logg'] = user_id
                    dd = Category_product.objects.all()
                    idd = []
                    ds = []
                    for i in dd:
                        if i.Category_name not in ds:
                            ds.append(i.Category_name)
                            idd.append(i.id)
                    d = zip(idd, ds)
                    k = zip(idd, ds)
                    return render(request, 'customer_home.html', {'d': d, 'k': k})
        else:
            messages.success(request, 'Email or password entered is incorrect')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    if 'logg' in request.session:
        del request.session['logg']
        return render(request,'home.html')
    return render(request, 'home.html')

def add_product(request, id):
    id = int(id)
    c = Category_product.objects.get(id = id)
    if request.method == 'POST':
        nam = request.POST.get('nam')
        cv = Category_product.objects.all()
        for i in cv:
            k = str(i.Product_name)
            if k == str(nam):
                messages.success(request, 'Product already exists')
                return render(request, 'add_product.html',{'c':c})
        min_q = request.POST.get('min_q')
        max_q = request.POST.get('max_q')
        disc = request.POST.get('disc')
        price = request.POST.get('price')
        actt = request.POST.get('actt')
        photo1 = request.FILES['photo1']
        fs = FileSystemStorage()
        fs.save(photo1.name, photo1)
        b = Category_product()
        b.Category_name = c.Category_name
        b.Product_image = photo1
        b.Product_name = nam
        b.Minimum_quantity = min_q
        b.Maximum_quantity = max_q
        b.Discount_percentage = disc
        b.Unit_price = price
        b.Status = actt
        b.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'Product added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'add_product.html',{'c':c})

def nfs(request):
    if request.method == 'POST':
        font = request.POST.get('font')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Font_name)
            if k == str(font):
                messages.success(request, 'Font style already exists')
                return render(request, "new_font_style.html")
        a = Band_details()
        a.Size_in_inch = 0.0
        a.Style = ''
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = font
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New font style added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_font_style.html')


def nbs(request):
    if request.method == 'POST':
        band_style = request.POST.get('band_style')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Style)
            if k == str(band_style):
                messages.success(request, 'Band style already exists')
                return render(request, "new_band_style.html")
        a = Band_details()
        a.Size_in_inch = 0
        a.Style = band_style
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'Band style added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request,'new_band_style.html')

def new_category(request):
    if request.method == 'POST':
        cat = request.POST.get('cat')
        actt = request.POST.get('actt')
        a = Category_product()
        a.Product_name = ''
        a.Product_image = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0
        a.Unit_price = 0
        a.Category_name = cat
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New category added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_category.html')

def new_band_size(request):
    if request.method == 'POST':
        band_size = request.POST.get('band_size')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = float(i.Size_in_inch)
            if k == float(band_size):
                messages.success(request, 'Band size already exists')
                return render(request, "new_band_size.html")
        a = Band_details()
        a.Size_in_inch = band_size
        a.Style = ''
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New band size added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_band_size.html')

def new_clipart(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)
        clippart = request.POST.get('clippart')
        actt = request.POST.get('actt')

        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Clipart_name)
            if k == str(clippart):
                messages.success(request, 'Clipart already exists')
                return render(request, "new_clipart.html")

        a = Band_details()
        a.Size_in_inch = 0
        a.Style = ''
        a.Clipart_name = clippart
        a.Clipart_image = photo
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New clipart added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_clipart.html')

def new_ship(request):

    if request.method == 'POST':
        day = request.POST.get('day')
        desc = request.POST.get('desc')
        cost = request.POST.get('cost')
        actt = request.POST.get('actt')
        cv = Conveyance_fees.objects.all()
        for i in cv:
            k = float(i.Shipping_cost)
            if k == float(cost):
                messages.success(request, 'Shipping cost already exists')
                return render(request, "new_ship.html")
        a = Conveyance_fees()
        a.Delivery_charge_min_km = 0
        a.Delivery_charge_max_km = 0
        a.Delivery_fees = 0
        a.Shipping_days = day
        a.Shipping_description = desc
        a.Shipping_cost = cost
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New shipping details added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_ship.html')


def new_delivery(request):
    if request.method == 'POST':
        Minimum_kilometer = request.POST.get('Minimum_kilometer')
        Maximum_kilometer = request.POST.get('Maximum_kilometer')
        huh = Conveyance_fees.objects.all()
        for i in huh:
            if i.Delivery_charge_min_km == int(Minimum_kilometer) and i.Delivery_charge_max_km == int(Maximum_kilometer):
                messages.success(request, 'Kilometer range already exists')
                return render(request, 'new_delivery.html')
        price = request.POST.get('price')
        actt = request.POST.get('actt')
        a = Conveyance_fees()
        a.Shipping_days = 0
        a.Shipping_description = ''
        a.Shipping_cost = 0
        a.Delivery_charge_min_km = Minimum_kilometer
        a.Delivery_charge_max_km = Maximum_kilometer
        a.Delivery_fees = price
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New delivery details added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_delivery.html')

def new_price(request):
    bsi = Band_details.objects.all()
    b_s = []
    b_st = []
    for y in bsi:
        if (y.Size_in_inch not in b_s) and (y.Size_in_inch != 0):
            b_s.append(y.Size_in_inch)
        if (y.Style not in b_st) and (y.Style != ''):
            b_st.append(y.Style)

    if request.method == 'POST':
        bd_s = request.POST.get('bd_s')
        bd_st = request.POST.get('bd_st')
        mi_qq = request.POST.get('mi_q')
        ma_qq = request.POST.get('ma_q')
        pricee = request.POST.get('price')
        discc = request.POST.get('disc')
        acttt = request.POST.get('actt')
        a = Band_details()
        a.Style = bd_st
        a.Size_in_inch = bd_s
        a.Clipart_name = ''
        a.Clipart_image = ''
        a.Font_name = ''
        a.Maximum_quantity = ma_qq
        a.Minimum_quantity = mi_qq
        a.Discount_percentage = discc
        a.Unit_price = pricee
        a.Status = acttt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'New price added')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'new_price.html',{'b_s':b_s,'b_st':b_st})

def view_prdct_cus(request, id, idg):
    idg = str(idg)
    request.session["cataa_name"] = idg
    id = int(id)
    request.session["catt_id"] = id
    z = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '')
    zz = str()
    for p in z:
        zz+=p.Category_name
        zz = str(zz)
        zz = zz.upper()
        request.session["cata_name"] = zz
        break
    try:
        n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '')
        return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz})
    except:
        return render(request, 'view_prdct_cus.html')

def ord_product(request):
    zz = request.session["cata_name"]
    idg = request.session["cataa_name"]
    request.session['cart_product'] = cart = request.POST.getlist('cart')
    try:
        request.session['quantity'] = qqn = request.POST.getlist('quantity')
    except:
        try:
            n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '',Unit_price = 0)
            messages.success(request, 'Please enter quantity required')
            return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz})
        except:
            return render(request, 'view_prdct_cus.html')

    while ("" in qqn):
        qqn.remove("")
    request.session['quantity'] = qqn
    qse = len(cart)
    qvs = len(qqn)
    if int(qse) < int(qvs):
        try:
            n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '',Unit_price = 0)
            messages.success(request, 'Please enter selected item to cart')
            return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz})
        except:
            return render(request, 'view_prdct_cus.html')

    if int(qse) != int(qvs):
        try:
            n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '',Unit_price = 0)
            messages.success(request, 'Please enter quantity required')
            return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz})
        except:
            return render(request, 'view_prdct_cus.html')
    Idd = []
    Image_namme = []
    Product_namme = []
    Pprice = []
    quantity = []
    for i in cart:
        i = int(i)
        vb = Category_product.objects.get(id = i)
        Idd.append(vb.id)
        Image_namme.append(vb.Product_image)
        Product_namme.append(vb.Product_name)
        Pprice.append(vb.Unit_price)
    for u in qqn:
        quantity.append(u)
    request.session['checkouts'] = Idd
    bm = zip(Idd, Image_namme, Product_namme, Pprice, quantity)
    bt = zip(Pprice, quantity)
    mz = 0
    mzm = []
    for i,j in bt:
        bp = int(i) * int(j)
        mz = mz + (int(i) * int(j))
        mzm.append(bp)
    request.session["indivi_price"] = mzm
    request.session["tot_price"] = mz
    return render(request,'checkout.html',{'bm':bm})

def Remove_order(request, id, idm, idt):
    cart = request.session['cart_product']
    qqn = request.session['quantity']
    th = request.session["tot_price"]
    idr = float(idm) * float(idt)
    thh = float(th) - float(idr)
    request.session["tot_price"] = thh
    cart.remove(id)
    qqn.remove(idm)
    Idd = []
    Image_namme = []
    Product_namme = []
    Pprice = []
    quantity = []
    for i in cart:
        vb = Category_product.objects.get(id=i)
        Idd.append(vb.id)
        Image_namme.append(vb.Product_image)
        Product_namme.append(vb.Product_name)
        Pprice.append(vb.Unit_price)
    for u in qqn:
        quantity.append(u)
    request.session['checkouts'] = Idd
    request.session['quantity'] = qqn
    bm = zip(Idd, Image_namme, Product_namme, Pprice, quantity)
    return render(request, 'checkout.html', {'bm': bm})

def ord_cus_band(request):
    b_det = Band_details.objects.all()
    min_qu = []
    max_qu = []
    dis_p = []
    b_st = []
    act = []
    ght2 = zip(b_st,act)
    b_s = []
    act1 = []
    ght1 = zip(b_s,act1)
    f_nam = []
    act2 = []
    ght = zip(f_nam,act2)
    clip = []
    clip_img = []
    cll = zip(clip,clip_img)
    pricd = []

    for g in b_det:
        if (g.Style not in b_st) and (g.Style != ''):
            b_st.append(g.Style)
            act.append(g.Status)
        if (g.Size_in_inch not in b_s) and (g.Size_in_inch != 0):
            b_s.append(g.Size_in_inch)
            act1.append(g.Status)
        if (g.Font_name not in f_nam) and (g.Font_name != ''):
            f_nam.append(g.Font_name)
            act2.append(g.Status)
        if (g.Clipart_name not in clip) and (g.Clipart_name != ''):
            clip.append(g.Clipart_name)
        if (g.Clipart_image not in clip) and (g.Clipart_image != ''):
            clip_img.append(g.Clipart_image)
        if (g.Unit_price not in pricd) and (g.Unit_price != 0):
            pricd.append(g.Unit_price)
            min_qu.append(g.Minimum_quantity)
            max_qu.append(g.Maximum_quantity)
            dis_p.append(g.Discount_percentage)
    bb_det = zip(b_s, b_st, min_qu, max_qu, dis_p, pricd)

    deli = Conveyance_fees.objects.all()
    if request.method == 'POST':
        f_ss = request.POST.get('f_ss')
        b_ss = request.POST.get('b_ss')
        b_stt = request.POST.get('b_stt')
        clipp = request.POST.get('clipp')
        quan = request.POST.get('quan')
        f_mes = request.POST.get('f_mes')
        b_mes = request.POST.get('b_mes')
        collr = request.POST.get('collr')
        m = Registration.objects.get(id = request.session['logg'])
        ctt = Cust_cart()
        ctt.Front_message = f_mes
        ctt.Back_message = b_mes
        ctt.Color = collr
        ctt.Fon_style = f_ss
        ctt.Ban_size = b_ss
        ctt.Ban_style = b_stt
        ctt.Clippart_name = clipp
        ctt.QQuantity = quan
        ctt.Delivery_charge = 0.0
        for i in b_det:
            mw = i.Size_in_inch
            mp = i.Style
            if float(b_ss) == float(mw) and mp == b_stt and i.Unit_price != 0:
                bcb = i.Unit_price
                bc = int(bcb)
                if int(quan) >= int(i.Minimum_quantity) and int(quan) <= int(i.Maximum_quantity):
                    ctt.Pricce = i.Unit_price
                    bgb = int(quan)
                    km = bc * bgb
                    kmm = (float(i.Discount_percentage)/100.0) * int(km)
                    kdf = km - kmm
                    kdd = round(kdf,2)
                    ctt.Total_amount = kdd
                    ctt.regg = m
                    ctt.save()
                    messages.success(request, 'The item has been added to cart')
                    return render(request, 'ord_cus_band.html', {'bb_det':bb_det,'ght2':ght2,'ght1':ght1,'ght':ght,'clip':clip,
                                                                 'clip_img':clip_img,'pricd':pricd,'b_det':b_det,'cll':cll,'deli':deli})
                else:
                    ctt.Pricce = i.Unit_price
                    bgb = int(quan)
                    km = bc*bgb
                    ctt.Total_amount = km
                    ctt.regg = m
                    ctt.save()
                    messages.success(request, 'The item has been added to cart')
                    return render(request, 'ord_cus_band.html',{'bb_det':bb_det,'ght2':ght2,'ght1':ght1,'ght':ght,'clip':clip,
                                                                 'clip_img':clip_img,'pricd':pricd,'b_det':b_det,'cll':cll,'deli':deli})
        messages.success(request, 'Your suggested specification cannot been made..Please try another')
        return render(request, 'ord_cus_band.html', {'bb_det':bb_det,'ght2':ght2,'ght1':ght1,'ght':ght,'clip':clip,
                                                                 'clip_img':clip_img,'pricd':pricd,'b_det':b_det,'cll':cll,'deli':deli})
    else:
        return render(request, 'ord_cus_band.html', {'bb_det':bb_det,'ght2':ght2,'ght1':ght1,'ght':ght,
                                                     'clip':clip,'clip_img':clip_img,'pricd':pricd,'b_det':b_det,'cll':cll,'deli':deli})

def view_cart(request):
    b = Cust_cart.objects.filter(regg = request.session["logg"])
    g = Band_details.objects.all()
    gt ='20px'
    return render(request,'view_cart.html',{'b':b,'g':g,'gt':gt})

def delete_cart(request, id):
    Cust_cart.objects.get(id = id).delete()
    g = Band_details.objects.all()
    b = Cust_cart.objects.filter(regg = request.session["logg"])
    return render(request, 'view_cart.html', {'b': b,'g':g})

def checkout_cus_band(request):
    b = Cust_cart.objects.filter(regg = request.session["logg"])
    m = 0.0
    for i in b:
        n = float(i.Total_amount)
        m+=n

    if request.method == 'POST':
        amt = request.POST.get('amt')
        if float(amt) < float(m):
            messages.success(request, 'Please pay full amount')
            return render(request,'checkout_cus_band.html',{'m':m})
        for i in b:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            state = request.POST.get('state')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            s = Band_order()
            s.First_name = first_name
            s.Last_name = last_name
            s.Email = email
            s.Phone = phone
            s.State = state
            s.City = city
            s.Pincode = pincode
            s.Address = address
            s.Front_message = i.Front_message
            s.Back_message = i.Back_message
            s.Color = i.Color
            s.Fonts_style = i.Fon_style
            s.Bandd_size = i.Ban_size
            s.Bandd_style = i.Ban_style
            s.Clipartt_name = i.Clippart_name
            s.Quantitty = i.QQuantity
            s.Pricee = i.Pricce
            s.Totall_amount = i.Total_amount
            s.Order_status = "To be expected"
            s.save()
        Cust_cart.objects.filter(regg = request.session["logg"]).delete()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        messages.success(request, 'Order has been placed successfully')
        return render(request, 'customer_home.html', {'d': d, 'k': k})
    return render(request,'checkout_cus_band.html',{'m':m})

def ch_out(request):
    tot_pri = request.session["tot_price"]
    return render(request,'delivery_addr_product.html',{'tot_pri':tot_pri})

def ch_out1(request):
    tot_pri = request.session["tot_price"]
    amt = request.POST.get('amt')
    tot = request.session["tot_price"]
    if float(amt) < float(tot):
        messages.success(request, 'Please pay in full')
        return render(request, 'delivery_addr_product.html',{'tot_pri':tot_pri})
    qq = request.session['quantity']
    q = request.session['checkouts']
    nbn = zip(q,qq)
    for i,j in nbn:
        i = int(i)
        mb = Category_product.objects.get(id = i)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        Category_name = mb.Category_name
        product_name = mb.Product_name
        pricc = mb.Unit_price
        s = Pre_order()
        s.First_name = first_name
        s.Last_name = last_name
        s.Email = email
        s.Phone = phone
        s.State = state
        s.City = city
        s.Pincode = pincode
        s.Address = address
        s.Category_name = Category_name
        s.Product_name = product_name
        s.Price = pricc

        if int(j) >= int(mb.Minimum_quantity) and int(j) <= int(mb.Maximum_quantity):
            bgb = float(j)
            bc = float(mb.Unit_price)
            km = bc * bgb
            kmm = (float(mb.Discount_percentage)/100.0) * float(km)
            kdf = km - kmm
            kdd = round(kdf,2)
            s.Total_amount = kdd
            s.Quantity = bgb
            s.Order_status = "To be expected"
            s.save()
        else:
            bgb = float(j)
            bc = float(mb.Unit_price)
            km = bc * bgb
            km = float(km)
            kdd = round(km, 2)
            s.Total_amount = kdd
            s.Quantity = bgb
            s.Order_status = "To be expected"
            s.save()

    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd, ds)
    k = zip(idd, ds)
    messages.success(request, 'Order has been placed successfully')
    return render(request, 'customer_home.html', {'d': d, 'k': k})

def view_product(request, id):
    id = str(id)
    request.session["cat_id"] = id
    z = Category_product.objects.filter(Category_name=request.session["cat_id"]).exclude(Product_name='')
    zz = str()
    for p in z:
        zz += p.Category_name
        zz = str(zz)
        zz = zz.upper()
        request.session["ctt_name"] = zz
        break
    try:
        n = Category_product.objects.filter(Category_name = request.session["cat_id"]).exclude(Product_name = '')
        return render(request, 'view_product.html',{'n':n,'zz':zz})
    except:
        return render(request, 'view_product.html')

def view_category(request):

    try:
        bb = Category_product.objects.all()
        idd = []
        c_n = []
        st = []
        for w in bb:
            if (w.Category_name not in c_n):
                idd.append(w.id)
                c_n.append(w.Category_name)
                st.append(w.Status)
        b = zip(idd,c_n,st)
        return render(request,'view_category.html',{'b':b})
    except:
        return render(request,'view_category.html')

def view_band_size(request):
    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Size_in_inch not in sii) and (w.Size_in_inch != 0):
                idd.append(w.id)
                sii.append(w.Size_in_inch)
                st.append(w.Status)
        b = zip(idd,sii,st)
        return render(request, 'view_band_size.html',{'b':b})
    except:
        return render(request, 'view_band_size.html')


def view_font_style(request):
    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Font_name not in sii) and (w.Font_name != ''):
                idd.append(w.id)
                sii.append(w.Font_name)
                st.append(w.Status)
        b = zip(idd, sii, st)
        return render(request, 'view_font_style.html', {'b': b})
    except:
        return render(request, 'view_font_style.html')



def view_clipart(request):

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Clipart_name not in sii) and (w.Clipart_name != ''):
                idd.append(w.id)
                sii.append(w.Clipart_name)
                st.append(w.Clipart_image)
        b = zip(idd,sii,st)
        return render(request, 'view_clipart.html',{'b':b})
    except:
        return render(request, 'view_clipart.html')


def view_band_style(request):

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Style not in sii) and (w.Style != ''):
                idd.append(w.id)
                sii.append(w.Style)
                st.append(w.Status)
        b = zip(idd,sii,st)
        return render(request, 'view_band_style.html',{'b':b})
    except:
        return render(request, 'view_band_style.html')


def view_price(request):
    try:
        bb = Band_details.objects.all()
        idd = []
        stt = []
        sii = []
        maxx = []
        minn = []
        pricc = []
        disc = []
        st = []
        for w in bb:
            if (w.Style != '') and (w.Unit_price != 0):
                idd.append(w.id)
                stt.append(w.Style)
                sii.append(w.Size_in_inch)
                maxx.append(w.Maximum_quantity)
                minn.append(w.Minimum_quantity)
                pricc.append(w.Unit_price)
                disc.append(w.Discount_percentage)
                st.append(w.Status)
        b = zip(idd, stt, sii, minn, maxx, pricc, disc)
        return render(request, 'view_band_price.html', {'b': b})
    except:
        return render(request, 'view_band_price.html')



def view_ship(request):
    try:
        b = Conveyance_fees.objects.all()
        return render(request, 'view_ship.html', {'b': b})
    except:
        return render(request, 'view_ship.html')

def view_delivery(request):
    try:
        b = Conveyance_fees.objects.all()
        return render(request, 'view_delivery.html', {'b': b})
    except:
        return render(request, 'view_delivery.html')

def band_cust_orders(request):
    if request.method == 'POST':
        status = request.POST.getlist('status')
        idd = request.POST.getlist('idd')
        idm = []
        for i in idd:
            n = int(i)
            idm.append(n)
        st_id = zip(idm,status)
        for k,j in st_id:
            try:
                f = Band_order.objects.get(id = k)
                f.Order_status = j
                f.save()
            except:
                try:
                    b = Band_order.objects.all()
                    return render(request, 'view_band_order.html', {'b': b})
                except:
                    return render(request, 'view_band_order.html')

    try:
        b = Band_order.objects.all()
        mm = Band_details.objects.all()
        return render(request, 'view_band_order.html', {'b': b,'mm':mm})
    except:
        return render(request, 'view_band_order.html')

def delete_band_cust_orders(request):
    prr = Band_order.objects.all()
    mm = Band_details.objects.all()
    return render(request, 'delete_band_cust_orders.html', {'prr': prr,'mm':mm})

def delete_cust_band_orders(request, id):
    Band_order.objects.get(id=id).delete()
    prr = Band_order.objects.all()
    mm = Band_details.objects.all()
    return render(request, 'delete_band_cust_orders.html', {'prr':prr,'mm':mm})

def pre_orders(request):
    if request.method == 'POST':
        status = request.POST.getlist('status')
        idd = request.POST.getlist('idd')
        idm = []
        for i in idd:
            n = int(i)
            idm.append(n)
        st_id = zip(idd,status)
        for k,j in st_id:
            try:
                f = Pre_order.objects.get(id = k)
                f.Order_status = j
                f.save()
            except:
                try:
                    b = Pre_order.objects.all()
                    return render(request, 'view_pre_order.html', {'b': b})
                except:
                    return render(request, 'view_pre_order.html')

    try:
        b = Pre_order.objects.all()
        return render(request, 'view_pre_order.html', {'b': b})
    except:
        return render(request, 'view_pre_order.html')

def delete_pre_orders(request):
    prr = Pre_order.objects.all()
    return render(request,'delete_pre_orders.html',{'prr':prr})

def delete_pre_orderss(request, id):
    Pre_order.objects.get(id=id).delete()
    prr = Pre_order.objects.all()
    return render(request, 'delete_pre_orders.html', {'prr':prr})


def edit_category(request, id):
    id = int(id)
    b = Category_product.objects.get(id=id)
    if request.method == 'POST':
        cat = request.POST.get('cat')
        huh = Category_product.objects.exclude(id=id)
        for i in huh:
            if i.Category_name == cat:
                try:
                    bb = Category_product.objects.all()
                    idd = []
                    c_n = []
                    st = []
                    for w in bb:
                        if (w.Category_name not in c_n):
                            idd.append(w.id)
                            c_n.append(w.Category_name)
                            st.append(w.Status)
                    b = zip(idd, c_n, st)
                    messages.success(request, 'Category already exists')
                    return render(request, 'view_category.html', {'b': b})
                except:
                    messages.success(request, 'Category already exists')
                    return render(request, 'view_category.html')
        actt = request.POST.get('actt')
        b.Category_name = cat
        b.Product_name = ''
        b.Product_image = ''
        b.Unit_price = 0
        b.Status = actt
        b.save()

        try:
            bb = Category_product.objects.all()
            idd = []
            c_n = []
            st = []
            for w in bb:
                if (w.Category_name not in c_n):
                    idd.append(w.id)
                    c_n.append(w.Category_name)
                    st.append(w.Status)
            b = zip(idd, c_n, st)
            messages.success(request, 'Category edited')
            return render(request, 'view_category.html', {'b': b})
        except:
            return render(request, 'view_category.html')
    return render(request, 'edit_category.html', {'b': b})

def edit_product(request, id):
    zz = request.session["ctt_name"]
    b = Category_product.objects.get(id=id)
    if request.method == 'POST':
        pro_n = request.POST.get('pro_n')
        pro_p = request.POST.get('pro_p')
        min_q = request.POST.get('min_q')
        max_q = request.POST.get('max_q')
        disc = request.POST.get('disc')
        huh = Category_product.objects.exclude(id=id)
        for i in huh:
            if i.Product_name == pro_n:
                z = Category_product.objects.filter(Category_name=request.session["cat_id"]).exclude(Product_name='')
                zz = str()
                for p in z:
                    zz += p.Category_name
                    zz = str(zz)
                    zz = zz.upper()
                    request.session["ctt_name"] = zz
                    break
                try:
                    n = Category_product.objects.filter(Category_name=request.session["cat_id"]).exclude(Product_name='')
                    messages.success(request, 'Product already exists')
                    return render(request, 'view_product.html', {'n': n, 'zz': zz})
                except:
                    messages.success(request, 'Product already exists')
                    return render(request, 'view_product.html')
        b.Product_name = pro_n
        b.Unit_price = pro_p
        b.Minimum_quantity = min_q
        b.Maximum_quantity = max_q
        b.Discount_percentage = disc
        b.save()
        try:
            n = Category_product.objects.filter(Category_name = request.session["cat_id"]).exclude(Product_name = '')
            messages.success(request, 'Product edited')
            return render(request, 'view_product.html', {'n': n,'zz':zz})
        except:
            return render(request, 'view_product.html')
    return render(request, 'edit_product.html', {'b': b,'zz':zz})

def edit_band_size(request, id):
    id = int(id)
    b = Band_details.objects.get(id=id)
    if request.method == 'POST':
        bandd_size = request.POST.get('bandd_size')
        actt = request.POST.get('actt')
        b.Size_in_inch = bandd_size
        b.Status = actt
        b.save()

        try:
            bb = Band_details.objects.all()
            idd = []
            sii = []
            st = []
            for w in bb:
                if (w.Size_in_inch not in sii) and (w.Size_in_inch != 0):
                    idd.append(w.id)
                    sii.append(w.Size_in_inch)
                    st.append(w.Status)
            b = zip(idd, sii, st)
            messages.success(request, 'Band size edited')
            return render(request, 'view_band_size.html', {'b': b})
        except:
            return render(request, 'view_band_size.html')
    return render(request, 'edit_band_size.html', {'b': b})

def edit_band_style(request, id):
    id = int(id)
    b = Band_details.objects.get(id=id)
    if request.method == 'POST':
        bandd_style = request.POST.get('bandd_style')
        actt = request.POST.get('actt')
        b.Style = bandd_style
        b.Status = actt
        b.save()

        try:
            bb = Band_details.objects.all()
            idd = []
            sii = []
            st = []
            for w in bb:
                if (w.Style not in sii) and (w.Style != ''):
                    idd.append(w.id)
                    sii.append(w.Style)
                    st.append(w.Status)
            b = zip(idd, sii, st)
            messages.success(request, 'Band style edited')
            return render(request, 'view_band_style.html', {'b': b})
        except:
            return render(request, 'view_band_style.html')
    return render(request, 'edit_band_style.html', {'b': b})

def edit_font_style(request, id):
    id = int(id)
    b = Band_details.objects.get(id = id)
    if request.method == 'POST':
        font = request.POST.get('font')
        huh = Band_details.objects.exclude(id=id)
        for i in huh:
            if i.Font_name == font:
                try:
                    bb = Band_details.objects.all()
                    idd = []
                    sii = []
                    st = []
                    for w in bb:
                        if (w.Font_name not in sii) and (w.Font_name != ''):
                            idd.append(w.id)
                            sii.append(w.Font_name)
                            st.append(w.Status)
                    b = zip(idd, sii, st)
                    messages.success(request, 'Font name already exists')
                    return render(request, 'view_font_style.html', {'b': b})
                except:
                    messages.success(request, 'Font name already exists')
                    return render(request, 'view_font_style.html')
        actt = request.POST.get('actt')
        b.Font_name = font
        b.Status = actt
        b.save()

        try:
            bb = Band_details.objects.all()
            idd = []
            sii = []
            st = []
            for w in bb:
                if (w.Font_name not in sii) and (w.Font_name != ''):
                    idd.append(w.id)
                    sii.append(w.Font_name)
                    st.append(w.Status)
            b = zip(idd, sii, st)
            messages.success(request, 'Font style edited')
            return render(request, 'view_font_style.html', {'b': b})
        except:
            messages.success(request, 'Font style edited')
            return render(request, 'view_font_style.html')
    return render(request, 'edit_font_style.html', {'b': b})

def edit_ship(request, id):
    id = int(id)
    b = Conveyance_fees.objects.get(id=id)
    if request.method == 'POST':
        Shipping_days = request.POST.get('Shipping_days')
        desc = request.POST.get('desc')
        Cost = request.POST.get('Cost')
        actt = request.POST.get('actt')
        b.Shipping_days = Shipping_days
        b.Shipping_description = desc
        b.Shipping_cost = Cost
        b.Status = actt
        b.save()

        try:
            b = Conveyance_fees.objects.all()
            messages.success(request, 'Shipping details edited')
            return render(request, 'view_ship.html', {'b': b})
        except:
            messages.success(request, 'Shipping details edited')
            return render(request, 'view_ship.html')
    return render(request, 'edit_ship.html', {'b': b})

def edit_delivery(request, id):
    b = Conveyance_fees.objects.get(id=id)
    if request.method == 'POST':
        Minimum_kilometer = request.POST.get('Minimum_kilometer')
        Maximum_kilometer = request.POST.get('Maximum_kilometer')
        huh = Conveyance_fees.objects.exclude(id = id)
        for i in huh:
            if i.Delivery_charge_min_km == int(Minimum_kilometer) and i.Delivery_charge_max_km == int(Maximum_kilometer):
                try:
                    b = Conveyance_fees.objects.all()
                    messages.success(request, 'Kilometer range already exists')
                    return render(request, 'view_delivery.html', {'b': b})
                except:
                    messages.success(request, 'Kilometer range already exists')
                    return render(request, 'view_delivery.html')

        price = request.POST.get('price')
        actt = request.POST.get('actt')
        b.Delivery_charge_min_km = Minimum_kilometer
        b.Delivery_charge_max_km = Maximum_kilometer
        b.Delivery_fees = price
        b.Status = actt
        b.save()

        b = Conveyance_fees.objects.all()
        messages.success(request, 'Delivery details edited')
        return render(request, 'view_delivery.html', {'b': b})
    return render(request, 'edit_delivery.html', {'b': b})

def edit_band_price(request, id):
    id = int(id)
    b = Band_details.objects.get(id = id)
    if request.method == 'POST':
        bs = request.POST.get('bs')
        bst = request.POST.get('bst')
        Maximum_quantity = request.POST.get('Maximum_quantity')
        Minimum_quantity = request.POST.get('Minimum_quantity')
        price = request.POST.get('price')
        disc = request.POST.get('disc')
        actt = request.POST.get('actt')
        b.Size_in_inch = bs
        b.Style = bst
        b.Minimum_quantity = Minimum_quantity
        b.Maximum_quantity = Maximum_quantity
        b.Unit_price = price
        b.Discount_percentage = disc
        b.Status = actt
        b.save()
        try:
            bb = Band_details.objects.all()
            idd = []
            stt = []
            sii = []
            maxx = []
            minn = []
            pricc = []
            disc = []
            st = []
            for w in bb:
                if (w.Style != '') and (w.Unit_price != 0):
                    idd.append(w.id)
                    stt.append(w.Style)
                    sii.append(w.Size_in_inch)
                    maxx.append(w.Maximum_quantity)
                    minn.append(w.Minimum_quantity)
                    pricc.append(w.Unit_price)
                    disc.append(w.Discount_percentage)
                    st.append(w.Status)
            b = zip(idd, stt, sii, minn, maxx, pricc, disc)
            messages.success(request, 'Band price edited')
            return render(request, 'view_band_price.html', {'b': b})
        except:
            messages.success(request, 'Band price edited')
            return render(request, 'view_band_price.html')
    return render(request, 'edit_band_price.html',{'b':b})


def delete_category(request, id):
    Category_product.objects.get(id=id).delete()
    try:
        bb = Category_product.objects.all()
        idd = []
        c_n = []
        st = []
        for w in bb:
            if (w.Category_name not in c_n):
                idd.append(w.id)
                c_n.append(w.Category_name)
                st.append(w.Status)
        b = zip(idd,c_n,st)
        messages.success(request, 'Category removed')
        return render(request, 'view_category.html',{'b':b})
    except:
        return render(request, 'view_category.html')

def delete_product(request, id):
    zz = request.session["ctt_name"]
    Category_product.objects.get(id = id).delete()
    try:
        n = Category_product.objects.filter(Category_name = request.session["cat_id"]).exclude(Product_name = '')
        return render(request, 'view_product.html', {'n': n,'zz':zz})
    except:
        return render(request, 'view_product.html')

def delete_band_size(request, id):
    id = int(id)
    jk = Band_details.objects.get(id=id)
    jk.Size_in_inch = 0
    jk.save()
    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Size_in_inch not in sii) and (w.Size_in_inch != 0):
                idd.append(w.id)
                sii.append(w.Size_in_inch)
                st.append(w.Status)
        b = zip(idd,sii,st)
        messages.success(request, 'Band size deleted')
        return render(request, 'view_band_size.html',{'b':b})
    except:
        return render(request, 'view_band_size.html')

def delete_band_style(request, id):

    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Style = ''
    kj.save()

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Style not in sii) and (w.Style != ''):
                idd.append(w.id)
                sii.append(w.Style)
                st.append(w.Status)
        b = zip(idd,sii,st)
        messages.success(request, 'Band style deleted')
        return render(request, 'view_band_style.html',{'b':b})
    except:
        return render(request, 'view_band_style.html')


def delete_band_price(request, id):
    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Minimum_quantity = 0
    kj.Maximum_quantity = 0
    kj.Discount_percentage = 0
    kj.Unit_price = 0
    kj.save()
    try:
        bb = Band_details.objects.all()
        idd = []
        stt = []
        sii = []
        maxx = []
        minn = []
        pricc = []
        disc = []
        st = []
        for w in bb:
            if (w.Style != '') and (w.Unit_price != 0):
                idd.append(w.id)
                stt.append(w.Style)
                sii.append(w.Size_in_inch)
                maxx.append(w.Maximum_quantity)
                minn.append(w.Minimum_quantity)
                pricc.append(w.Unit_price)
                disc.append(w.Discount_percentage)
                st.append(w.Status)
        b = zip(idd, stt, sii, minn, maxx, pricc, disc)
        return render(request, 'view_band_price.html', {'b': b})
    except:
        return render(request, 'view_band_price.html')

def delete_font_style(request, id):
    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Font_name = ''
    kj.save()

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Font_name not in sii) and (w.Font_name != ''):
                idd.append(w.id)
                sii.append(w.Font_name)
                st.append(w.Status)
        b = zip(idd, sii, st)
        messages.success(request, 'Font style deleted')
        return render(request, 'view_font_style.html', {'b': b})
    except:
        return render(request, 'view_font_style.html')



def delete_clipart(request, id):
    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Clipart_name = ''
    kj.Clipart_image = ''
    kj.save()


    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Clipart_name not in sii) and (w.Clipart_name != ''):
                idd.append(w.id)
                sii.append(w.Clipart_name)
                st.append(w.Clipart_image)
        b = zip(idd,sii,st)
        messages.success(request, 'Clipart deleted')
        return render(request, 'view_clipart.html',{'b':b})
    except:
        return render(request, 'view_clipart.html')


def delete_ship(request, id):
    id = int(id)
    kj = Conveyance_fees.objects.get(id=id)
    kj.Shipping_days = 0
    kj.Shipping_description = ''
    kj.Shipping_cost = 0
    kj.save()

    try:
        b = Conveyance_fees.objects.all()
        return render(request, 'view_ship.html', {'b': b})
    except:
        return render(request, 'view_ship.html')



def delete_delivery(request, id):
    Conveyance_fees.objects.get(id=id).delete()
    b = Conveyance_fees.objects.all()
    return render(request, 'view_delivery.html', {'b': b})

def feedback(request):
    dd = Registration.objects.get(id = request.session['logg'])
    if request.method == 'POST':
        text_feed = request.POST.get('text_feed')
        qw = Feedback()
        a = str(dd.First_name)
        b = str(dd.Last_name)
        qw.Name =  a+' '+b
        qw.Email = dd.Email
        qw.Content = text_feed
        qw.Category = 'Customer'
        qw.save()
        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        messages.success(request, 'Thank you for your valuable feedback')
        return render(request, 'customer_home.html', {'d': d, 'k': k})
    return render(request,'feedback.html',{'dd':dd})

def feedbak(request):
    se = Feedback.objects.all()
    return render(request,'feedbak.html',{'se':se})

def delete_feedback(request, id):
    Feedback.objects.get(id=id).delete()
    se = Feedback.objects.all()
    return render(request, 'feedbak.html', {'se': se})

def faq(request):
    se = Faq.objects.all()
    dd = Registration.objects.get(id = request.session['logg'])
    if request.method == 'POST':
        text_feed = request.POST.get('text_feed')
        ss = Faq()
        a = str(dd.First_name)
        b = str(dd.Last_name)
        ss.Customer_name = a+' '+b
        ss.Customer_email = dd.Email
        ss.Question = text_feed
        ss.Answer = "To be expected soon"
        ss.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        messages.success(request, 'Please wait for reply')
        return render(request, 'customer_home.html', {'d': d, 'k': k})
    return render(request, 'faq.html', {'se': se})

def faqs(request):
    se = Faq.objects.all()
    if request.method == 'POST':
        text_ques = request.POST.getlist('text_ques')
        text_answ = request.POST.getlist('text_answ')
        cus_name = request.POST.getlist('cus_name')
        Customer_email = request.POST.getlist('Customer_email')
        ss = Faq.objects.all()
        ft = []
        for y in ss:
            if y.id not in ft:
                ft.append(y.id)
        fb = zip(ft,cus_name, Customer_email, text_ques, text_answ)
        for m,p,i,j,k in fb:
            for e in ss:
                ty = e.id
                ty = int(ty)
                if int(m) == ty:
                    e.Customer_name = p
                    e.Customer_email = i
                    e.Question = j
                    e.Answer = k
                    e.save()
        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'FAQ edited')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'faqs.html', {'se': se})

def del_faq(request):
    v = Faq.objects.all()
    return render(request,'del_faq.html',{'v':v})

def delete_faq(request, id):
    Faq.objects.get(id = id).delete()
    v = Faq.objects.all()
    return render(request, 'del_faq.html', {'v': v})


def quott_disc(request, id):
    id = int(id)
    g = Category_product.objects.get(id=id)
    if request.method == 'POST':
        min_q = request.POST.get('min_q')
        max_q = request.POST.get('max_q')
        dis_p = request.POST.get('dis_p')
        actt = request.POST.get('actt')
        try:
            m = Quotation.objects.get(catt=g)
            m.Category_name = g.Category_name
            m.Minimum_quantity = min_q
            m.Maximum_quantity = max_q
            m.Discount_percent = dis_p
            m.Status = actt
            m.catt = g
            m.save()
            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            messages.success(request, 'Quotation discount edited')
            return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
        except:
            m = Quotation()
            m.Category_name = g.Category_name
            m.Minimum_quantity = min_q
            m.Maximum_quantity = max_q
            m.Discount_percent = dis_p
            m.Status = actt
            m.catt = g
            m.save()
            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            messages.success(request, 'Quotation discount added')
            return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request,'quott_disc.html',{'g':g})

def delete_quot(request, id):
    id = int(id)
    g = Category_product.objects.get(id=id)
    try:
        m = Quotation.objects.get(catt = g)
    except:

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        messages.success(request, 'No quotation discount added for the specified category')
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request, 'delete_quot.html', {'g': g,'m':m})

def delete_quotm(request, id):
    Quotation.objects.get(id = id).delete()
    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd, ds)
    k = zip(idd, ds)
    zx = zip(idd, ds)
    kf = zip(idd, ds)
    messages.success(request, 'Discount given for the category has been removed')
    return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})

def del_quot(request):
    wr = Quotation_cus.objects.all()
    return render(request,'del_quot.html',{'wr':wr})

def del_qtt(request, id):
    Quotation_cus.objects.get(id = id).delete()
    wr = Quotation_cus.objects.all()
    return render(request, 'del_quot.html', {'wr': wr})

def quott(request):
    b_det = Band_details.objects.all()
    b_st = []
    act = []
    b_s = []
    act1 = []
    f_nam = []
    act2 = []
    ght = zip(f_nam, act2)
    clip = []
    clip_img = []
    cll = zip(clip, clip_img)
    pricd = []

    for g in b_det:
        if (g.Style not in b_st) and (g.Style != ''):
            b_st.append(g.Style)
            act.append(g.Status)
        if (g.Size_in_inch not in b_s) and (g.Size_in_inch != 0):
            b_s.append(g.Size_in_inch)
            act1.append(g.Status)
        if (g.Font_name not in f_nam) and (g.Font_name != ''):
            f_nam.append(g.Font_name)
            act2.append(g.Status)
        if (g.Clipart_name not in clip) and (g.Clipart_name != ''):
            clip.append(g.Clipart_name)
        if (g.Clipart_image not in clip) and (g.Clipart_image != ''):
            clip_img.append(g.Clipart_image)
        if (g.Unit_price not in pricd) and (g.Unit_price != 0):
            pricd.append(g.Unit_price)
    bb_det = zip(b_s, b_st, pricd)
    jkj = Quotation.objects.all()

    deli = Conveyance_fees.objects.all()
    dd = Registration.objects.get(id = request.session["logg"])
    if request.method == 'POST':
        catgo = request.POST.get('catgo')
        descript = request.POST.get('descript')
        qty = request.POST.get('qty')
        a = str(dd.First_name)
        c = str(dd.Last_name)
        b = Quotation_cus()
        b.Customer_name = a + ' ' + c
        b.Customer_email = dd.Email
        b.Category_name = catgo
        b.Description = descript
        b.Quantity_selected = qty
        b.Status = "To be expected"
        b.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        messages.success(request, 'Quotation sent')
        return render(request, 'customer_home.html', {'d': d, 'k': k})
    else:
        return render(request, 'quott.html', {'ght':ght,'bb_det':bb_det,'cll':cll,'b_s': b_s, 'b_st': b_st,'clip': clip, 'deli': deli,'jkj':jkj})

def view_all_products(request):
    kr = Category_product.objects.all()
    gr = []
    idd = []
    st = []
    for t in kr:
        if t.Category_name not in gr:
            gr.append(t.Category_name)
            idd.append(t.id)
            st.append(t.Status)
    rr = zip(idd,gr,st)
    return render(request,'view_all_products.html',{'rr':rr})

def quott1(request):
    catg = request.POST.get('catg')
    pro = Category_product.objects.filter(Category_name = catg)
    return render(request,'quott1.html',{'pro':pro})

def quott_req(request):
    if request.method == 'POST':
        status = request.POST.getlist('status')
        idd = request.POST.getlist('idd')
        idm = []
        for i in idd:
            n = int(i)
            idm.append(n)
        st_id = zip(idm,status)
        for k,j in st_id:
            try:
                f = Quotation_cus.objects.get(id = k)
                f.Status = j
                f.save()
            except:
                try:
                    b = Quotation_cus.objects.all()
                    return render(request,'quott_req.html',{'b':b})
                except:
                    return render(request,'quott_req.html')

    try:
        b = Quotation_cus.objects.all()
        return render(request, 'quott_req.html', {'b': b})
    except:
        return render(request, 'quott_req.html')

def customers(request):
    rt = Registration.objects.exclude(Email = 'admin@gmail.com')
    return render(request,'customers.html',{'rt':rt})

def block_cust(request, id):
    rt = Registration.objects.get(id=id)
    rt.Lock = 'blocked'
    rt.save()
    rt = Registration.objects.exclude(Email = 'admin@gmail.com')
    return render(request, 'customers.html', {'rt': rt})

def open_cust(request, id):
    rt = Registration.objects.get(id=id)
    rt.Lock = 'opened'
    rt.save()
    rt = Registration.objects.exclude(Email = 'admin@gmail.com')
    return render(request, 'customers.html', {'rt': rt})

def my_prof(request):
    rt = Registration.objects.get(id = request.session['logg'])
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        psw = request.POST.get('psw')
        Lok = request.POST.get('lok')
        rt.First_name = first_name
        rt.Last_name = last_name
        rt.Email = email
        rt.Password = psw
        rt.State = state
        rt.City = city
        rt.Pincode = pincode
        rt.Address = address
        rt.Phone = phone
        rt.Lock = Lok
        rt.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        messages.success(request, 'Updated profile')
        return render(request, 'customer_home.html', {'d': d, 'k': k})
    return render(request, 'my_prof.html', {'rt': rt})

def about(request):
    df = Registration.objects.get(Email = 'admin@gmail.com')
    bn = Category_product.objects.all()
    return render(request,'about.html',{'df':df,'bn':bn})

def abb(request):
    amm = Registration.objects.get(Email = 'admin@gmail.com')
    if request.method == 'POST':
        abbt = request.POST.get('abbt')
        idd = request.POST.get('idd')
        try:
            adc = Registration.objects.get(id = idd)
            adc.About = abbt
            adc.save()

            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            messages.success(request, 'Content added')
            return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
        except:
            adc = About()
            adc.About = abbt
            adc.save()
            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            messages.success(request, 'Content added')
            return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})
    return render(request,'about_content.html',{'amm':amm})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        t_a = request.POST.get('t_a')
        g = Feedback()
        g.Name = name
        g.Email = email
        g.Content = t_a
        g.Category = 'Guest'
        g.save()
        messages.success(request, 'Message sent')
        return render(request,'home.html')
    return render(request,'contact.html')

def g_m(request):
    bb = Feedback.objects.all()
    return render(request,'guest_message.html',{'bb':bb})

def delete_g_msg(request,id):
    Feedback.objects.get(id=id).delete()
    bb = Feedback.objects.all()
    messages.success(request, 'Message deleted')
    return render(request, 'guest_message.html',{'bb':bb})

def view_cus_band_orders(request):
    n = Registration.objects.get(id = request.session["logg"])
    b = Band_order.objects.filter(Email = n.Email)
    mm = Band_details.objects.all()
    return render(request,'view_cus_band_orders.html',{'b':b,'mm':mm})

def view_pre_cus_ord(request, id):
    id = str(id)
    n = Registration.objects.get(id = request.session["logg"])
    try:
        b = Pre_order.objects.filter(Email = n.Email, Category_name = id)
        gf = str()
        for i in b:
            gf = i.Category_name
            break
        return render(request, 'view_pre_cus_ord.html', {'b': b,'gf':gf})
    except:
        return render(request, 'view_pre_cus_ord.html')

def view_quotations_cust(request):
    n = Registration.objects.get(id=request.session["logg"])
    b = Quotation_cus.objects.filter(Customer_email = n.Email)
    return render(request, 'view_quotations_cust.html',{'b':b})

def price_chart(request):
    band_pr = Band_details.objects.all()
    quo_pr = Quotation.objects.filter(Status = 'Active')
    Categories = Category_product.objects.filter(Status = 'Active')
    Del_ch = Conveyance_fees.objects.filter(Status = 'Active')
    ship_cost = Conveyance_fees.objects.filter(Status = 'Active')
    return render(request,'price_chart.html',{'band_pr':band_pr,'quo_pr':quo_pr,'Categories':Categories,'Del_ch':Del_ch,'ship_cost':ship_cost})

