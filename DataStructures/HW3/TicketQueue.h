#pragma once

#include <iostream>
#include <climits>

#include "Ticket.h"

using namespace std;

void swap(Ticket *x, Ticket *y);

class TicketQueue
{
private:
    Ticket *harr;  // ADT for min heap
    int capacity;  // total size of heap
    int heap_size; // number of items in heap

public:
    TicketQueue(int cap);
    void trickleDown(int);
    int returnTicketQueueSize() { return capacity; }
    int parent(int i) { return (i - 1) / 2; }
    int leftChild(int i) { return (2 * i + 1); }
    int rightChild(int i) { return (2 * i + 2); }
    int getNumberOfTicketsInTicketQueue() { return heap_size; }
    Ticket ticketProcessed();
    void changeTicketPriority(Ticket i, int new_priority);
    Ticket getTicketWithHighestPriority();
    void deleteTicket(Ticket i);
    void insertTicket(Ticket k);
    void trickleUp(int i);
    void destroyList();
    // void print();
    ~TicketQueue();
};
