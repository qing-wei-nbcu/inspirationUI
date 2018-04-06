from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Table(models.Model):
# exampe
class Article(models.Model):
	title=models.CharField("your article's title", max_length=50)
	author=models.CharField(max_length=50)
	created_date=models.DateField(auto_now_add=True)
	modify_date=models.DateField(auto_now=True)
	content=models.TextField()
	is_show=models.BooleanField()

	class Meta:
		db_table="article"

	def  __str__(self):
		#name every instance
		return self.title