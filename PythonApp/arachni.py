#!/usr/bin/env python
# -[i]- encoding: utf-8 -[/i]-
 
#https://github.com/Arachni/arachni/wiki/REST-server
#https://github.com/Arachni/arachni/wiki/REST-API
'''
开启api
arachni_rest_server 
[开启认证]
(./bin/arachni_rest_server  --address=192.168.87.134 --port=7331  --authentication-username=admin --authentication-password=adminpassword)
 
 
1.查看扫描状态
GET /scans
 
2.提交扫描
POST /scans
json.dumps(xxx.json)
其实需要提供的是url和profiles
 
3.查看某个id的状态
GET /scans/:id
 
状态大约有几种[
   a.ready 准备中。但是不曾启动扫描
   b.preparing  准备好了，随时可以启动扫描(即初始化插件)
   c.scanning   扫描中
   d.pausing   扫描被暂停了
   e.paused    扫描已经被停职了
   f.cleanup   扫描已经被中止(即等待插件完成等)
   g.aborted   扫描非正常状态结束
   h.done      扫描结束
]
 
4.暂停扫描
PUT /scans/:id/pause
 
5.开始[已暂停的]扫描
PUT /scans/:id/resume
 
6.提取扫描报告
GET /scans/:id/report
GET /scans/:id/report.json
GET /scans/:id/report.xml
GET /scans/:id/report.yaml
GET /scans/:id/report.html.zip
 
7.删除扫描
DELETE /scans/:id
 
'''
 
import urllib2
import json
 
class ArachniClient(object):
 
   with open('./profiles/default.json') as f:
      default_profile = json.load(f)
 
   def __init__(self, arachni_url = 'http://127.0.0.1:7331'):
      self.arachni_url = arachni_url
      self.options = ArachniClient.default_profile
 
   def get_http_request(self, api_path):
      return urllib2.urlopen(self.arachni_url + api_path).read()
 
   def post_api(self, api_path):
      options = json.dumps(self.options)
      request = urllib2.Request(self.arachni_url + api_path, options)
      request.add_header('Content-Type', 'application/json')
      return urllib2.urlopen(request).read()
 
   def put_request(self, api_path):
      request = urllib2.Request(self.arachni_url + api_path)
      request.get_method = lambda: 'PUT'
      return urllib2.urlopen(request).read()
 
   def delete_request(self, api_path):
      request = urllib2.Request(self.arachni_url + api_path)
      request.get_method = lambda: 'DELETE'
      return urllib2.urlopen(request).read()
   #获取扫描    
   def get_scans(self):
      return json.loads(self.get_http_request('/scans'))
   #获取扫描状态
   def get_status(self, scan_id):
      return json.loads(self.get_http_request('/scans/' + scan_id))
   #暂停扫描
   def pause_scan(self, scan_id):
      return self.put_request('/scans/' + scan_id + '/pause')
   #重启扫描
   def resume_scan(self, scan_id):
      return self.put_request('/scans/' + scan_id + '/resume')
   #获取扫描结果
   def get_report(self, scan_id, report_format = None):
      if self.get_status(scan_id)['status'] == 'done':
 
         if report_format == 'html':
            report_format = 'html.zip'
 
         if report_format in ['json', 'xml', 'yaml', 'html.zip']:
            return self.get_http_request('/scans/' + scan_id + '/report.' + report_format)
         elif report_format == None:
            return self.get_http_request('/scans/' + scan_id + '/report')
         else:
            print 'your requested format is not available.'
 
      else:
         print 'your requested scan is in progress.'
   #删除扫描
   def delete_scan(self, scan_id):
      return self.delete_request('/scans/' + scan_id)
   #开启扫描
   def start_scan(self):
      if self.options['url']:
         return json.loads(self.post_api('/scans'))
      else:
         print 'Target is not set!'
 
   def target(self, target_url):
      try:
         urllib2.urlopen(target_url)
         self.options['url'] = target_url
      except urllib2.HTTPError, e:
         print e.code
 
   def profile(self, profile_path):
      with open(profile_path) as f:
         self.options = json.load(f)
 
if __name__ == '__main__':
   a = ArachniClient()
   a.profile('./profiles/default.json')
   #'http://testphp.vulnweb.com/','http://23.88.112.156/xvwa/'
   a.target('https://acf49629d204.ngrok.io/')
   #print(a.start_scan())
   print a.get_status('277cddcd61aa225c1a8579a4ee9864ed')
   print a.get_report('277cddcd61aa225c1a8579a4ee9864ed', 'xml')
   
