# notes

stop and wait protocol - current

Simulator:
 

 Send
 


## netsim

- has a bunch of queues inside (not how it works but helpful to understand)
- the length of those q means the delay
- they are udp sockets so it should be instantanteous
- latency = length of queue
- How do we move from stop and wait to something else
- The solution is some sliding window
  - Have receiver say here is how much I can receive
  - Window 
  - Est rtt
  - 
- Send a fin!!!

- In addition to RTT also have a Try N times or Try Delta time - after some delay decide that the ack is not going to come then retransmit. 

RTT is for send 

TCP Closes:
Sender: sends a fin - 
Rec: When gets that, knows that no more data
Sender: needs to send an ack of the fin


Under really bad package drop:

Then fin doesn't get there. Send another fin. Send another fin, then receiver sends another ack. 

TCP uses 2* rtt 




Recv