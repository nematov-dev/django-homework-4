from django.db import models

 
class Blogger(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Blogger'
        verbose_name_plural = 'Bloggers'



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.FileField(upload_to='content/')
    blogger = models.ForeignKey(Blogger,on_delete=models.CASCADE,related_name='posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.blogger.name} add post {self.title} ...'
    
    def __repr__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
