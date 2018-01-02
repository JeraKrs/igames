from django.db import models

class game_save(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField()
	price = models.TextField()
	score = models.TextField()
	developer = models.TextField()
	publisher = models.TextField()
	description = models.TextField()
	review = models.TextField()
	category = models.TextField()
	advantage = models.TextField()
	disadvantages = models.TextField()
	language_number = models.TextField()
	save_time = models.DateField()
