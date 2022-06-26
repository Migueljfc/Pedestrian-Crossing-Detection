version: '2.4'
services:
    rsu:
        hostname: rsu
        restart: always
        image: code.nap.av.it.pt:5050/mobility-networks/vanetza:latest
        cap_add:
            - "NET_ADMIN"
        environment:
            - VANETZA_STATION_ID=1
            - VANETZA_STATION_TYPE=15
            - VANETZA_MAC_ADDRESS=6e:06:e0:03:00:01
            - VANETZA_INTERFACE=eth0
            - START_EMBEDDED_MOSQUITTO=true
            - VANETZA_CAM_PERIODICITY=0
        networks:
            vanetzalan0:
                ipv4_address: 192.168.0.10
        sysctls:      
            kernel.msgmax:  65536
            kernel.msgmnb:  65536

    obu1:
        hostname: car1
        restart: always
        image: code.nap.av.it.pt:5050/mobility-networks/vanetza:latest
        cap_add:
            - "NET_ADMIN"
        environment:
            - VANETZA_STATION_ID=2
            - VANETZA_STATION_TYPE=5
            - VANETZA_MAC_ADDRESS=6e:06:e0:03:00:02
            - VANETZA_INTERFACE=br0
            - START_EMBEDDED_MOSQUITTO=true
            - SUPPORT_MAC_BLOCKING=true
            - VANETZA_CAM_PERIODICITY=0
        networks:
            vanetzalan0:
                ipv4_address: 192.168.0.20
        sysctls:      
            kernel.msgmax:  65536
            kernel.msgmnb:  65536
   
    obu2:
        hostname: car2
        restart: always
        image: code.nap.av.it.pt:5050/mobility-networks/vanetza:latest
        cap_add:
            - "NET_ADMIN"
        environment:
            - VANETZA_STATION_ID=3
            - VANETZA_STATION_TYPE=5
            - VANETZA_MAC_ADDRESS=6e:06:e0:03:00:03
            - VANETZA_INTERFACE=br0
            - START_EMBEDDED_MOSQUITTO=true
            - SUPPORT_MAC_BLOCKING=true
            - VANETZA_CAM_PERIODICITY=0
        networks:
            vanetzalan0:
                ipv4_address: 192.168.0.30
        sysctls:      
            kernel.msgmax:  65536
            kernel.msgmnb:  65536    
       
    obu3:
        hostname: car3
        restart: always
        image: code.nap.av.it.pt:5050/mobility-networks/vanetza:latest
        cap_add:
            - "NET_ADMIN"
        environment:
            - VANETZA_STATION_ID=4
            - VANETZA_STATION_TYPE=5
            - VANETZA_MAC_ADDRESS=6e:06:e0:03:00:04
            - VANETZA_INTERFACE=br0
            - START_EMBEDDED_MOSQUITTO=true
            - SUPPORT_MAC_BLOCKING=true
            - VANETZA_CAM_PERIODICITY=0
        networks:
            vanetzalan0:
                ipv4_address: 192.168.0.40
        sysctls:      
            kernel.msgmax:  65536
            kernel.msgmnb:  65536      
networks:
  vanetzalan0:
    external: true
