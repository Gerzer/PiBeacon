# PiBeacon
Low-cost iBeacon platform using Raspberry Pi

## Components
All components are required unless stated otherwise.
### Hardware
- [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
- [Raspberry Pi Zero Case](https://www.raspberrypi.org/products/raspberry-pi-zero-case/) *(Optional)*
- microUSB cable
- 4 GB or larger microSD card
- microSD to SD card adapter *(Required unless you're able to write to a microSD card directly from your computer)*
- Computer capable of writing to an SD card
- iPhone, iPad, or iPod touch *(Any one device from the sub-list required)*
	- iPhone 4s *(Support planned)*
	- iPhone 5 *(Support planned)*
	- iPhone 5s *(Partial support)*
	- iPhone 5c *(Support planned)*
	- iPhone 6 *(Partial support)*
	- iPhone 6 Plus *(Partial support)*
	- iPhone 6s
	- iPhone 6s Plus
	- iPhone SE
	- iPhone 7
	- iPhone 7 Plus
	- iPhone 8
	- iPhone 8 Plus
	- iPhone X
	- iPad (3rd generation) *(Support planned)*
	- iPad (4th generation) *(Support planned)*
	- iPad (5th generation)
	- iPad mini *(Support planned)*
	- iPad mini 2 *(Partial support)*
	- iPad mini 3 *(Partial support)*
	- iPad mini 4 *(Partial support)*
	- iPad Air *(Partial support)*
	- iPad Air 2 *(Partial support)*
	- 9.7-inch iPad Pro
	- 10.5-inch iPad Pro
	- 12.9-inch iPad Pro (1st generation)
	- 12.9-inch iPad Pro (2nd generation)
	- iPod touch (5th generation) *(Support planned)*
	- iPod touch (6th generation) *(Partial support)*
### Software
The below list doesn't include the various components of the PiBeacon project itself.
- [PiBakery](http://www.pibakery.org)
- macOS or Windows *(Any one version from the sub-list required)*
	- macOS Mavericks *(Partial support)*
	- macOS Yosemite *(Partial support)*
	- macOS El Captian *(Partial support)*
	- macOS Sierra
	- macOS High Sierra
	- Windows Vista *(Partial support)*
	- Windows 7 *(Partial support)*
	- Windows 8 *(Partial support)*
	- Windows 10 *(Partial support)*
- iOS *(Any one version from the sub-list required)*
	- iOS 11  
	*Support for older versions of iOS is under development.*

## Instructions
1. Open PiBakery
2. Click "Import"
3. Navigate to "PiBakery Recipe.xml"
4. Replace "network-name" with your Wi-Fi network name
5. Configure Wi-Fi authentication
	- WPA and WPA 2 networks
		1. Replace "network-password" with your Wi-Fi network password
	- WEP networks
		1. Change "WPA/WPA2" to "WEP" from dropdown menu
		2. Replace "network-password" with your Wi-Fi network password
	- Open networks
		1. Change "WPA/WPA2" to "Open (no password)" from dropdown menu
6. Replace "pibeacon" with a custom hostname *(Optional)*
7. Insert SD card
8. Click "Write"
9. Change "Raspbian Full" to "Raspbian Lite" from dropdown menu
10. Click "OK"
11. Click "Start Write"
12. When ready, eject SD card
13. Insert SD card into Raspberry Pi
14. Connect Raspberry Pi to power source
15. Install [iOS client app](https://link.gerzer.net/pibeacon-mobile)
16. In iOS app, tap "Add Beacon"
17. Follow in-app instructions to configure beacon
