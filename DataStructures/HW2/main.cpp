#include <iostream>

#include "LinkedList.h"

int main()
{
    LinkedList<int> list;
    list.append(1);  // 1
    list.prepend(2); // 2, 1
    list.append(3);  // 2, 1, 3
    list.prepend(4); // 4, 2, 1, 3
    list.print();
    return 0;
}