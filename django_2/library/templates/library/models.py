from import models
from django.contrib.auth.models import User

# --- Author Model ---

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# --- Genre Model ---

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# --- Book Model ---

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='books')
    published_date = models.DateField()

    def __str__(self):
        return self.title

# --- Post Model (related to Django User) ---

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
