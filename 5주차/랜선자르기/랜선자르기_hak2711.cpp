#include <iostream>
#include <climits>
#include <algorithm>
#define MAX 1000001

using namespace std;

int arr[MAX];

int main(void)
{
  int k, n;
  cin >> k >> n;

  for (int i = 0; i < k; i++)
  {
    cin >> arr[i];
  }

  long long low = 1;
  long long high = *max_element(arr, arr + k);
  long long answer = 0;

  while (low <= high)
  {
    long long mid = (low + high) / 2;

    long long cnt = 0;
    for (int i = 0; i < k; i++)
    {
      cnt += (arr[i] / mid);
    }

    if (cnt >= n)
    {
      low = mid + 1;
      answer = mid;
    }
    else
    {
      high = mid - 1;
    }
  }

  cout << answer;
}
