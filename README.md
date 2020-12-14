# Wifi-Confusion
##### Created by: ExceptionRegret
# Wifi-Confusion is used to create to Fake Wifi Acess-Points to Confuse the Victim

  **!Notice : Educational purpose only not for any illegal activites.I'm not responsible for anything you did wrong with code**
  
# Features!

  - Massive generation of fake wifi access points
  - Access montior mode in easy way

# Usage:
```sh
$ git clone https://github.com/ExceptionRegret/Wifi-Confusion.git
$ cd Wifi-Confusion
$ python3 setup.py
$ python3 wifi-confusion.py
```
# Additional Information:

***Find your external wificard interface***
```sh
$iwconfig
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     unassociated  Nickname:"<WIFI@REALTEK>"
          Mode:Managed  Frequency=2.457 GHz  Access Point: Not-Associated   
          Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality=0/100  Signal level=0 dBm  Noise level=0 dBm
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
```
##### In above example the external wificard interface is wlan0

#Let's Confuse✌️
