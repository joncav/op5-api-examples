#! /usr/bin/python

 # For hosts or services with special characters, be sure to URL encode the name. 
 # For names with back slashes, you will need to double encode the slashes to escape them, / should be escaped and encoded like %2F%2F.


import json
import requests

# Ignore the self-signed cert for this demonstration.
# NOT recommended for production!
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

user = "changeme"
password = "changeme"
hostname = "changeme"

url = "https://%s/api" % (hostname)

# To print the URL created by the request you're submitting
print url

# Query for host
# See: https://{your-op5-server}/api/help/status/host
host = "monitor"
r = requests.get(url +'/status/host?format=json&name=%s' % (host), auth=(user, password), verify=False)
#print r.text
print json.dumps(r.json(), indent=2)

# Query for service on host (this is not complete yet)
# See: https://{your-op5-server}/api/help/status/service
# host = raw_input("Enter the host to query: ")
# service = raw_input("Enter the service on " + host + " to query: ")
# payload = {'format' : 'json', 'check_command' : service, 'name' : host}
# r = requests.get(url +'/status/service', params=payload , auth=(user, password), verify=False)
# print r.text

# ADD host
# See: https://{your-op5-server}/api/help/config/host
# data = {
# 	"file_id": "etc/hosts.cfg",
# 	"host_name": "test_host",
# 	"max_check_attempts": "3",
# 	"notification_interval": "10",
# 	"notification_options": ["d","r"],
# 	"notification_period": "24x7",
# 	"template": "default-host-template"
# }
# r = requests.post(url +'/config/host', verify=False, data=json.dumps(data), auth=(user, password), verify=False, headers={'content-type': 'application/json'})
# print r.text

# ADD service
# See: https://{your-op5-server}/api/help/config/service
# data = {
# 	"check_command": "check_nrpe",
#   "check_command_args": "load",
# 	"check_interval": "5",
# 	"check_period": "24x7",
# 	"file_id": "/etc/service",
# 	"host_name": "AP101",
# 	"max_check_attempts": "3",
# 	"notification_interval": "10",
# 	"notification_options": ["d","r"],
# 	"notification_period": "24x7",
# 	"retry_interval": "1",
# 	"service_description": "Checking Load Test",
# 	"template": "default-service"
# }
# r = requests.post(url +'/config/service', verify=False, data=json.dumps(data), auth=(user, password), verify=False, headers={'content-type': 'application/json'})
# print r.text

# UPDATE service
# See "patch": https://{your-op5-server}/api/help/config/service
# Exaple URL: https://demo.op5.com/api/config/service/<yourhost>;<yourservice>?parent_type=host
# Example to update Hostgroup Service: https://demo.op5.com/api/config/service/<yourhostgroup>;<yourservice>?parent_type=host_group
# host = "host-name"
# service = "service-name"
#
# data = {
#     "check_command_args": "args-to-update"
# }
#
# r = requests.patch(url +'/config/service/' +host +';' +service,  verify=False, data=json.dumps(data), auth=(user, password), headers={'content-type': 'application/json'})
# print r.url
# print r.text

# Review the update
# See: https://{your-op5-server}/api/help/config/change
# r = requests.get("https://{your-op5-server}/api/config/change", verify=False, auth=(user, password), verify=False, headers={'content-type': 'application/json'})
# print r.text

# Commit changes (post)
# See: https://{your-op5-server}/api/help/config/change
# r = requests.post("https://{your-op5-server}/api/config/change", verify=False, auth=(user, password), verify=False, headers={'content-type': 'application/json'})
# print r.text

#GET last status, perf_data for a single check
# host = "host-name"
# service = "service-name"
# data = {
#     "perf_data": ""
# }
#
# r = requests.get(url +'/status/service/' +host +';' +service,  verify=False, auth=(user, password), headers={'content-type': 'application/json'})
# json_data = json.loads(r.text)
# print r.url
# # print r.text
# print(json_data['perf_data'])
