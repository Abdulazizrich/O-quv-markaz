from django.shortcuts import render, redirect
from .forms import *

def bosh_sahifa(request):
    return render(request, 'bosh_sahifa.html')

#Qo'shish
def yonalish(request):
    if request.method == 'POST':
        data = YonalishForm(request.POST)
        if data.is_valid():
            Yonalish.objects.create(
                nom=data.cleaned_data['nom'],
                narx=data.cleaned_data['narx'],
            )
        return redirect('/yonalish/')
    natija = Yonalish.objects.all()
    kiritilgan_nom = request.GET.get("nom")
    print(kiritilgan_nom)
    if kiritilgan_nom is not None:
        natija = Yonalish.objects.filter(nom__contains=kiritilgan_nom)
        print(natija)

    context = {
        'form': YonalishForm(),
        "yonalish": natija
    }
    return render(request, 'yonalish.html', context)

def xona(request):
    if request.method == 'POST':
        data = XonaForm(request.POST)
        if data.is_valid():
            Xona.objects.create(
                nom=data.cleaned_data['nom'],
                raqam=data.cleaned_data['raqam'],
            )
        return redirect('/xona/')
    context = {
        'xona': Xona.objects.all(),
        'form': XonaForm()
    }
    return render(request, 'xona.html', context)

def ustoz(request):
    if request.method == 'POST':
        data = UstozForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/ustoz/')
    context = {
        'ustoz': Ustoz.objects.all(),
        'form': UstozForm()
    }
    return render(request, 'ustoz.html', context)

def guruh(request):
    if request.method == 'POST':
        data = GuruhForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/guruh/')
    context = {
        'guruh': Guruh.objects.all(),
        'form': GuruhForm()
    }
    return render(request, 'guruh.html', context)


def oquvchi(request):
    if request.method == 'POST':
        data = OquvchiForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/oquvchi/')
    context = {
        'oquvchi': Oquvchi.objects.all(),
        'form': OquvchiForm()
    }
    return render(request, 'oquvchi.html', context)

def tolov(request):
    if request.method == "POST":
        Tolov.objects.create(
            oquvchi= Oquvchi.objects.get(id=request.POST["oquvchi"]),
            guruh= Guruh.objects.get(id=request.POST["guruh"]),
            tolov_summasi=request.POST.get("tolov_summasi"),
            qarz=request.POST.get("qarz"),
            chegirma=request.POST.get("chegirma"),

        )
    data = {
        "tolov": Tolov.objects.all(),
        'oquvchilar': Oquvchi.objects.all(),
        'guruhlar': Guruh.objects.all(),
    }
    return render(request, "tolov.html", data)


#Tahrirlash
def yonalish_tahrirlash(request, id):
    if request.method == 'POST':
        yonalish = Yonalish.objects.get(id=id)
        yonalish.nom = request.POST['nom']
        yonalish.narx = request.POST['narx']
        yonalish.save()
        return redirect('/yonalish/')
    context = {
        'yonalish': Yonalish.objects.get(id=id)
    }
    return render(request, 'yonalish_tahrirlash.html', context)

def xona_tahrirlash(request, id):
    if request.method == 'POST':
        xona = Xona.objects.get(id=id)
        xona.nom = request.POST['nom']
        xona.raqam = request.POST['raqam']
        xona.save()
        return redirect('/xona/')
    context = {
        'xona': Xona.objects.get(id=id)
    }
    return render(request, 'xona_tahrirlash.html', context)


def ustoz_tahrirlash(request, id):
    if request.method == 'POST':
        ustoz = Ustoz.objects.get(id=id)
        ustoz.ism = request.POST['ism']
        ustoz.tel_raqam = request.POST['tel_raqam']
        ustoz.yonalish = Yonalish.objects.get(id=request.POST["yonalish"])
        ustoz.manzil = request.POST['manzil']
        ustoz.save()
        return redirect('/ustoz/')
    context = {
        'ustoz': Ustoz.objects.get(id=id),
        'yonalish': Yonalish.objects.all(),
    }
    return render(request, 'ustoz_tahrirlash.html', context)

def guruh_tahrirlash(request, id):
    if request.method == 'POST':
        guruh = Guruh.objects.get(id=id)
        guruh.nom = request.POST['nom']
        guruh.yonalish = Yonalish.objects.get(id=request.POST["yonalish"])
        guruh.ustoz = Ustoz.objects.get(id=request.POST["ustoz"])
        guruh.xona = Xona.objects.get(id=request.POST["xona"])
        guruh.ochilgan_sana = request.POST['ochilgan_sana']
        guruh.dars_vaqti = request.POST['dars_vaqti']
        guruh.save()
        return redirect('/guruh/')
    context = {
        'guruh': Guruh.objects.get(id=id),
        'yonalish': Yonalish.objects.all(),
        'ustoz': Ustoz.objects.all(),
        'xona': Xona.objects.all(),
    }
    return render(request, 'guruh_tahrirlash.html', context)


def oquvchi_tahrirlash(request, id):
    if request.method == 'POST':
        oquvchi = Oquvchi.objects.get(id=id)
        oquvchi.ism = request.POST['ism']
        oquvchi.tel_raqam = request.POST['tel_raqam']
        oquvchi.guruh = Guruh.objects.get(id=request.POST["guruh"])
        oquvchi.save()
        return redirect('/oquvchi/')
    context = {
        'oquvchi': Oquvchi.objects.get(id=id),
        'guruh': Guruh.objects.all(),
    }
    return render(request, 'oquvchi_tahrirlash.html', context)


def tolov_tahrirlash(request, id):
    if request.method == 'POST':
        tolov = Tolov.objects.get(id=id)
        tolov.oquvchi = Oquvchi.objects.get(id=request.POST["oquvchi"])
        tolov.guruh = Guruh.objects.get(id=request.POST["guruh"])
        tolov.tolov_summasi = request.POST['tolov_summasi']
        tolov.qarz = request.POST['qarz']
        tolov.chegirma = request.POST['chegirma']
        tolov.save()
        return redirect('/tolov/')
    context = {
        'tolov': Tolov.objects.get(id=id),
        'oquvchi': Oquvchi.objects.all(),
        'guruh': Guruh.objects.all(),
    }
    return render(request, 'tolov_tahrirlash.html', context)



#O'chirish
def yonalish_ochir(request, id):
    Yonalish.objects.get(id=id).delete()
    return redirect("/yonalish/")

def xona_ochir(request, id):
    Xona.objects.get(id=id).delete()
    return redirect("/xona/")

def ustoz_ochir(request, id):
    Ustoz.objects.get(id=id).delete()
    return redirect("/ustoz/")

def guruh_ochir(request, id):
    Guruh.objects.get(id=id).delete()
    return redirect("/guruh/")

def oquvchi_ochir(request, id):
    Oquvchi.objects.get(id=id).delete()
    return redirect("/oquvchi/")

def tolov_ochir(request, id):
    Tolov.objects.get(id=id).delete()
    return redirect("/tolov/")


