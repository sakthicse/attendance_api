from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Hostel, Mess, Student, HostelStudent, Attendance, HostelRC, Year
from .serializers import HostelSerializer, MessSerializer, StudentSerializer, HostelStudentSerializer, AttendanceSerializer, YearSerializer
from rest_framework.views import APIView
import datetime
from rest_framework import permissions
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone
import pytz
from django.http import JsonResponse
from django.db.models import Q
# from master_api.views import get_role
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    def get_paginated_response(self, data):
        return Response({
            # 'links': {
            #    'next': self.get_next_link(),
            #    'previous': self.get_previous_link()
            # },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
class HostelView(viewsets.ModelViewSet):

    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer


    def get_queryset(self):
        queryset = Hostel.objects.all()
        
        return queryset
    def perform_create(self, serializer):
    	serializer.save(created_by=self.request.user,modified_by=self.request.user,created_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)))
    def perform_update(self, serializer):
    	serializer.save(modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_by=self.request.user)

class MessView(viewsets.ModelViewSet):

    queryset = Mess.objects.all()
    serializer_class = MessSerializer


    def get_queryset(self):
        queryset = Mess.objects.all()
        
        return queryset
    def perform_create(self, serializer):
    	serializer.save(created_by=self.request.user,modified_by=self.request.user,created_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)))
    def perform_update(self, serializer):
    	serializer.save(modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_by=self.request.user)
    	
class StudentView(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get_queryset(self):
        queryset = Student.objects.all()
        
        return queryset
    def perform_create(self, serializer):
    	serializer.save(created_by=self.request.user,modified_by=self.request.user,created_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)))
    def perform_update(self, serializer):
    	serializer.save(modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_by=self.request.user)

class HostelStudentView(viewsets.ModelViewSet):

    queryset = HostelStudent.objects.all()
    serializer_class = HostelStudentSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = HostelStudent.objects.all()
        
        search = self.request.query_params.get('search', None)
        purpose = self.request.query_params.get('purpose', None)
        current_year = self.request.query_params.get('current_year', None)
        if current_year:
            print("CURRR...")
            print(current_year)
            hostel_rc = HostelRC.objects.filter(rc_id=self.request.user.id,year_id=current_year).last()
            if hostel_rc:
            	queryset = queryset.filter(hostel_id = hostel_rc.hostel)
            else:
                queryset = []
        else:
            queryset = []
        # organization = self.request.query_params.get('organization', None)
        # if organization is not None:
        #     queryset = queryset.filter(organization_id=organization)
        if search:
            queryset = queryset.filter(Q(student__student_name__icontains=search)|Q(student__register_number__icontains=search))
        if purpose=='form' and queryset:
            self.pagination_class.page_size = len(queryset)
        return queryset
    def perform_create(self, serializer):
    	serializer.save(created_by=self.request.user,modified_by=self.request.user,created_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)))
    def perform_update(self, serializer):
    	serializer.save(modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_by=self.request.user)

class AttendanceView(viewsets.ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        current_date = datetime.datetime.now(tz=timezone.utc)
        
        queryset = Attendance.objects.all()
        search = self.request.query_params.get('search', None)
        purpose = self.request.query_params.get('purpose', None)
        if search:
            queryset = queryset.filter(organization_id=search)
        queryset = queryset.filter(attendance_at__startswith=datetime.date(current_date.year,current_date.month,current_date.day))
        if search:
            queryset = queryset.filter(Q(hostel_student__student__student_name__icontains=search)|Q(hostel_student__student__register_number__icontains=search))
        if purpose=='form' and queryset:
            self.pagination_class.page_size = len(queryset)
        return queryset
    def perform_create(self, serializer):
    	serializer.save(created_by=self.request.user,modified_by=self.request.user,created_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)))
    def perform_update(self, serializer):
    	serializer.save(modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_by=self.request.user)
class SaveAttendance(APIView):
    def get(self,request):
        pass
    def post(self,request):
        current_date = datetime.datetime.now(tz=timezone.utc)
        data = request.data
        print(data)
        for ke in data.keys():
            attendance_obj = Attendance.objects.filter(attendance_at__startswith=datetime.date(current_date.year,current_date.month,current_date.day),hostel_student_id=ke).last()
            if not attendance_obj:
                attendance_obj = Attendance()
                attendance_obj.created_by_id = request.user.id
            attendance_obj.hostel_student_id = ke
            attendance_obj.is_present = data[ke]
            attendance_obj.modified_at = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
            attendance_obj.modified_by_id = request.user.id
            attendance_obj.save()
        datas = {"message": "success"}
        return Response(datas)

class YearView(viewsets.ModelViewSet):

    queryset = Year.objects.all()
    serializer_class = YearSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Year.objects.all()
        get_current_year = self.request.query_params.get('get_current_year', None)
        if get_current_year is not None:
            queryset = queryset.filter(is_active=True)
        return queryset
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,modified_by=self.request.user,created_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)))
    def perform_update(self, serializer):
        serializer.save(modified_at=datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)),modified_by=self.request.user)
class CheckCurrentYear(APIView):
    def get(self, request):
        data = request.GET
        year_id = data.get('year_id')
        check_year = Year.objects.filter(current_year=True).last()
        if check_year:
            if year_id:
                if str(check_year.id) == str(year_id):
                    datas = {"already_exit": False}
                else:
                    datas = {"already_exit": True}
            else:
                datas = {"already_exit": True}
        else:
            datas = {"already_exit": False}
        return Response(datas)
class CheckYear(APIView):
    def get(self, request):
        data = request.GET
        year = data.get('year')
        message = ""
        if year:
            hostel_rc = HostelRC.objects.filter(Q(year_id=year))
            if hostel_rc:
                message = "Hostel RC"
            hostel_student = HostelStudent.objects.filter(Q(year_id=year))
            if hostel_student:
                if message:
                    message = message + ", Hostel Student"
                else:
                    message = "Hostel Student"
        is_dependent = False
        if message:
            is_dependent = True
        response_data = {"is_dependent": is_dependent, "message": message}
        return JsonResponse(response_data)