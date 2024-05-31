from django.shortcuts import render

# Create your views here.
def fun(request):
    return render(request,'first.html')

def fun2(request):
    return render(request,'h1.html')

def nk(request,fath,son ):
    father=fath
    son=son
    nandha={"fath":father,"son":son}
    return render(request,'h1.html',nandha)

def kow(request,p_name,b_name):

    butter=b_name
    fly=p_name
    context={"me":butter,"you":fly}
    return render(request,'first.html',context)



def base(request):
    return render(request,"base.html")



def page1(request,butter,baby):
    butter=butter
    baby=baby
    context={"butter":butter,"baby":baby}
    return render(request,"page1.html",context)

   
def page2(request,dady,son):
    dady=dady
    son=son
    return render(request,"page2.html",{"dady":dady,"son":son})


def page3(request,pop,top):
    pop=pop
    top=top
    context={"pop":pop,"top":top}
    return render(request,"page3.html",context)


def info(request):
    if request.method == "POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        number=request.POST.get('number')
        email=request.POST.get('email')
        context={'name':name,'age':age,'number':number,'email':email}
        return render(request,'info.html',context)
    return render(request,'info.html')

def calsi(request):
    if request.method == "POST":
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        calculate=request.POST.get("calculater")
        if calculate =="add":
            sum=num1+num2
            context={"sum":sum}
            return render(request,"calsi.html",context)
        
        if calculate =="sub":
            sum=num1-num2
            context={"sum":sum}
            return render(request,"calsi.html",context)
        
        if calculate =="mul":
            sum=num1*num2
            context={"sum":sum}
            return render(request,"calsi.html",context)
        
        if calculate =="div":
            sum=num1/num2
            context={"sum":sum}
            return render(request,"calsi.html",context)
        
    return render(request,"calsi.html")



def wish(request,father,son):
    context= {'father':father,'son':son}
    return render(request ,'sample.html', context )

def rhyme1(request,butter,baby):
    context={'butter':butter,'baby':baby}
    return render(request ,'sam2.html', context )

def rhyme2(request,pop,top):
    context={'pop':pop,'top':top}
    return render(request ,'sam3.html', context )

def rhyme3(request,ringa,rose):
    context={'ringa':ringa,'rose':rose}
    return render(request ,'sam4.html', context )
