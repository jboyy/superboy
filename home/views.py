from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from blogcomment import models
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import authenticate
from home import forms
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
 
def about(request):
    return render (request,'about.html')
def blog(request):
    blogs = models.blog.objects.all()
    context = {'blogs': blogs }
    return render (request,'bloghome.html',context)

class bloglistview(ListView):
  model =models.blog
  template_name ='bloghome.html'
  context_object_name ='blogs'
  ordering = ['-date']
  paginate_by = 2

class userbloglistview(ListView):
  model =models.blog
  template_name ='blog_user_posts.html'
  context_object_name ='blogs'
  paginate_by = 2

  def get_queryset(self):
      user =get_object_or_404(User,username =self.kwargs.get('username')) 
      return models.blog.objects.filter(author=user).order_by('-date')

class blogdetailview(DetailView):
   model =models.blog
   template_name ='blog_detail.html'

   def get_context_data(self,*args,**kwargs):
     context=super().get_context_data(**kwargs)
  
     context['comments'] =models.BlogComment.objects.filter(blogpost=self.object).order_by('-date')
     context['form']=forms.CommentForm()
     return context
   
   #def post(self,request,*args,**kwargs):
     # new_comment = models.BlogComment(content=request.POST.get('content'),blogpost =self.get_object())
      #new_comment.save()
      #return self.get(self,request,*args,**kwargs)

class AddCommentView(CreateView):
   model =models.BlogComment
   form_class =forms.CommentForm
   template_name ='add_comment.html'
   
   def form_valid(self,form):
     form.instance.blogpost_id = self.kwargs['pk']
     return super().form_valid(form)
     #success_url = reverse_lazy('home')
    # messages.success (request,f'comment added')
    # return redirect('blog')
   def get_success_url(self,**kwargs):
     
     return reverse('blog')
  
  
   
class blogcreateview(LoginRequiredMixin,CreateView):
    model = models.blog
    template_name ='blog_form.html'
    fields = ['title','content','header_image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return  super().form_valid(form)
    
   
class blogupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.blog
    template_name ='blog_form.html'
    fields = ['title','content','header_image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return  super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
          return True
        return False    
class blogdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model =models.blog
    success_url = "/blog"
    template_name ="blog_confirm_delete.html"
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
          return True
        return False

def home(request):
    #context = {"posts":posts}
    return render (request,'index.html')

def search(request):
    if request.method =='GET':

      query=request.GET['q']
      allPosts= model.blog.objects.filter(title__icontains=query)
      params={'allPosts': allPosts}
    return render(request, 'search.html', params)


def logout(request):
    #context = {"posts":posts}
    return render(request,'logout.html')