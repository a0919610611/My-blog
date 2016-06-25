from django.shortcuts import *
from django.http import *
from .models import *
from datetime import *
from django.views.generic import *
from django.core.urlresolvers import *
from django.views.generic.edit import *
from blog.forms import *
def article_list(request):
    article_list=Article.objects.all().filter(status='p')
    return render(request,'article_list.html',locals())
def article_draft_list(request):
    if request.user.is_superuser:
        article_list=Article.objects.all().filter(status='d')
        return render(request,'draft_list.html',locals())
    else:
        return HttpResponseRedirect('/')
def admin_article_list(request):
    article_list=Article.objects.all()
    return render(request,'admin_article_list.html',locals())
def publish(request,article_id):
    article=Article.objects.get(pk=article_id)
    article.publish()
    article.save()
    #return HttpResponseRedirect(reverse('article:detail',kwargs={'article_id':article_id}))
    return HttpResponseRedirect(reverse('article:admin_article_list'))
def unpublish(request,article_id):
    article=Article.objects.get(pk=article_id)
    article.unpublish()
    article.save()
    #return HttpResponseRedirect(reverse('article:detail',kwargs={'article_id':article_id}))
    return HttpResponseRedirect(reverse('article:admin_article_list'))
class ArticleDetailView(DetailView):
    model=Article
    template_name='detail.html'
    context_object_name="article"
    pk_url_kwarg = 'article_id'
    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.blogcomment_set.all()
        kwargs['form'] = BlogCommentForm()
        return super(ArticleDetailView, self).get_context_data(**kwargs)
class CommentPostView(FormView):
    form_class=BlogCommentForm
    template_name='detail.html'
    def form_valid(self,form):
        target_article=get_object_or_404(Article,pk=self.kwargs['article_id'])
        comment=form.save(commit=False)
        comment.article=target_article
        comment.save()
        self.success_url = target_article.get_absolute_url()
        return HttpResponseRedirect(self.success_url)
    def form_invalid(self,form):
         target_article=get_object_or_404(Article,pk=self.kwargs['article_id'])
         return render(self.request, 'detail.html', {
            'form': form,
            'article': target_article,
            'comment_list': target_article.blogcomment_set.all(),
        })
