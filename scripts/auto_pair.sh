#!/bin/bash
ADB=adb

while true; do
  for serial in $($ADB devices | grep -w device | awk '{print $1}'); do
    echo "Detected USB device: $serial"
    ip=$($ADB -s $serial shell ip route | grep wlan0 | awk '{print $9}')
    if [ -n "$ip" ]; then
      echo "Found IP: $ip. Switching to TCP."
      $ADB -s $serial tcpip 5555
      sleep 1
      $ADB connect $ip
      $ADB -s $serial shell am broadcast -a com.questmdm.SETUP_COMPLETE
    else
      echo "No IP found, pushing fallback Wi-Fi config."
      $ADB -s $serial shell svc wifi enable
      $ADB -s $serial shell am start -a android.settings.WIFI_SETTINGS
      # Optionally push a Wi-Fi config if supported by Quest
    fi
  done
  sleep 10
done
