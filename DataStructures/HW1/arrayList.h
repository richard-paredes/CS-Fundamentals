#include <iostream>
#include <cassert>

using namespace std;

#ifndef ARRAYLIST_H
#define ARRAYLIST_H

template <typename T>
class arrayList
{
public:
	//Constructor with default parameter.
	//Sets maxSize = 100 and length = 0 if no parameter is provided
	//Sets maxSize = <n> and length = 0 if <n> is provided and it is larger than 0 (otherwise use default value)
	arrayList(int size = 100);

	//Copy constructor.
	//Must achieve deep copy of original arrayList
	arrayList(const arrayList<T> &other);

	//Overloaded assignment operator =.
	//Must achieve deep copy of original arrayList
	arrayList<T> &operator=(const arrayList<T> &other);

	//isEmpty returns true if list is empty, false otherwise
	bool isEmpty() const;

	//isEmpty returns true if list is full, false otherwise
	bool isFull() const;

	//Return length
	int listSize() const;

	//Return maxSize
	int maxListSize() const;

	//Print all elements in the list separated by a single space
	void print() const;

	//Empty list
	void clearList();

	//Remove from list item at a given position.
	//If position is out of bounds, print an error message.
	void removeAt(int pos);

	//Remove from list an item.
	//If the item is not found, or if list is empty, print an error message.
	void remove(const T &data);

	//Add item to list preserving ascending order.
	//If list is full, print an error message.
	void insert(const T &data);

	//Access an item in the list at a given position.
	//If position is out of bounds, print an error message.
	//Otherwise, return found item in parameter d.
	void retrieveAt(int pos, T &data) const;

	//Search an item in the list and return its position.
	//If not found, return -1;
	int search(const T &data) const;
	~arrayList();

private:
	T *list;
	int length;
	int maxSize;
};

#endif

//Write your functions below
template <typename T>
arrayList<T>::arrayList(int size)
{
	this->maxSize = (size > 0) ? size : 100;
	this->length = 0;
	this->list = new T[this->maxSize];
}

template <typename T>
arrayList<T>::arrayList(const arrayList<T> &other)
{
	this->maxSize = other.maxSize;
	this->length = other.length;
	this->list = new T[this->maxSize];
	for (int i = 0; i < this->length; i++)
		this->list[i] = other.list[i];
}

template <typename T>
arrayList<T> &arrayList<T>::operator=(const arrayList<T> &other)
{
	delete[] this->list;
	this->maxSize = other.maxSize;
	this->length = other.length;
	this->list = new T[this->maxSize];
	for (int i = 0; i < this->length; i++)
		this->list[i] = other.list[i];

	return *this;
}

template <typename T>
bool arrayList<T>::isEmpty() const
{
	return this->length == 0;
}

template <typename T>
bool arrayList<T>::isFull() const
{
	return this->length == this->maxSize;
}

template <typename T>
int arrayList<T>::listSize() const
{
	return this->length;
}

template <typename T>
int arrayList<T>::maxListSize() const
{
	return this->maxSize;
}

template <typename T>
void arrayList<T>::print() const
{
	if (!isEmpty())
	{
		for (int i = 0; i < this->length - 1; i++)
			cout << this->list[i] << " ";
		cout << this->list[this->length - 1] << endl;
	}
}

template <typename T>
void arrayList<T>::clearList()
{
	this->length = 0;
}

template <typename T>
void arrayList<T>::removeAt(int pos)
{
	if (pos > -1 && pos < this->length)
	{
		for (int i = pos; i < this->length - 1; i++)
			this->list[i] = this->list[i + 1];
		this->length--;
	}
	else
		cout << "Error. Index out of bounds." << endl;
}

template <typename T>
void arrayList<T>::remove(const T &data)
{
	int pos = search(data);
	if (pos != -1)
		removeAt(pos);
	else
		cout << "Error. Item is not in the list." << endl;
}

template <typename T>
void arrayList<T>::insert(const T &data)
{
	if (!isFull())
	{
		int pos = 0;
		while (pos < this->length && this->list[pos] < data)
			pos++;
		for (int i = ++this->length; i > pos; i--)
			this->list[i] = this->list[i - 1];
		this->list[pos] = data;
	}
	else
		cout << "Error. List is full." << endl;
}

template <typename T>
void arrayList<T>::retrieveAt(int pos, T &data) const
{
	if (pos > -1 && pos < this->length)
		data = this->list[pos];
	else
		cout << "Error. Index out of bounds." << endl;
}

template <typename T>
int arrayList<T>::search(const T &data) const
{
	for (int i = 0; i < this->length; i++)
		if (this->list[i] == data)
			return i;

	return -1;
}

template <typename T>
arrayList<T>::~arrayList()
{
	delete[] this->list;
}