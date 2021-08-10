from django.db import models
from django.contrib.auth import get_user_model
# from crum import get_current_user
from core.utils import auto_save_current_user

User = get_user_model()

class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    text = models.CharField( max_length=250,blank=True,null=True)
    image = models.ImageField(upload_to = 'post_images')
    user = models. ForeignKey(User, on_delete=models.PROTECT,editable=False) 
    # since in this we only one time access user model that's why 
    # django by default set realative name as ModelName_set
    #django internally id to name -> user_id
    # editable=False --> it hide this field in form table of model
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Post, self).save(*args, **kwargs)

    @property
    def likes_count(self):
        count=self.like_set.count()
        return count

    @property
    def comments_count(self):
        count=self.comment_set.count()
        return count


    # to run save method of parent class from child class

class Comment(models.Model):
    text = models.CharField( max_length=150)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models. ForeignKey(User, on_delete=models.CASCADE,editable=False)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.pk)
    
    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Comment, self).save(*args, **kwargs)

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) # like_set is default relative name set by django default
    user = models. ForeignKey(User, on_delete=models.CASCADE,editable=False)
    # is_like = models.BooleanField(default=True)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.post.id)
    
    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Like, self).save(*args, **kwargs)

class Follow(models.Model):
    # since we can used User table in 2 fields hence got Reverse accessor warning
    # to fix this assign diff related_name
    user = models.ForeignKey(User,related_name='follow_follower', on_delete=models.CASCADE,editable=False)
    followed = models.ForeignKey(User,related_name='follow_followed', on_delete=models.CASCADE)
    # is_follow = models.BooleanField(default=True)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"(self.user) -->  (self.follower)"

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(Follow, self).save(*args, **kwargs)

class SavedPost(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    saved_on = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return str(self.post.pk)

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(SavedPost,self).save(*args,**kwargs)

