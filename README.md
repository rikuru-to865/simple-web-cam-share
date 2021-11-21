# simple-web-cam-share
![main](https://user-images.githubusercontent.com/54424613/142750755-1c83a6c3-583b-4235-a619-f09506d2c099.gif)
this is virtual camera,You should be able to run normally
## Overview
You can easily share the webcam image by specifying the ip and port and executing it.

## Requirement
### client:  
opencv-python  
socket  
sys
### server:  
socket  
numpy  
sys  
opencv-python  
 ## Usage
 Start the server first
 ```
 python server.py 1000 #python server.py port
 ```
 Start the clinet secound
 ```
 python client.py 127.0.0.1 1000 0 #python client.py ip port cam_num(It's usually 0)
 ```
