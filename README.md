# PingStats
A CLI tool to help with ping logging and simple analyze, notify user when slow connection is detected

## Sample Output
```
64 bytes from 192.168.31.1: icmp_seq=405 ttl=64 time=1.147 ms
--------------------
Fast  393 96.80% [1.878, 1.163, 1.147]
Ok    10 2.46% [10.869, 15.297, 15.029]
Slow  2 0.49% [62.377, 117.331]
SSlow 0 0.00% []
Fail  1 0.25% ['Request timeout for icmp_seq 34']
--------------------
```
![ScreenShot](https://github.com/Meowzz95/PingStats/raw/master/ss.jpg)

## Usage
Just check the source and change parameters as needed

### Remark
Notification is only supported on Mac OS, will try a win version later
