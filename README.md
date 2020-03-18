# README Project 3

Lucas Calero Forero, William Cooper, Riddhi Adhiya

## High level Approach

- For this project, our first task was to actually understand what the given starter code meant.
  While we understood both the Transport Layer concepts and what the final product should do, we
  were challenged by the format of the assignment, where we had to work with two separate files
  that were technically “not used” by each other, except when run from a third file.
- Once we were able to speak with the course instructor about the project and what it meant, we
  quickly got to work with modifying the code to be more understandable to us, and more readable
  for future reviewers. This meant encapsulating the sender and receivers in classes, as well as
  developing a number of simple helper functions.
- Despite a sliding window being a concept with a specific implementation in the slides, we thought
  it best to make it our own, and therefore used a “leftmost edge” technique for sending acks.
  This allowed us to send a large number of messages and wait for just one correct ack, which
  saved us considerable time as an efficiency algorithm.

- We implemented an RTT and RTO in order to resend packages from the sender to the receiver so that
  we could continue receiving acks.
- We also implemented two lists in the receiver ordered_list and packet_buffer, which held packets
  that arrived in order and packets that arrived out of order respectively
- This ordered_list was used to calculate the “left edge” that was sent in the ack
- Our ACK was implemented with this left edge, and a list of all the other out-of-order packets received.

## Challenges

- Our most time consuming challenge was a very silly bug where we were writing to stdout the wrong data,
  and logging the correct order.
- Another challenge was having EOF and and ack back to the sender so that both systems close correctly
  when high drop rates were present.
- We struggled to implement RTT and have the sender resend packages if the receiver did not ack them
  in time. We used the slides heavily for our equation

## Overview of Testing

- We tested this by logging as much as we could. We used two lists in the receiver to represent
  packages that arrived in order and packages that arrived out of order, we printed out those lists
  in order to understand how the receiver was handling the packages.
