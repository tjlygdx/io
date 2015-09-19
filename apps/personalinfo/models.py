import datetime
from django.db import models

class MyInfo(models.Model):
	name = models.CharField(max_length=128, default='unknown')
	birthday = models.DateField(auto_now_add=False, default=datetime.datetime.now)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=64, default='Male', choices=GENDER_CHOICES)
	email = models.EmailField(max_length=64, default='example@iolala.com')
	qq = models.CharField(max_length=64, default='1234567890', verbose_name='QQ')
	is_show_qq = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'ME'

	def __unicode__(self):
		return self.name

class MyWorks(models.Model):
	name = models.CharField(max_length=128, default='io')
	homepage = models.CharField(max_length=256, default='www.iolala.com')
	desc = models.TextField(null=True, default='This is a ...')

	class Meta:
		verbose_name_plural = 'Works'

	def __unicode__(self):
		return self.name
