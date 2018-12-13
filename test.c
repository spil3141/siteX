#include <stdio.h>

#define N 5

int Q[N];
int front = 0, rear =0;

int isFull(){
  if((rear == N-1 && front ==0) || (front == rear+1))
    return 1;
  else
    return 0;
}

int enqueue(int data){
  if(isFull())
    printf("Full!!\n");
  else {
    Q[rear++] = data;
    printf("삽입했다\n");
  }
  return 1;
}

int main()
{
  enqueue(22);
  enqueue(31);
  enqueue(43);
  enqueue(4);
  enqueue(5);
  enqueue(6);
  int i;
  for (i=0;i<N;i++)
    printf("%d\n",Q[i]);
  printf("\n");

    // // Fails because front = -1
    // deQueue();
    //
    // enQueue(1);
    // enQueue(2);
    // enQueue(3);
    // enQueue(4);
    // enQueue(5);
    //
    // // Fails to enqueue because front == 0 && rear == N - 1
    // enQueue(6);
    //
    // display();
    // deQueue();
    //
    // display();
    //
    // enQueue(7);
    // display();
    //
    // // Fails to enqueue because front == rear + 1
    // enQueue(8);
    //
    return 0;
}
