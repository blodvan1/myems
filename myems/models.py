from django.db import models
from django.db.models import Max

import os

from django.core.files.storage import FileSystemStorage
from stdimage.models import StdImageField

class LocalFileSystemStorage(FileSystemStorage):


	def get_available_name(self, name, max_length=None):

		if os.path.exists(self.path(name)):

			# check if thumb nails removed also

			os.remove(self.path(name))

		return name

fs = LocalFileSystemStorage()



class Department(models.Model):
	dept_no = models.CharField(primary_key=True, max_length=4)
	dept_name = models.CharField(unique=True, max_length=40)

	class Meta:
		db_table = 'departments'

	def __str__(self):
			return "%s" % (self.dept_name)

def upload_path_handler(self, filename):

	return u'profile/user_{id}/{file}'.format(id=self.pk, file=filename)



class Employee(models.Model):

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	emp_no = models.IntegerField(primary_key=True)
	birth_date = models.DateField()
	first_name = models.CharField(max_length=14)
	last_name = models.CharField(max_length=16)
	gender = models.CharField(max_length=1)
	ib_admin = models.IntegerField(max_length=1)
	ib_unstuffing = models.IntegerField(max_length=1)
	ib_putaway = models.IntegerField(max_length=1)
	#gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
	hire_date = models.DateField()
	#profile_pic = models.ImageField(null=True, blank=True)
	departments = models.ManyToManyField(Department, related_name = 'departments', through = 'DeptEmp')
	image = StdImageField(upload_to=upload_path_handler, storage=fs, null=True, blank=True, max_length=255, variations={
			'large': (600, 400),
			'thumbnail': (100, 100, True),
			'medium': (300, 200),
		})
	#on_delete=models.CASCADE,

	

	def __str__(self):
		return "first_name = %s, last_name = %s" % (self.first_name, self.last_name)

	class Meta:
		db_table = 'employees'

def generate_next_emp_no():
	return 1 if Employee.objects.all().count() == 0 else Employee.objects.all().aggregate(Max('emp_no'))['emp_no__max'] + 1

class DeptEmp(models.Model):
	emp_no = models.ForeignKey(Employee, db_column='emp_no', on_delete=models.CASCADE)
	dept_no = models.ForeignKey(Department, db_column='dept_no', on_delete=models.CASCADE)
	from_date = models.DateField()
	to_date = models.DateField()
   
	class Meta:
		db_table = 'dept_emp'
		unique_together = (('emp_no', 'dept_no'),)


class Salary(models.Model):
	emp_no = models.ForeignKey(Employee, db_column='emp_no', related_name = 'employeeSalaries', on_delete=models.CASCADE)
	salary_amount = models.IntegerField()
	from_date = models.DateField()
	to_date = models.DateField()

	class Meta:
		db_table = 'salaries'
		unique_together = (('emp_no', 'from_date'),)


class Titles(models.Model):
	emp_no = models.ForeignKey(Employee, db_column='emp_no', related_name = 'employeeTitles', on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	from_date = models.DateField()
	to_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'titles'


class Dg(models.Model):	
	id = models.IntegerField(primary_key=True)
	commercial_designation_in_english = models.CharField(max_length=100)
	code_ean13 = models.CharField(max_length=50)
	commercial_reference = models.CharField(max_length=50)
	un_code = models.CharField(max_length=50)

	class Meta:
		db_table = 'dg_gen'

	def __str__(self):
		return "ID = %s, Part name = %s, EAN13 = %s" % (self.id, self.commercial_designation_in_english, self.code_ean13)

def generate_next_id_no():
	return 1 if Dg.objects.all().count() == 0 else Dg.objects.all().aggregate(Max('id'))['id__max'] + 1