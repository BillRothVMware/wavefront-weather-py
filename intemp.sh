#!/bin/bash

#
# first, call the api, then parse for the inside temperature
t=`curl -s 'https://api.ambientweather.net/v1/devices?applicationKey=<app-key>&apiKey=<api-key>' | jq '.[0].lastData.tempinf'`
#
# Output in Wavefront format: http://wavefront.com/sign-up/
#
echo "broth.home.weather.intempf" ${t} "source=ambient dc=willow-glen user=broth@vmware.com"
