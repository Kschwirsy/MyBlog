from django.contrib import admin
from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm

class PostType(models.Model):
    name = models.CharField(max_length=30, default="tech")

    def __unicode__(self):
        return u"%s" % self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, default='2014-01-01')
    postType = models.ForeignKey(PostType)
    comments = Comment.objects.filter(post=post)

    class Meta:
        ordering = ['-created']
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

class CommentForm(ModelForm):
        class Meta:
                model = Comment
                exclude = ["post"]

        def add_comment(request, pk):
            """add new comment"""
            p = request.Post

            if p.has_key("body") and p["body"]:
                    author = "Anonymous"
                    if p["author"]: author = p["author"]

                    comment = Comment(post = Post.objects.get(pk=pk))
                    cf = CommentForm(p, instance=comment)
                    cf.fields["author"].required = False

                    comment = cf.save(commit=False)
                    comment.author = author
                    comment.save()

                    return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))

class PostAdmin(admin.ModelAdmin):
        # fields display on change list
        list_display = ['title', 'description', 'published', 'created']
        # fields to filter the change list with
        list_filter = ['published', 'created']
        # fields to search in change list
        search_fields = ['title', 'description', 'content']
        # enable the date drill down on change list
        date_hierarchy = 'created'
        # enable ordering by date
        ordering = ('created',)
        # enable the save buttons on top on change form
        save_on_top = True
        # prepopulate the slug from the title - big timesaver!
        prepopulated_fields = {"slug": ("title",)}  