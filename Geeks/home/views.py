from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
     return render(request,'about.html')
def contact(request):
     if request.method == "POST":
          name = request.POST['name']
          email = request.POST['email']
          phone = request.POST['phone']
          content = request.POST['content']
          if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<10:
                messages.error(request,"please fill the form properly")
          else:
               contact = Contact(name=name,email=email,phone=phone,content=content)
               contact.save()
               messages.success(request,"Your response has been submitted sucessfully")
          return render(request,'contact.html')     
     
       
     return render(request,'contact.html')   

# def search(request):
#      query=request.GET['query']
#      if len(query)> 78:
#           allposts=Post.objects.none()
#      else:
#           allposts=Post.objects.filter(title__icontains=query)
#           allposts=Post.objects.filter(author__username__icontains=query)
#           allposts=Post.objects.filter(content__icontains=query)

#      if allposts.count()==0:
#           messages.error(request,"No search results found. Please refine your query")     
#      params={'allposts':allposts}
#      return render(request,'search.html',params)
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")    
    params={'allPosts': allPosts, 'query': query}    
    return render(request, 'search.html', params)


def signin(request):
    if request.method=="POST":
        username=request.POST["loginusername"]
        email=request.POST["inputEmail"]
        password=request.POST["loginpassword1"]
        confirm_password=request.POST["loginpassword2"]
    #creating user    
        if password != confirm_password:
            messages.warning(request,"password do not match,please check the password and try again")
        else:
            data = User.objects.create_user(username=username,email=email,password=password)
            data.save()
            messages.success(request,"Your response has been submitted sucessfully")
    return redirect("home")

def bloglogin(request):
    if request.method=="POST":
        #parameter for the post
        loginusername = request.POST["loginusername"]
        loginpassword= request.POST["loginpassword"]

        user=authenticate(username=loginusername,password=loginpassword)
        if user is None:
            messages.warning(request,"Invalid credentials,please check and retry")
        else:
            login(request,user)
            messages.success(request,"successfully logged in")
        return redirect('home')
    return HttpResponse("404 - Not Found")        
def bloglogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')

