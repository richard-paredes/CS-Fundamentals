#ifndef B_TREE_H
#define B_TREE_H

#include <utility>
#include <stdlib.h>
#include <utility>
#include <stdio.h>

using namespace std;

enum RootType
{
    NOT_MODIFIED,
    MODIFIED_NOT_ROOT,
    NEW_ROOT
};

template <typename T>
struct BNode
{
    BNode<T> **child;
    T *keys;
    unsigned size;
    bool leaf;
};

template <typename T>
class BTree
{
public:
    BTree(unsigned int minNumOfDegree);
    ~BTree<T>();

    void insert(T key); //Complete
    bool remove(T key); //Complete
    bool searchKey(T key);
    void preorderTraverse(); //Complete
    void inorderTraverse();

private:
    void initializeNode(BNode<T> *node);
    void freeNode(BNode<T> *node);

    unsigned findIndex(BNode<T> *node, T key);
    std::pair<BNode<T> *, unsigned> search(T key);

    unsigned nodeInsert(BNode<T> *node, T key);
    T nodeDelete(BNode<T> *node, unsigned index);

    void splitChild(BNode<T> *node, int split_index);
    char mergeChildren(BNode<T> *parent, unsigned index);
    char fixChildSize(BNode<T> *parent, unsigned index);

    bool lessThan(T a, T b);
    void preRec(BNode<T> *node); //Complete
    void inRec(BNode<T> *node);

    BNode<T> *root;
    unsigned minDegree;
};

#endif // B_TREE_H

template <typename T>
BTree<T>::BTree(unsigned int minNumOfDegree)
{
    if (minNumOfDegree < 2)
    {
        cout << "Minimum number of degree cannot be less than 2" << endl;
    }

    minDegree = minNumOfDegree;
    root = new BNode<T>();
    initializeNode(root);
    root->leaf = true;
}

template <typename T>
BTree<T>::~BTree<T>()
{
    freeNode(root);
}

template <typename T>
void BTree<T>::insert(T key)
{
    //Complete insert
}

template <typename T>
bool BTree<T>::remove(T key)
{
    //Complete remove so that it removes an item from the tree and returns true if successfull.
    //Return false if item is not in the tree.
}

template <typename T>
pair<BNode<T> *, unsigned> BTree<T>::search(T key)
{
    BNode<T> *node = root;

    while (true)
    {
        unsigned index = findIndex(node, key);

        if (index < node->size && !(lessThan(key, node->keys[index]) || lessThan(node->keys[index], key)))
        {
            return pair<BNode<T> *, unsigned>(node, index);
        }
        else if (node->leaf)
        {
            return pair<BNode<T> *, unsigned>(NULL, 0);
        }
        else
        {
            node = node->child[index];
        }
    }
}

template <typename T>
bool BTree<T>::searchKey(T key)
{
    pair<BNode<T> *, unsigned> info_pair = search(key);

    if (info_pair.first == NULL)
        return false;
    else
    {
        //		cout << "Index: " << info_pair.second << endl;
        return true;
    }
}

template <typename T>
void BTree<T>::preorderTraverse()
{
    //Complete preorderTraverse (it should call preRec on root)
}

template <typename T>
void BTree<T>::preRec(BNode<T> *node)
{
    //Complete recursive preorder traversal
}

template <typename T>
void BTree<T>::inorderTraverse()
{
    inRec(root);
}

template <typename T>
void BTree<T>::inRec(BNode<T> *node)
{
    if (node != NULL)
    {
        inRec(node->child[0]);

        for (unsigned i = 0; i < node->size; i++)
        {
            cout << node->keys[i] << " ";
            inRec(node->child[i + 1]);
        }
    }
}

template <typename T>
void BTree<T>::initializeNode(BNode<T> *node)
{
    node->size = 0;
    node->keys = new T[2 * minDegree - 1];
    node->child = new BNode<T> *[2 * minDegree];
}

template <typename T>
void BTree<T>::freeNode(BNode<T> *node)
{
    if (!node->leaf)
    {
        for (unsigned i = 0; i <= node->size; i++)
        {
            freeNode(node->child[i]);
        }
    }

    delete[] node->child;
    delete[] node->keys;
    delete node;
}

template <typename T>
unsigned BTree<T>::findIndex(BNode<T> *node, T key)
{
    unsigned i = 0;

    while (i < node->size && lessThan(node->keys[i], key))
    {
        i++;
    }

    return i;
}

template <typename T>
unsigned BTree<T>::nodeInsert(BNode<T> *node, T key)
{
    int index;

    for (index = node->size; index > 0 && lessThan(key, node->keys[index - 1]); index--)
    {
        node->keys[index] = node->keys[index - 1];
        node->child[index + 1] = node->child[index];
    }

    node->child[index + 1] = node->child[index];
    node->keys[index] = key;
    node->size++;

    return index;
}

template <typename T>
T BTree<T>::nodeDelete(BNode<T> *node, unsigned index)
{
    T toReturn = node->keys[index];

    node->size--;
    while (index < node->size)
    {
        node->keys[index] = node->keys[index + 1];
        node->child[index + 1] = node->child[index + 2];
        index++;
    }

    return toReturn;
}

template <typename T>
void BTree<T>::splitChild(BNode<T> *node, int split_index)
{
    BNode<T> *toSplit = node->child[split_index];
    BNode<T> *newNode = new BNode<T>;

    initializeNode(newNode);
    newNode->leaf = toSplit->leaf;
    newNode->size = minDegree - 1;

    for (unsigned j = 0; j < minDegree - 1; j++)
    {
        newNode->keys[j] = toSplit->keys[j + minDegree];
    }

    if (!toSplit->leaf)
    {
        for (unsigned j = 0; j < minDegree; j++)
        {
            newNode->child[j] = toSplit->child[j + minDegree];
        }
    }

    toSplit->size = minDegree - 1;
    nodeInsert(node, toSplit->keys[minDegree - 1]);
    node->child[split_index + 1] = newNode;
}

template <typename T>
char BTree<T>::mergeChildren(BNode<T> *parent, unsigned index)
{
    BNode<T> *leftKid = parent->child[index];
    BNode<T> *rightKid = parent->child[index + 1];

    leftKid->keys[leftKid->size] = nodeDelete(parent, index);
    unsigned j = ++(leftKid->size);

    for (unsigned k = 0; k < rightKid->size; k++)
    {
        leftKid->keys[j + k] = rightKid->keys[k];
        leftKid->child[j + k] = rightKid->child[k];
    }

    leftKid->size += rightKid->size;
    leftKid->child[leftKid->size] = rightKid->child[rightKid->size];

    delete[] rightKid->child;
    delete[] rightKid->keys;
    delete rightKid;

    if (parent->size == 0)
    {
        root = leftKid;
        free(parent->child);
        free(parent->keys);
        free(parent);
        return NEW_ROOT;
    }

    return MODIFIED_NOT_ROOT;
}

template <typename T>
char BTree<T>::fixChildSize(BNode<T> *parent, unsigned index)
{
    BNode<T> *kid = parent->child[index];

    if (kid->size < minDegree)
    {
        if (index != 0 && parent->child[index - 1]->size >= minDegree)
        {
            BNode<T> *leftKid = parent->child[index - 1];

            for (unsigned i = nodeInsert(kid, parent->keys[index - 1]); i != 0; i--)
            {
                kid->child[i] = kid->child[i - 1];
            }
            kid->child[0] = leftKid->child[leftKid->size];
            parent->keys[index - 1] = nodeDelete(leftKid, leftKid->size - 1);
        }
        else if (index != parent->size && parent->child[index + 1]->size >= minDegree)
        {
            BNode<T> *rightKid = parent->child[index + 1];
            nodeInsert(kid, parent->keys[index]);
            kid->child[kid->size] = rightKid->child[0];
            rightKid->child[0] = rightKid->child[1];
            parent->keys[index] = nodeDelete(rightKid, 0);
        }
        else if (index != 0)
        {
            return mergeChildren(parent, index - 1);
        }
        else
        {
            return mergeChildren(parent, index);
        }
        return MODIFIED_NOT_ROOT;
    }

    return NOT_MODIFIED;
}

template <typename T>
bool BTree<T>::lessThan(T a, T b)
{
    return (a < b) ? true : false;
}