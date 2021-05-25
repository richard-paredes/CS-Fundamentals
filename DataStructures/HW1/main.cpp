#include <iostream>
#include <string>
#include "arrayList.h"
#include "Circle.h"
using namespace std;

int main()
{
	arrayList<int> list(10);

	list.insert(30); // 30
	list.insert(10); // 10, 30
	list.insert(30); // 10, 30, 30
	list.insert(40); // 10, 30, 30, 40
	list.insert(20); // 10, 20, 30, 30, 40
	list.print();

	list.remove(40); // 10, 20, 30, 30
	list.print();

	list.removeAt(0);  // 20, 30, 30
	list.removeAt(-1); // error
	list.removeAt(51); // error
	list.print();

	cout << "The size of my list is: " << list.listSize() << endl;
	cout << "The max size of my list is: " << list.maxListSize() << endl;

	int temp;
	list.retrieveAt(5, temp); // error
	list.retrieveAt(0, temp); // 20
	cout << "The value at 0 is: " << temp << endl;

	int pos;
	pos = list.search(50); // error
	pos = list.search(30); // 1
	cout << "The position of 30 is " << pos << endl;

	list.clearList();
	if (!list.isEmpty())
		list.print();
	else
		cout << "The list is empty." << endl;

	list.insert(55); // 55
	list.insert(33); // 33, 55
	list.insert(22); // 22, 33, 55
	list.insert(66); // 22, 33, 55, 66
	list.insert(77); // 22, 33, 55, 66, 77
	list.insert(88); // 22, 33, 55, 66, 77, 88
	list.insert(99); // 22, 33, 55, 66, 77, 88, 99
	list.insert(0);	 // 0, 22, 33, 55, 66, 77, 88, 99
	list.insert(11); // 0, 11, 22, 33, 55, 66, 77, 88, 99
	list.insert(44); // 0, 11, 22, 33, 44, 55, 66, 77, 88, 99
	list.insert(45); // error

	list.print();
	cout << "The size of my list is: " << list.listSize() << endl;
	cout << "The max size of my list is: " << list.maxListSize() << endl;

	arrayList<Circle> circles(5);
	circles.insert(Circle(3.0));
	circles.insert(Circle(1.0));
	circles.insert(Circle(4.0));
	circles.insert(Circle(2.0));
	circles.insert(Circle(5.0));
	circles.insert(Circle(0)); // error

	circles.print();

	circles.remove(Circle(5.0));
	circles.remove(Circle(6.0));
	circles.print();
	return 0;
}

//You may modify main for testing purposes
ostream &operator<<(ostream &os, const Circle &circle)
{
	os << "Circle radius: " << to_string(circle.getRadius());
	return os;
}