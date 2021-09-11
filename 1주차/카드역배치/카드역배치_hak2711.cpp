#include <iostream>
#define MAX 21

using namespace std;

int arr[MAX];

void flip(int x, int y)
{
  int temp;
  for (int i = 0; i < (y - x + 1) / 2; i++)
  {
    temp = arr[x + i];
    arr[x + i] = arr[y - i];
    arr[y - i] = temp;
  }
}

int main(void)
{
  int n = 10;

  for (int i = 1; i < MAX; i++)
  {
    arr[i] = i;
  }

  for (int i = 0; i < n; i++)
  {
    int x, y;
    cin >> x >> y;
    flip(x, y);
  }

  for (int i = 1; i < MAX; i++)
  {
    cout << arr[i] << " ";
  }
}
