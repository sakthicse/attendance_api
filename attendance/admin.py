from django.contrib import admin
from .models import Year, Hostel, HostelRC, Mess, Student, HostelStudent, Attendance, HostelMessStudent
# Register your models here.
admin.site.register(Year)
admin.site.register(Hostel)
admin.site.register(HostelRC)
admin.site.register(Mess)
admin.site.register(Student)
admin.site.register(HostelStudent)
admin.site.register(Attendance)
admin.site.register(HostelMessStudent)