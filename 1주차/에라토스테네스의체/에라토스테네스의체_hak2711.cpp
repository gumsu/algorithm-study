#include <iostream>
#define MAX 1001

using namespace std;

int arr[MAX];
int n, k, cnt;

int main(void)
{
  cin >> n >> k;

  for (int i = 2; i <= n; i++)
  {
    arr[i] = i;
  }

  for (int i = 2; i <= n; i++)
  {
    if (arr[i])
    {
      for (int j = 1; j <= (n / i); j++)
      {
        if (arr[i * j])
        {
          arr[i * j] = 0;
          cnt++;
          if (cnt == k)
          {
            cout << i * j;
            break;
          }
        }
      }
    }
    if (cnt == k)
      break;
  }
}
