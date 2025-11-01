#include <iostream>
using namespace std;

#define SIZE 5  // Maximum size of the queue

class Queue {
private:
    int items[SIZE];
    int front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    // Check if the queue is full
    bool isFull() {
        return (rear == SIZE - 1);
    }

    // Check if the queue is empty
    bool isEmpty() {
        return (front == -1 || front > rear);
    }

    // Enqueue operation
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is full. Cannot enqueue " << value << endl;
        } else {
            if (front == -1)  // first element
                front = 0;
            rear++;
            items[rear] = value;
            cout << value << " enqueued to queue." << endl;
        }
    }

    // Dequeue operation
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue." << endl;
        } else {
            cout << items[front] << " dequeued from queue." << endl;
            front++;
        }
    }

    // Display all elements
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
        } else {
            cout << "Queue elements: ";
            for (int i = front; i <= rear; i++)
                cout << items[i] << " ";
            cout << endl;
        }
    }
};

// Main function to test the queue
int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();

    q.dequeue();
    q.display();

    q.enqueue(40);
    q.enqueue(50);
    q.enqueue(60);  // This will show "Queue is full"
    q.display();

    return 0;
}
