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
	- iPhone 5s *(Partial support)*
	- iPhone 6 *(Partial support)*
	- iPhone 6 Plus *(Partial support)*
	- iPhone 6s
	- iPhone 6s Plus
	- iPhone 7
	- iPhone 7 Plus
	- iPhone 8
	- iPhone 8 Plus
	- iPhone X
	- iPhone XS
	- iPhone XS Max
	- iPhone XR
	- iPhone 11
	- iPhone 11 Pro
	- iPhone 11 Pro Max
	- iPhone 12
	- iPhone 12 mini
	- iPhone 12 Pro
	- iPhone 12 Pro Max
	- iPhone 13
	- iPhone 13 mini
	- iPhone 13 Pro
	- iPhone 13 Pro Max
	- iPhone SE (1st generation)
	- iPhone SE (2nd generation)
	- iPad (5th generation)
	- iPad (6th generation)
	- iPad (7th generation)
	- iPad (8th generation)
	- iPad (9th generation)
	- iPad mini (2nd generation) *(Partial support)*
	- iPad mini (3rd generation) *(Partial support)*
	- iPad mini (4th generation) *(Partial support)*
	- iPad mini (5th generation)
	- iPad mini (6th generation)
	- iPad Air (1st generation) *(Partial support)*
	- iPad Air (2nd generation) *(Partial support)*
	- iPad Air (3rd generation)
	- iPad Air (4th generation)
	- 9.7-inch iPad Pro
	- 10.5-inch iPad Pro
	- 11-inch iPad Pro (1st generation)
	- 11-inch iPad Pro (2nd generation)
	- 11-inch iPad Pro (3rd generation)
	- 12.9-inch iPad Pro (1st generation)
	- 12.9-inch iPad Pro (2nd generation)
	- 12.9-inch iPad Pro (3rd generation)
	- 12.9-inch iPad Pro (4th generation)
	- 12.9-inch iPad Pro (5th generation)
	- iPod touch (6th generation) *(Partial support)*
	- iPod touch (7th generation)
### Software
The below list doesn't include the various components of the PiBeacon project itself.
- [PiBakery](http://www.pibakery.org)
- macOS or Windows *(Any one version from the sub-list required)*
	- macOS Mavericks *(Partial support)*
	- macOS Yosemite *(Partial support)*
	- macOS El Captian *(Partial support)*
	- macOS Sierra
	- macOS High Sierra
	- macOS Mojave
	- macOS Catalina
	- macOS Big Sur
	- macOS Monterey
	- Windows Vista *(Partial support)*
	- Windows 7 *(Partial support)*
	- Windows 8 *(Partial support)*
	- Windows 10 *(Partial support)*
	- Windows 11 *(Partial support)*
- iOS or iPadOS *(Any one version from the sub-list required)*
	- iOS 11
	- iOS 12
	- iOS 13
	- iOS 14
	- iOS 15
	- iPadOS 13
	- iPadOS 14
	- iPadOS 15

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
15. Install [iOS/iPadOS client app](https://link.gerzer.net/pibeacon-mobile)
16. In iOS/iPadOS app, tap "Add Beacon"
17. Follow in-app instructions to configure beacon
