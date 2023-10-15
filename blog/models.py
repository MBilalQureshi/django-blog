from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # 1 TO MANY, 1 user can have many posts, on_delete=models.CASCADE means O
    # To M relation is deleted, delete related records too, meaning if user
    # is deleted, delete blog post too
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # M to M as many users can like many posts
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/options/#ordering
        # order our post on created and - means in decending
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        # herper method to return total number of likes
        return self.likes.count()


class Comment(models.Model):
    # one to many, if post is deleted so will the comment
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/options/#ordering
        # asscending order(oldest first)
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
