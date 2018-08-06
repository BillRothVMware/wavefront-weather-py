#!/bin/bash

t=`curl -s 'https://api.ambientweather.net/v1/devices?applicationKey=<app-key>&apiKey=<api-key)' | jq '.[0].lastData.tempinf'`
echo "broth.home.weather.intempf" ${t} "source=ambient dc=willow-glen user=broth
@vmware.com"
