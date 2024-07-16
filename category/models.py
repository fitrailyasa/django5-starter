from django.db import models

class Category(models.Model):
	id		= models.AutoField(primary_key=True)
	name	= models.CharField(max_length=100)
	desc	= models.CharField(max_length=255, null=True, blank=True)
	img		= models.ImageField(upload_to='category/img', null=True, blank=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = "category"
		db_table = "category"
