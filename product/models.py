from django.db import models

class Product(models.Model):
	id		= models.AutoField(primary_key=True)
	name	= models.CharField(max_length=100)
	price	= models.IntegerField(default=0)
	desc	= models.CharField(max_length=255, null=True, blank=True)
	img		= models.FileField(upload_to='product/img', null=True, blank=True)
	category_id	= models.ForeignKey('category.Category', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = "product"
		db_table = "product"
