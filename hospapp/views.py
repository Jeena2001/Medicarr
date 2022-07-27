from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,render_to_response,redirect
from django.db import connection

def index(request):
	return render(request,'index.html')
def patienthome(request):
    return render(request,'patienthome.html')
def login(request):
    return render(request,'login.html')
def logaction(request):
    cursor=connection.cursor()
    p=request.GET['t1']
    q=request.GET['t2']
    sql2="select * from login where uname='%s' and upass='%s'"%(p,q)
    cursor.execute(sql2)
    rs=cursor.fetchall()
    if(cursor.rowcount)>0:
        sql3="select * from login where uname='%s' and upass='%s'"%(p,q)
        cursor.execute(sql3)
        rsl=cursor.fetchall()
        for rowl in rsl:
            request.session['id']=rowl[0]
            request.session['utype']=rowl[3]
            if(request.session['utype']=='doctor'):
                return render(request,'doctor.html')
            elif(request.session['utype']=='patient'): 
                return render(request,'patienthome.html')
    else:
        html="<script>alert('invalid password and username');window.location='/index/';</script>"
        return HttpResponse(html)
    
def doctors(request):
    	return render(request,'doctor.html')
def patient(request):
    	return render(request,'patient.html')
def viewpat(request):
    	return render(request,'viewpat.html')
def paction(request):
    cursor=connection.cursor()
    fname=request.GET['t1']
    lname=request.GET['t2']
    addr=request.GET['t3']
    gend=request.GET['t4']
    mob=request.GET['t5']
    patid=request.GET['t6']
    passw=request.GET['t7']
    sql="insert into pat(fname,lname,address,gender,mob,patid,passw)values('%s','%s','%s','%s','%s','%s','%s')"%(fname,lname,addr,gend,mob,patid,passw)
    cursor.execute(sql)
    sql3="select max(pid)  from pat" 
    cursor.execute(sql3)
    result=cursor.fetchall()
    for row in result:
        id=int(row[0])
        sql2="insert into login(uid,uname,upass,utype) values('%s','%s','%s','%s')"%(id,patid,passw,'patient')
        cursor.execute(sql2)
        msg="<script>alert ('Sucessfully Added');window.location='/patient/';</script>"
        return HttpResponse(msg)
def patientupdate(request):
    	return render(request,'patientupdate.html')
 
def pre(request):
    	return render(request,'pres.html')
def viewpat(request):
    cursor=connection.cursor()
    s="select * from pat"
    cursor.execute(s)
    result=cursor.fetchall()
    list=[]
    for row in result:
        y={'pid':row[0],'fname':row[1], 'lname':row[2], 'addr':row[3], 'gend':row[4], 'mob':row[5], 'patid':row[6]}
        list.append(y)
    return render(request,'viewpat.html',{'list':list})

def dele(request):
    cursor=connection.cursor()
    cd=request.GET['id']
    sql="delete from pat where pid='%s'" %(cd)
    cursor.execute(sql)		
    msg="<script>alert('deleted');window.location='/viewpat/';</script>"
    return HttpResponse(msg)
# Create your views here.
def update(request):
    cursor=connection.cursor()
    id=request.GET['id']
    s="select * from pat where pid=%s" %(id)
    cursor.execute(s)
    rs=cursor.fetchall()
    list=[]
    for row in rs:
        y={'pid':row[0],'fname':row[1], 'lname':row[2], 'addr':row[3], 'gend':row[4], 'mob':row[5], 'patid':row[6]}
        list.append(y)
        return render(request,'patientup.html',{'list':list})
def pdaction(request):
    cursor=connection.cursor()
    fname=request.GET['t1']
    lname=request.GET['t2']
    addr=request.GET['t3']
    mob=request.GET['t5']
    patid=request.GET['t6']
    cd= request.GET['t8']
    sql="update pat set fname='%s',lname='%s',address='%s',mob='%s',patid='%s' where pid='%s'" %(fname,lname,addr,mob,patid,cd)
    cursor.execute(sql)
    msg="<script>alert ('Sucessfully Updated');window.location='/viewpat/'</script>"
    return HttpResponse(msg)
def logout(request):
    try:
        del request.session['id']
        del request.session['utype']
    except:
        pass
    return HttpResponse("<script>alert('you are loged out');window.location='/index/';</script>")

def preaction(request):
    cursor=connection.cursor()
    fname=request.GET['t1']

    sql="select * from pat where  patid='%s'" %(fname)
    cursor.execute(sql)
    result=cursor.fetchall()
    list=[]
    for row in result:
        y={'pid':row[0],'fname':row[1], 'lname':row[2], 'addr':row[3], 'gend':row[4], 'mob':row[5], 'patid':row[6]}
        list.append(y)
    return render(request,'patpre.html',{'list':list})

def addp(request):
    	return render(request,'detail.html')
def detailaction(request):
    cursor=connection.cursor()
    mname=request.GET['t1']
    dos=request.GET['t2']
    time=request.GET['t3']
    sql="insert into detail(mname,dos,time)values('%s','%s','%s')" %(mname,dos,time)
    cursor.execute(sql)
    msg="<script>alert ('Sucessfully Added');window.location='/pre/';</script>"
    return HttpResponse(msg)
def viewpre(request):
    cursor=connection.cursor()
    

    s="select * from detail"
    cursor.execute(s)
    result=cursor.fetchall()
    list=[]
    for row in result:
        y={'id':row[0],'mname':row[1], 'dos':row[2], 'time':row[3]}
        list.append(y)
    return render(request,'viewpatient.html',{'list':list})

