#
# Pulling data from WUnderground and sending to Wavefront by Python
#
# Core original code written by Durren Shen @durrenshen 
# in a blog at https://www.wavefront.com/weather-metrics/
# 
# Cleaned up by Bill Roth @BillRothVMware
#
import urllib2
import json
import logging
import socket
import sys
import time
import re
import syslog

sock = socket.socket()
sock.connect(('127.0.0.1', 2878))
sourceName = 'BrothPWS'

f = urllib2.urlopen('http://api.wunderground.com/api/6bea16c68a4066e9/conditions/q/pws:KCASANJO821.json')
json_string = f.read()
parsed_json = json.loads(json_string)

temp_f = parsed_json['current_observation']['temp_f']
sock.sendall('weather.temp_f ' + str(temp_f) + ' source=' + sourceName + ' \n')

humidity = parsed_json['current_observation']['relative_humidity']
sock.sendall('weather.humidity ' + re.sub("[^0-9]", "", str((humidity))) + ' source=' + sourceName + ' \n')

wind_degrees = parsed_json['current_observation']['wind_degrees']
sock.sendall('weather.wind_degrees ' + str(wind_degrees) + ' source=' + sourceName + ' \n')

wind_mph = parsed_json['current_observation']['wind_mph']
sock.sendall('weather.wind_mph ' + str(wind_mph) + ' source=' + sourceName + ' \n')

wind_gust_mph = parsed_json['current_observation']['wind_gust_mph']
sock.sendall('weather.wind_gust_mph ' + str(wind_gust_mph) + ' source=' + sourceName + ' \n')

pressure_in = parsed_json['current_observation']['pressure_in']
sock.sendall('weather.pressure_in ' + str(pressure_in) + ' source=' + sourceName + ' \n')

pressure_trend = parsed_json['current_observation']['pressure_trend']
sock.sendall('weather.pressure_trend ' + str(pressure_trend) + ' source=' + sourceName + ' \n')

dewpoint_f = parsed_json['current_observation']['dewpoint_f']
sock.sendall('weather.dewpoint_f ' + str(dewpoint_f) + ' source=' + sourceName + ' \n')

feelslike_f = parsed_json['current_observation']['feelslike_f']
sock.sendall('weather.feelslike_f ' + str(feelslike_f) + ' source=' + sourceName + ' \n')

visibility_mi = parsed_json['current_observation']['visibility_mi']
sock.sendall('weather.visibility_mi ' + str(visibility_mi) + ' source=' + sourceName + ' \n')

solarradiation = parsed_json['current_observation']['solarradiation']
sock.sendall('weather.solarradiation ' + str(solarradiation) + ' source=' + sourceName + ' \n')

UV = parsed_json['current_observation']['UV']
sock.sendall('weather.UV ' + str(UV) + ' source=' + sourceName + ' \n')

precip_1hr_in = parsed_json['current_observation']['precip_1hr_in']
sock.sendall('weather.precip_1hr_in ' + str(precip_1hr_in) + ' source=' + sourceName + ' \n')

precip_today_in = parsed_json['current_observation']['precip_today_in']
sock.sendall('weather.precip_today_in ' + str(precip_today_in) + ' source=' + sourceName + ' \n')

observation_epoch = parsed_json['current_observation']['observation_epoch']

syslog.syslog('Weather logged at ' + str(observation_epoch));

f.close()
sock.close()

