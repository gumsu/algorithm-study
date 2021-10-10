#include <iostream>
#define N 5

using namespace std;

int arr[N];

int main(void)
{
  for (int i = 0; i < N; i++)
  {
    cin >> arr[i];
  }

  for (int i = N; i > 1; i--)
  {
    for (int j = 0; j < (i - 1); j++)
    {
      if (arr[j] > arr[j + 1])
      {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;

        for (int k = 0; k < N; k++)
        {
          cout << arr[k] << " ";
        }
        cout << "\n";
      }
    }
  }
}
