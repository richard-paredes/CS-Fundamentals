#include "TicketQueue.h"

TicketQueue::TicketQueue(int cap)
{
   //complete
   this->capacity = (cap < 0) ? 1 : cap;
   this->heap_size = 0;
   this->harr = new Ticket[this->capacity];
}

Ticket TicketQueue::getTicketWithHighestPriority()
{
   //complete
   if (this->heap_size > 0)
   {
      return this->harr[0];
   }
   else
   {
      std::cout << "There are no tickets in the ticket queue." << std::endl;
   }
}

void TicketQueue::insertTicket(Ticket k)
{
   //complete
   if (this->heap_size < this->capacity)
   {
      this->harr[this->heap_size++] = k;
      this->trickleUp(this->heap_size - 1);
   }
   else
   {
      std::cout << "The ticket queue is already full." << std::endl;
   }
}

void TicketQueue::changeTicketPriority(Ticket tkt, int new_priority)
{
   //complete
   bool found = false;
   int found_index = 0;
   while (!found && found_index < this->heap_size)
   {
      if (tkt.getPriority() == this->harr[found_index].getPriority())
         found = true;
      else
         found_index++;
   }

   if (found)
   {

      this->harr[found_index].setPriority(new_priority);
      int parentIndex = this->parent(found_index);
      bool shouldTrickleUp = (parentIndex > 0 && this->harr[parentIndex].getPriority() < this->harr[found_index].getPriority());

      if (shouldTrickleUp)
         this->trickleUp(found_index);
      else
         this->trickleDown(found_index);
   }
   else
   {
      // std::cout << "The ticket is not in the ticket queue." << std::endl;
   }
}

void TicketQueue::trickleUp(int i)
{
   //complete
   // std::cout << "Tricklng index " << i << " upwards." << std::endl;
   if (this->heap_size > 0)
   {
      while (i > 0)
      {
         int parentIndex = this->parent(i);
         int parentPriority = this->harr[parentIndex].getPriority();
         int currentPriority = this->harr[i].getPriority();
         if (currentPriority < parentPriority)
         {
            swap(this->harr[parentIndex], this->harr[i]);
            i = parentIndex;
         }
         else
         {
            break;
         }
      }
   }
}

Ticket TicketQueue::ticketProcessed()
{
   //complete
   if (this->heap_size > 0)
   {
      Ticket processedTicket = this->harr[0];
      swap(this->harr[0], this->harr[heap_size - 1]);
      this->heap_size--;
      this->trickleDown(0);
      return processedTicket;
   }
   else
   {
      std::cout << "The ticket queue is already empty." << std::endl;
   }
}

void TicketQueue::deleteTicket(Ticket i)
{
   //complete
   this->changeTicketPriority(i, INT_MIN); // move to root
   this->ticketProcessed();                // finally, delete the root
}

void TicketQueue::trickleDown(int i)
{
   //complete
   if (this->heap_size > 0)
   {
      int currentPriority = this->harr[i].getPriority();
      while (i < this->heap_size)
      {
         int highestPriority = currentPriority;
         int highestPriorityIndex = -1;
         int leftChildIndex = this->leftChild(i);
         int rightChildIndex = this->rightChild(i);

         if (leftChildIndex < this->heap_size)
         {
            int leftChildPriority = this->harr[leftChildIndex].getPriority();
            if (leftChildPriority < highestPriority)
            {
               highestPriority = leftChildPriority;
               highestPriorityIndex = leftChildIndex;
            }
         }
         if (rightChildIndex < this->heap_size)
         {
            int rightChildPriority = this->harr[rightChildIndex].getPriority();
            if (rightChildPriority < highestPriority)
            {
               highestPriority = rightChildPriority;
               highestPriorityIndex = rightChildIndex;
            }
         }

         if (highestPriority != currentPriority)
         {
            swap(this->harr[i], this->harr[highestPriorityIndex]);
            i = highestPriorityIndex;
            currentPriority = highestPriority;
         }
         else
         {
            break;
         }
      }
   }
}

void TicketQueue::destroyList()
{
   //complete
   delete[] this->harr;
   this->harr = NULL;
}

TicketQueue::~TicketQueue()
{
   //complete
   this->destroyList();
}

// Used for debugging.
// void TicketQueue::print()
// {
//    for (int i = 0; i < this->heap_size; i++)
//    {
//       cout << "[" << i << "] - " << this->harr[i].getClientType() << ": " << this->harr[i].getPriority() << "." << endl;
//    }
// }

void swap(Ticket *x, Ticket *y)
{
   //complete
   Ticket *temp = x;
   x = y;
   y = temp;
}
