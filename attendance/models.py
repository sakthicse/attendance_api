from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CommonFieldsModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	modified_at = models.DateTimeField(blank=True,null=True)
	# owner = models.ForeignKey(TaskUser, related_name="%(app_label)s_%(class)s_ownership")
	created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_by", on_delete=models.PROTECT)
	modified_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_modefied_by", null=True, blank=True,on_delete=models.PROTECT)
	class Meta:
		abstract = True

class Year(CommonFieldsModel):
	from_year = models.IntegerField(unique=True)
	to_year = models.IntegerField(unique=True)
	current_year = models.BooleanField(default=False)
	def __str__(self):
		return "{from_year} - {to_year}".format(from_year=str(self.from_year),to_year=str(self.to_year))
class Hostel(CommonFieldsModel):
	name = models.CharField(max_length=255,unique=True)
	def __str__(self):
		return self.name
class HostelRC(CommonFieldsModel):
	hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
	rc = models.ForeignKey(User,on_delete=models.CASCADE)
	year = models.ForeignKey(Year,on_delete=models.CASCADE)
	active = models.BooleanField(default=False)

	def __str__(self):
		return "{hostel} - {rc} - {from_year} - {to_year}".format(hostel=self.hostel.name,rc=self.rc.username,from_year=str(self.year.from_year), to_year=str(self.year.to_year))
	class Meta:
		unique_together=('hostel','rc','year')
class Mess(CommonFieldsModel):
	name = models.CharField(max_length=255,unique=True)
	def __str__(self):
		return self.name

class Student(CommonFieldsModel):
	GENDER = (("male","Male"),("female","Female"))
	FOOD_TYPES = (("veg","Veg"),("non_veg","Non Veg"))
	GRADUATE = (("ug","UG"),("pg","PG"))
	BRANCHS = (('cse','CSE'),('ece','ECE'))
	student_name = models.CharField(max_length=500)
	register_number = models.IntegerField()
	gender = models.CharField(max_length=15,choices=GENDER)
	graduate = models.CharField(max_length=15,choices=GRADUATE)
	year = models.CharField(max_length=15)
	branch = models.CharField(max_length=15,choices=BRANCHS)
	food_type = models.CharField(max_length=12,choices=FOOD_TYPES)
	contact_number = models.CharField(max_length=15)
	address = models.TextField(max_length=500)

	def __str__(self):
		return "{name}".format(name=self.student_name)

class HostelStudent(CommonFieldsModel):
	year = models.ForeignKey(Year,on_delete=models.CASCADE)
	hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	def __str__(self):
		return "{hostel}  - {from_year} - {to_year} - {student}".format(hostel=self.hostel.name,from_year=str(self.year.from_year), to_year=str(self.year.to_year),student=self.student.student_name)

class Attendance(CommonFieldsModel):
	attendance_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	hostel_student = models.ForeignKey(HostelStudent,on_delete=models.CASCADE)
	is_present = models.BooleanField(default=False)