# The Internet: Behind the Scenes

The Internet is a transport mechanism that lets any connected device communicate with any other connected device. Behind the scenes:

Each device has a globally distinct IP address, which is a 32 bit number. Usually an IP address is represented as a sequence of four decimal numbers, each number in the range (0, 255). For example, when I checked the IP address for my laptop just now, it was 141.211.203.248. Any IP address beginning with 141.211 is for a device at the University of Michigan. When I take my laptop home and connect to a network there, my laptop gets a different IP address that it uses there.

Data is chopped up into reasonable sized packets (up to 65,535 bytes, but usually much smaller).

Each data packet has a header that includes the destination IP address.

Each packet is routed independently, getting passed on from one computing device to another until it reaches its destination. The computing devices that do that packet forwarding are called routers. Each router keeps an address table that says, when it gets a packet for some destination address, which of its neighbors should it pass the packet on to. The routers are constantly talking to each other passing information about how they should update their routing tables. The system was designed to be resistant to any local damage. If some of the routers stop working, the rest of the routers talk to each other and start routing packets around in a different way so that packets still reach their intended destination if there is some path to get there. It is this technical capability that has spawned metaphoric quotes like this one from John Gilmore: “The Net interprets censorship as damage and routes around it.”

At the destination, the packets are reassembled into the original data message.

![image](https://user-images.githubusercontent.com/103328611/206882250-50fb95fc-7df7-47fd-8aa2-f299cbf7e10e.png)
