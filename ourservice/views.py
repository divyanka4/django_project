# from contactform.models import Contactform

# def ContactPage(request):

#     msg=""
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         subject=request.POST.get('subject')
#         message=request.POST.get('message')
#         alldata=Contactform(name=name,email=email,subjet=subject,message=message)
#         alldata.save() 
#         msg="Data Inserted"

#     return render(request,"contact.html",{'msg':msg})