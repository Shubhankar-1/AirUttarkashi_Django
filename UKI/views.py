from django.shortcuts import render, HttpResponseRedirect
from .models import ticket
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User, auth

def home(request):
    return render(request, 'home.html')

def data(request):
    if request.method == 'POST':
        d = request.POST
        a=[]
        for b,c in d.items():
            a.append(c)

        da = ticket(First_Name=a[1],
        Last_Name=a[2],From=a[3],To=a[4],Mob=a[5],
        Flight_Date=a[6],Class=a[7])
        da.save()
        print("saved")
        fdata = {'fname':a[1],'lname':a[2],'frm':a[3],'to':a[4],'mob':a[5],'fdate':a[6],'cl':a[7]}
        return render(request, 'booked.html',fdata)
    else:
        return render(request, 'booking.html')

def details(request):
    return render(request,'details.html')

def search(request):
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            match=ticket.objects.filter(Q(First_Name__iexact=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'No Record Found')
        else:
            return HttpResponseRedirect('search')
    return render(request,'search.html')
    
