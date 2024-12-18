from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,LoginForm,CaptchaForm
from .models import CustomUser,backuser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.db import IntegrityError

def send_mail(rec,idd,forpass):
    server = smtplib.SMTP('smtp.gmail.com',587)
    senderr = "Your-email"
    server.starttls()
    server.login(senderr,"password_here")
    message = MIMEMultipart()
    message['From'] = senderr
    message['To'] = rec
    if not forpass:
        message['Subject'] = "Activation link for Customer"
        
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; font-size: 16px; color: #333;">
            <p>Dear User,</p>
            <p>Thank you for joining our service. Please visit the following link to activate your account:</p>
            <p><a href="http://127.0.0.1:8000/activate/{idd}" style="color: #007bff; text-decoration: none;">Activate My Account</a></p>
            <p>Best regards,<br>Team Example</p>
        </body>
        </html>
        """
    else:
        message['Subject'] = "Your password for Account"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; font-size: 16px; color: #333;">
            <p>Dear User,</p>
            <p>Thank you for joining our servies</p>
            <p>Your password for eatright is <h1>{idd}</h1></p>
            <p>Don't Share with strangers</p>
            <p>Best regards,<br>Team Example</p>
        </body>
        </html>
        """

    message.attach(MIMEText(body, 'html'))
    try:
        server.sendmail(senderr,rec,message.as_string())
        return True
    except Exception as e:
        print(e)
        return False

@login_required   
def logout_user(request):
    logout(request)
    return redirect("/login")

def register(request):
    msg = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            plain_password = form.cleaned_data['password1']  # Get plain password
            email = form.cleaned_data['email']
            try:
                backuser.objects.create(email=email,password=plain_password)
                form.save()
        
            except IntegrityError:
                msg = "Email Already Exist, try diffrent email"
            except Exception as e:
                msg = "An Error occured, error : "+e
            else:
                idd = CustomUser.objects.filter(email=email).values("usid").first()
                if send_mail(email,idd['usid'],False):

                    form = LoginForm()

                    msg = "User registered Sucessfully , Activate through activation link send to email"  # Redirect to the login page after successful registration
                    return render(request, 'login.html', {'form': form,"msg":msg})
                else:
                    return HttpResponse("An Error Occured try again later")
                
            return render(request, 'register.html', {'form': form,"msg":msg})
            

         
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form,"msg":msg})


def custom_login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')  # Redirect to your desired pag
                else:
                    context = {"msg":"Account is not activated","color":"warning"}

            else:
                context = {"msg":"Invalid crendentials","color":"danger"}
            
        else:
            context = {"msg":"Fill all fields coreectly","color":"warning"}
    
    context["form"] = LoginForm
    return render(request, 'login.html', context)

@login_required
def home(request):
    return render(request,"index.html")

def forgotpassword(request):
    msg,color = None,None
    if request.method == "POST":
        email = request.POST.get('forgotemail')
        password = backuser.objects.filter(email=email).first()
        if password:
            if send_mail(email,password,True):
                msg = "Password is been sent to respective email"
                color = "success"
            else:
                msg = "An Error occured , try again later"
                color = "warning"

        else:
            msg = "This email Doesn't Exist in system"
            color = "danger"
    context = {"msg":msg,"color":color}
    return render(request,"forgot.html",context)

def activate(request,id):
    try:
        CustomUser.objects.filter(usid=id).update(is_active=True)
        form = LoginForm()
        msg = "User is now activated"  # Redirect to the login page after successful registration
        return render(request, 'login.html', {'form': form,"msg":msg,"color":"success"})
    except CustomUser.DoesNotExist:
        return HttpResponse("<center style='color:lightgreen'>Account Does not exist,<a href='/'>Register here</a></center>")
    
