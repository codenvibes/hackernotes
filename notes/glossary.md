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

