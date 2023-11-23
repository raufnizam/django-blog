from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# def home(request):
    # return render(request, 'home.html' , {})

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'  

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)

        see = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = see.total_likes()

        liked = False
        if see.likes.filter(id=self.request.user.id).exists():
            liked =True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        # form.instance.name = self.request.user.username 
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.kwargs['pk']})

class AddCAtegoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('blog:home')
    

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

def category_view(request, cats):
    category_posts = Post.objects.filter(category=cats)
    cat_menu = Category.objects.all()
    has_posts = {category: Post.objects.filter(category=category).exists() for category in cat_menu}

    context = {
        'cats': cats,
        'category_posts': category_posts,
        'cat_menu': cat_menu,
        'has_posts': has_posts
    }
    return render(request, "categories.html", context)
    
