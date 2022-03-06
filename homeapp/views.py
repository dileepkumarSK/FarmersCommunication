from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, logout, login
from homeapp.models import Shareinformation, Personhomepage, Register
from .forms import registerForm, EditForm, personhomepageFrom
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Permission
from django.views.generic import UpdateView

# Create your views here.
def home(request):
    return render(request, "homepage.html")


def signin(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("user name already exists")
                messages.info(request, "username already cexists")
            elif User.objects.filter(email=email).exists():
                print("email has allready account")
                messages.info(request, "email already exists")
            
            else:

                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password1,
                    email=email,
                )
                user.save()
                
                return redirect("login")
        else:
            messages.error(request, "passwrod not matches")
            print("passwrod not matches")

    return render(request, "signin.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "success")
            return redirect("homepagep")
        else:
            messages.info(request, "invalid credinatils")
            return redirect("login")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def share(request):
    shin = Shareinformation.objects.all()
    if request.method == "POST":
        sharee = request.POST["sharee"]
        email = request.POST["feddmil"]
        srfed = Shareinformation(sharee=sharee, email=email)
        srfed.save()

        return render(request, "share.html", {"shin": shin})
    return render(request, "share.html", {"shin": shin})


def detalis(request):
    return render(request, "details.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


@login_required
def homepagep(request):
    
    if request.user.is_authenticated:
        per = personhomepageFrom()
        if request.method == "POST":
            per = personhomepageFrom(request.POST, request.FILES)
            if per.is_valid():
                instance = per.save(commit=False)
                instance.user = request.user
                instance.save()

            else:
                return render(request, "homepagep.html", {"per": per})
    return render(request, "homepagep.html", {"per": per })


@login_required
def buyer(request):
    return render(request, "buyer.html")


@login_required
def seller(request):
    return render(request, "seller.html")


@login_required
def machineary(request):
    return render(request, "machineary.html")


@login_required
def security(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, user)
            return redirect("account")
    else:

        fm = PasswordChangeForm(user=request.user)
    return render(request, "security.html", {"fm": fm})


@login_required
def help(request):
    return render(request, "help.html")


@login_required
def register(request):
    if request.user.is_authenticated:
        reg = registerForm()
        
        if request.method == "POST":
            reg = registerForm(request.POST)
            if reg.is_valid():
                    instance = reg.save(commit=False)
                    instance.user = request.user
                    instance.save()
                    messages.success(request, "sucess")

            else:
                    messages.success(request, "try agian")

        return render(request, "register.html", {"reg": reg})

    return render(request, "register.html", {"reg": reg})


def central(request):
    return render(request, "central.html")


@login_required
def account(request):
    return render(request, "account.html")


@login_required
def feed(request):
    return render(request, "feed.html")


@login_required
def terms(request):
    return render(request, "terms.html")


@login_required
def cropdet(request):

    return render(request, "cropdet.html")


@login_required
def editperinfo(request):

    form = EditForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()

        return redirect("account")
        return render(request, "editprofile.html", {"form": form})

    return render(request, "editprofile.html", {"form": form})
