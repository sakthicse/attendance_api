""" Views for the base application """

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from build_hr.models import Contractor, DeviceWorkdayMapping, Location
import MySQLdb
from django.views.generic.base import TemplateView
import datetime

class Home(TemplateView):
    template_name = "base/home.html"
    def get(self,request):
        return render(request, self.template_name, {})
        # data = request.GET
        # location_id = data.get('location_id')
        # start_date = data.get('start_date')
        # end_date = data.get('end_date')
        # con_start_date = ""
        # con_end_date = ""
        # if start_date:
        # 	con_start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        # 	con_start_date = con_start_date.strftime("%Y-%m-%d")
        # else:
        # 	start_date = ""
        # if end_date:
        # 	con_end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        # 	con_end_date = con_end_date.strftime("%Y-%m-%d")
        # else:
        # 	end_date = ""
        # device_mapping = []
        # device_list = []
        # user_list = []
        # if location_id:
        # 	location = Location.objects.get(pk=location_id)
        # 	location_id = int(location_id)
        # 	db = MySQLdb.connect(location.host_name,location.user_name,location.password,location.database_name)
        # 	cursor = db.cursor()
        # 	cursor.execute("SELECT * FROM devices")
        # 	datas = cursor.fetchall()
        # 	cursor.execute("SELECT * FROM employees")
        # 	employee_datas = cursor.fetchall()
        # 	db.close()
        # 	for da in datas:
        # 		device_list.append({"device_id":da[0],"device_name":da[2]})
        # 	for emp in employee_datas:
        # 		user_list.append({"id":emp[0],"employee_id":emp[2]})
        # 	device_mapping = DeviceWorkdayMapping.objects.filter(location_id=location_id)
        # total_device_mapping = {}
        # for mapp in device_mapping:
        # 	if mapp.entry:
        # 		total_device_mapping[str(mapp.location.id)+"_"+str(mapp.device_id)+"_"+str(mapp.employee_id)] = True
        # locations = Location.objects.filter()
        # return render(request, self.template_name, {'device_list': device_list, 'user_list': user_list,"total_device_mapping":total_device_mapping,"location_id":location_id,"locations":locations,"start_date":start_date,"end_date":end_date})
    # def post(self,request):
    #     data = request.POST
    #     user_id = data.getlist('user_id')
    #     device_id = data.getlist('device_id')
    #     device_names = data.getlist('device_name')
    #     # raise Exception(device_names)
    #     location_id = data.get('location_id')
    #     for user in user_id:
    #         i=0
    #         for dev in device_id:
    #             device_name =device_names[i]
    #             name = "val_"+user+"_"+dev
    #             # print(name)
    #             value  = data.get(name)
    #             mapping = DeviceWorkdayMapping.objects.filter(location_id=location_id,contractor=user,device_id=dev).last()
    #             if not mapping:
    #                 mapping = DeviceWorkdayMapping()
    #             mapping.location_id=location_id
    #             mapping.contractor=user
    #             mapping.device_id=dev
    #             mapping.device_name = device_name
    #             if value:
    #                 mapping.entry = True
    #             else:
    #                 mapping.entry = False
    #             mapping.save()
    #             i=i+1
    #     return redirect('/?location_id=' + str(location_id))
