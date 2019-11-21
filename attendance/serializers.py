from rest_framework import serializers
from .models import Hostel, Mess, Student, HostelStudent, Attendance, Year
from django.contrib.auth.models import User
import json
class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }

class MessSerializer(serializers.ModelSerializer):
    # organization_profile = OrganizationProfileSerializer(required=False)
    # org_type_name = serializers.SerializerMethodField()
    # status_name = serializers.SerializerMethodField()
    # def get_org_type_name(self, obj):
    #         if obj.org_type:
    #             return obj.org_type.type_name
    #         else:
    #             return ""
    # def get_status_name(self, obj):
    #         if obj.status:
    #             return obj.status.status_name
    #         else:
    #             return ""
    class Meta:
        model = Mess
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }

class HostelStudentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    register_number = serializers.SerializerMethodField()
    branch = serializers.SerializerMethodField()
    def get_student_name(self, obj):
        if obj.student:
            return obj.student.student_name
        else:
            return ""
    def get_register_number(self, obj):
        if obj.student:
            return obj.student.register_number
        else:
            return ""
    def get_branch(self, obj):
        if obj.student:
            return obj.student.branch
        else:
            return ""
    class Meta:
        model = HostelStudent
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }
class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }