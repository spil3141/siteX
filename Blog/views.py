from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from Blog.forms import Post_Form,Comment_Form
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from Blog.models import Post,Comment
from django.views.generic import (TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView
                                  )
import accounts.models as from_accounts

from django.db.models import Q


# A Class-base View for the About Page.
class About(TemplateView):
    template_name = "Blog/About.html"


class PostListView(ListView):
    context_object_name = "post_list"
    model = Post
    def get_queryset(self):
        q = self.request.GET.get("q")
        list_of_post_by_user = Post.objects.all().filter(published_date__isnull = False).order_by("create_date")
        if q:
            return list_of_post_by_user.filter(
            Q(title__icontains=q) |
            Q(text__icontains = q)
            ).distinct()
        else:
            return list_of_post_by_user
        # return Post.objects.filter(published_date__isnull = False).order_by("create_date")

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     selected_user_object = from_accounts.User.objects.all().filter(pk=self.kwargs.get("pk")) # .filter(username=self.request.user)
    #     context["object"] = selected_user_object
    #     return context
    # def get_queryset(self):
    #     return Post.objects.filter(published_date__lre = timezone.now()).order_by("-published_date")

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post_detail"


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    redirect_field_name = "Blog/post_detail.html"
    template_name_suffix = "_create"
    form_class = Post_Form
    model = Post


#View for updating a post, needs login authentification.
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    redirect_field_name = "Blog/post_detail.html"
    template_name_suffix = "_update"
    form_class = Post_Form
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    context_object_name = "post_list"
    model = Post
    success_url = reverse_lazy("Blog:Post_List_Page")


class PostDraftView(LoginRequiredMixin,ListView):
    login_url = "/login/"
    redirect_field_name = "Blog/post_detail.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by("create_date")

@login_required
def Post_Publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect("Blog:Post_List_Page")


# @login_required
def app_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk = pk)
    if (request.method == "POST"):
        form = Comment_Form(request.POST)
        if (form.is_valid()):
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect("Blog:Post_Detail_Page", pk = post.pk)
    else:
        form = Comment_Form()
    return render(request,"Blog/comment_create.html",{"form":form})

# @login_required
# def Post_Like(request,pk):
#     post = get_object_or_404(Post,pk = pk)
#     post.star.add(request.user)
#     post.save()
#     return redirect("Blog:Post_List_Page")

@login_required
def Comment_Approve(request,pk):
    comment = get_object_or_404(Comment,pk = pk)
    comment.approve()
    return redirect('Blog:Post_Detail_Page',pk=comment.post.pk)


@login_required
def Comment_Remove(request,pk):
    comment = get_object_or_404(Comment,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('Blog:Post_Detail_Page',pk=post_pk)






    # model = Post
    # template_name = "stage/user_profile_detail.html"
    #
    # def get_queryset(self): # new
    #     query = self.request.GET.get('q')
    #     object_list = Post.objects.filter(title=query)
    #     return object_list


# class Profile(LoginRequiredMixin,TemplateView):
#     login_url = "/login/"
#     template_name = "Blog/post_list.html"


# def index(request):
#     return redirect("Blog:Post_List_Page")
