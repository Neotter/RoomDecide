# RoomDecide
Use wireless iBeacon receiver receive beacon signal,then according to RSSI set a threshold to decide which room beacon are in.

老板叫我做一个房间定位的系统,直接就买个蓝牙beacon收集器做了

后台除了Flask的做的后端之外,还需要搭建一个MQTT的转发服务器,最后通过网页显示在哪个房间
