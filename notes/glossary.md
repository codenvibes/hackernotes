<h1 align="center"><b>GLOSSARY</b></h1>

<br>

## A
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## B
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## C
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## D
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## E
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## F
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## G
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## H
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## I
<details>
<summary><b><a href=" "> </a>ICMP</b></summary><br>

ICMP stands for ***Internet Control Message Protocol***. It is a network layer protocol that is used to send control messages and report errors between hosts and routers in an IP network. ICMP is an integral part of the Internet Protocol Suite (TCP/IP) and is used for various purposes, including:

1. **Error Reporting**: ICMP is used to report errors in packet delivery. For example, if a router receives an IP packet that it cannot forward, it will send an ICMP message back to the source indicating the nature of the problem.

2. **Diagnostic Tools**: ICMP is commonly used by diagnostic tools like `ping` and `traceroute`. `ping` uses ICMP echo requests and replies to test the reachability of a host and measure round-trip times, while `traceroute` uses ICMP time exceeded messages to map the route that packets take to reach a destination.

3. **Network Management**: ICMP messages are used by network administrators for various management tasks, such as discovering hosts on a network or checking the reachability of specific hosts.

ICMP messages are encapsulated within IP packets, and they do not carry any application data. Instead, they provide feedback about the network itself. ICMP messages are often used by network devices (such as routers) to communicate with each other and with hosts on the network to ensure efficient and error-free packet delivery.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## J
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## K
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## L
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## M
<details>
<summary><b><a href=" "> </a>MAC Address</b></summary><br>

MAC Address stands for Media Access Control Address.
MAC Address ensures that the physical address of the computer is unique.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a>MAC spoofing </b></summary><br>

**MAC Spoofing Overview:**

MAC spoofing is a technique used to change the Media Access Control (MAC) address of a network interface on a device. This allows a user to impersonate another device on a network and potentially carry out unauthorized actions.

**Importance in Network Hacking:**

MAC spoofing is significant in network hacking, particularly in attacks like Man-in-the-Middle, where an attacker intercepts communication between two parties.

**Steps to Change MAC Address:**

1. Disable the interface you want to change.
2. Change the MAC address.
3. Enable the interface.

***Remember:*** *Once we change the MAC address, it doesn't stay forever, once you restart the system, the original MAC automatically replaces the spoofed one*

**Command Line Instructions:**

To change the MAC address using the command line:

1) Disable the interface: `ifconfig etho down`<br>Here eth0 is the name of the interface we want to change the MAC for.<br>`down` is a parameter to the ifconfig command, indicating that the eth0 interface should be brought down or deactivated. When an interface is brought down, it effectively disables networking through that interface, meaning it will not be able to send or receive data until it is brought back up.
2) Change the MAC: `ifconfig etho hw ether 00:11:22:33:44:55`<br> Here 'hw' stands for hardware interface and '00:11:22:33:44:55' is the fake MAC that we have given to change the MAC. The Mac address will be changed to this given random address.
3) Enable the interface: `ifconfig etho up`
4) Now simply run the command `ifconfig` and check! The MAC address will be changed...

**Windows MAC Address Change:**

Technitium is a freeware utility to spoof the MAC address instantly. To change the MAC address on Windows using Technitium MAC Address Changer:

1. **Download and Install Technitium MAC Address Changer**:
   - If you haven't already, download and install Technitium MAC Address Changer from their official website (https://technitium.com/tmac/).

2. **Launch Technitium MAC Address Changer**:
   - Open the Technitium MAC Address Changer application on your Windows computer.

3. **Select Network Adapter**:
   - From the drop-down list of network adapters, select the adapter for which you want to change the MAC address.

4. **Change MAC Address**:
   - Click on the "Change" button to randomly generate a new MAC address or manually enter the MAC address you want to use. Note that the MAC address should be in the format xx-xx-xx-xx-xx-xx (where x is a hexadecimal digit).

5. **Apply Changes**:
   - Click on the "Change Now!" button to apply the new MAC address to the selected network adapter.

6. **Verify the Change**:
   - To verify that the MAC address has been changed, you can use the `ipconfig /all` command in Command Prompt or PowerShell and look for the "Physical Address" under the network adapter you modified. It should now display the new MAC address.

7. **Revert to Original MAC Address**:
   - If you want to revert to the original MAC address, simply select the network adapter again in Technitium MAC Address Changer, click on the "Restore Original" button, and then click "Change Now!" to apply the change.

8. **Verify the Reversion**:
   - Again, use the `ipconfig /all` command to verify that the MAC address has been reverted to its original value.

**Preventing MAC Spoofing:**

- MAC Locking: Lock a MAC address to a specific physical port on the switch to prevent its use on other ports.
- ARP Tables: Use static ARP tables in combination with routing tables to prevent spoofing.


Real Life Facts
- MAC Address is not an attack that will give you access to systems, but it will play a very important role in network hacking.
- MAC Spoofing is one of the important steps in Wifi Hacking.
- Heard of something called MITM (Man In The Middle) Attacks? MAC Spoofing plays a very important role there as well.
- You can change your MAC to the MAC of another system and pretend to be someone else. Thus you can sit in the middle of the network and intercept it.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## N
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## O
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## P
<details>
<summary><b><a href=" "> </a>payload</b></summary><br>

A **payload** is a specific piece of code or software that is delivered to a target system as part of an exploit. The payload is designed to execute a certain action on the compromised system once the vulnerability is exploited.
<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a><code>ping</code></b></summary><br>

The `ping` command is used to test the reachability of a host on an IP network. Here's how you can use it:

Basic usage:
```
ping [options] <hostname or IP address>
```

Replace `<hostname or IP address>` with the hostname or IP address of the target you want to ping.

Example:
```
ping google.com
```
This command will send ICMP echo requests to `google.com` and show you the round-trip time for each packet and whether the packets were received successfully.

Common options:
- `-c count`: Specifies the number of ICMP echo requests to send before stopping.
- `-i interval`: Specifies the interval between sending each ICMP echo request.
- `-w deadline`: Specifies a timeout, after which `ping` will stop sending ICMP echo requests.
- `-s packetsize`: Specifies the size of the ICMP echo request packets.

Example with options:
```
ping -c 5 -i 1 google.com
```
This command will send 5 ICMP echo requests to `google.com` with an interval of 1 second between each request.

Using `ping` with IP ranges:
If you want to ping a range of IP addresses, you can use a loop in a script, similar to the one in your original question.

For example, to ping a range of IP addresses from `192.168.1.1` to `192.168.1.254`, you could use a script like this:
```bash
#!/bin/bash

for ip in {1..254}; do
    ping -c 1 192.168.1.$ip | grep "64 bytes" &
done
```
Save this script to a file (e.g., `ping_range.sh`), make it executable with `chmod +x ping_range.sh`, and then run it with `./ping_range.sh`. This script will send a single ICMP echo request to each IP address in the range and print the results for each address that responds.

Remember that using `ping` to scan a large range of IP addresses can generate a lot of network traffic and may be considered intrusive or abusive by network administrators. Always make sure you have permission to perform such scans on a network.

<br><p align="center">※※※※※※※※※※※※</p><br>

The output of the `ping` command provides information about the status of the network connection between your computer and the target host (specified by its IP address or hostname).

Here's an example of a typical `ping` output:
```
PING google.com (216.58.200.110) 56(84) bytes of data.
64 bytes from 216.58.200.110: icmp_seq=1 ttl=55 time=13.2 ms
64 bytes from 216.58.200.110: icmp_seq=2 ttl=55 time=12.8 ms
64 bytes from 216.58.200.110: icmp_seq=3 ttl=55 time=12.8 ms
64 bytes from 216.58.200.110: icmp_seq=4 ttl=55 time=12.7 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3001ms
rtt min/avg/max/mdev = 12.727/12.936/13.236/0.205 ms
```

In this example:
- The first line shows the target host (google.com) and its IP address (216.58.200.110).
- The following lines show the individual ping responses, each indicating the size of the response, the sequence number of the ICMP echo request, the TTL value, and the round-trip time.
- The summary at the end shows that 4 packets were transmitted and received without any loss. It also provides the minimum, average, maximum, and standard deviation of the round-trip times for the received packets.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## Q
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## R
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## S
<details>
<summary><b><a href=" "> </a>SOC analyst</b></summary><br>

A Security Operations Center (SOC) analyst is a cybersecurity professional responsible for monitoring and analyzing an organization's security posture. Their primary role is to detect, analyze, and respond to security incidents and threats within an organization's IT infrastructure.
<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## T
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## U
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## V
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## W
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## X
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## Y
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

## Z
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

