from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    subheading = models.CharField(max_length=300)
    tldr = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    estimated_read_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reaction(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    reaction_type = models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=10)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reaction_type} on {self.blog.title}"

class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.blog.title} by {self.name or 'Anonymous'}"

class StorySubmission(models.Model):
    story_text = models.TextField()
    allow_publish = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Story submitted on {self.submitted_at.strftime('%Y-%m-%d')}"

class Feedback(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1 to 5
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}★ on {self.blog.title} by {self.email or 'Anonymous'}"

