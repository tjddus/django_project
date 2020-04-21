from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 장고 ORM , 쿼리셋(QuerySets)
'''
    from blog.models import Post
    from django.contrib.auth.models import User
    me = User.objects.get(username = 'tjddus')

    Post.objects.create(author=me, title='title 01', text='text 01')
    Post.objects.create(author=me, title='title 02', text='text 02')
    Post.objects.all()
    Post.objects.filter(author=me)
    Post.objects.filter(title__contains='title')
    Post.objects.filter(published_date__lte=timezone.now())
    # __lte : 같거나 보다 작다
    # __gte : 같거나 보다 크다
    post = Post.objects.get(title='title 01')
    post.publish()
    Post.objects.order_by('created_date')
    Post.objects.order_by('-created_date')



'''