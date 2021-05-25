template <typename T>
struct Node
{
    T data;
    Node<T> *next;
};

template <typename T>
class LinkedList
{
private:
    int count;
    Node<T> *head;
    Node<T> *tail;

public:
    LinkedList();
    void clear();
    void append(const T &data);
    void print() const;
    void prepend(const T &data);
    void remove(const T &data);
};