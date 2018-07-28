from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout
import os


global data
@csrf_exempt
def hello(request):
	print "hello"
	return render(request,'recruitmentapp/home.html')

@csrf_exempt
def success(request):
		print "hello"
		if request.method =="POST":
			url=str(request.POST['url2'])
			print "url obtained is",url
			print "sucess"
			print type(url)
			info=url.split(',')
			name,experience,p_lang=info[0],info[1],info[2]
			print name,experience,p_lang
			with open("C:\\recruitment\\"+name+".txt",'w') as file:
				file.write("Name: "+name+'\n'+"Experience: "+experience+'\n'+"Programming_Langauage: "+p_lang+'\n')

			return HttpResponse("Application submitted ")



@csrf_exempt
def adminpage(request):
		applicants=os.listdir("C:\\recruitment")
			
		return render(request,'recruitmentapp/header2.html',{"hlappl":applicants})

@csrf_exempt
def logout(request):
		logout(request)
			
		return redirect('/recruitmentapp/login.html')

@csrf_exempt
def showprofile(request):
		global data
		if request.method =="POST":
			url=str(request.POST['url2'])
			with open("C:\\recruitment\\"+url) as file:
				data=file.readlines()
				print "data  obtained is",data
				
			
				return render(request,'recruitmentapp/header2.html')


@csrf_exempt
def viewprofile(request):
		 
		 print "The profile is ",data
		 return render(request,"recruitmentapp/result.html",{"info":data})


@csrf_exempt
def accept(request):
		if request.method =="POST":
			url=str(request.POST['url2'])
			print type(url)
			print "url is ",url
			name=url.split(';')[1].replace('&#39 Name:','')
			print "name is ",name.split()[0]
			x= name.split()[1]
			with open("C:\Filtered\\accepted.txt",'a+') as file:
				file.write("selected candidate :"+name+"\n")
				
		 	return HttpResponse("Candidate selected and added to the accepted list in the path   C:\Users\c24088948\Desktop\Applications\\accepted.txt")

@csrf_exempt
def reject(request):
		if request.method =="POST":
			url=str(request.POST['url2'])
			print type(url)
			print "url is ",url
			name=(url.split(';')[1]).replace('&#39 Name:','')
			print "name is ",name.split()[0]
			x= name.split()[1]
			with open("C:\Filtered\\rejected.txt",'a+') as file:
				file.write("Rejected candidate :"+x+"\n")
				
		 		return HttpResponse("Candidate rejected and added to the rejected list C:\Users\c24088948\Desktop\Applications\\accepted.txt")
	 
	 

	


   

         
         

        
         
         
         
    
