from django.db import models

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=20)
	body = models.TextField()		
	created = models.DateTimeField(auto_now_add=True)	  # auto generates a date it was made
	slug = models.SlugField(max_length=200, unique=True)  # field that generates a url


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blog Entry"  # the verbose are purely for admin interface
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]      # orders them in reverse chron. order