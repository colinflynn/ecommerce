from django.db import models

class RetailStore(models.Model):
	store_id = models.AutoField(primary_key=True)
	store_name = models.CharField(max_length=50)
	store_abv = models.CharField(max_length=5)
	store_picture = models.ImageField(upload_to="images/retail_stores")

