# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.hashers import make_password
# from django.core.exceptions import ValidationError

# class Course(models.Model):
    # title = models.CharField(max_length=255)
    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
        # return self.title

# class Level(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='levels')
    # title = models.CharField(max_length=255)
    # order = models.PositiveIntegerField()  
    
    # class Meta:
        # ordering = ['order']
        # unique_together = ['course', 'order']  
    
    # def __str__(self):
        # return f"{self.course.title} - Уровень {self.order}: {self.title}"

# class UserLevelProgress(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    # level = models.ForeignKey(Level, on_delete=models.CASCADE)
    # is_completed = models.BooleanField(default=False)
    # completed_at = models.DateTimeField(null=True, blank=True)
    
    # class Meta:
        # unique_together = ['user', 'level']  
    
    # def clean(self):
        # # Если это ученик, проверяем, прошел ли родитель этот уровень
        # if self.user.role == 'STUDENT':
            # parent_progress = UserLevelProgress.objects.filter(
                # user=self.user.parent,
                # level=self.level,
                # is_completed=True
            # ).exists()
            
            # if not parent_progress:
                # raise ValidationError(
                    # 'Ученик не может пройти уровень, пока его не пройдет родитель!'
                # )
    
    # def save(self, *args, **kwargs):
        # self.clean()
        # super().save(*args, **kwargs)
    
    # def __str__(self):
        # return f"{self.user.username} → {self.level}"

# class Game(models.Model):
    # title = models.CharField(max_length=255)
    # description = models.TextField()
    # level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='games')
    
    # def __str__(self):
        # return f"{self.title} (Уровень: {self.level.order})"