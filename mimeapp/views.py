from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data="""<tables><tr><th>id</th>   <th>name</th>  <th>salary</th></tr><br>
<tr><td>001</td>  <td>uma</td>    <td>6000000</td></tr><br>
<tr><td>002</td>  <td>sri</td>    <td>4300000</td></tr><br>
<tr><td>003</td>  <td>mohan</td>    <td>4200000</td></tr></table>"""
class htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-excel")
class xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")

