from django.db import models

class Blog(models.Model):
    title =         models.CharField(max_length=255)
    body =          models.TextField()
    created =       models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title

def upload_gallery_image(instance, filename):
    return f"images/{instance.blog.title}/gallery/{filename}"

class Image(models.Model):
    image =         models.ImageField(upload_to=upload_gallery_image)
    blog =          models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="images")
    
