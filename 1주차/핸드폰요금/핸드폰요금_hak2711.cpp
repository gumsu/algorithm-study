#include <iostream>
#define MAX 21

using namespace std;

int arr[MAX];
int n;

int Ypay()
{
  int p = 0;
  for (int i = 0; i < n; i++)
  {
    p += (arr[i] / 30 + 1) * 10;
  }
  return p;
}

int Mpay()
{
  int p = 0;
  for (int i = 0; i < n; i++)
  {
    p += (arr[i] / 60 + 1) * 15;
  }
  return p;
}

int main(void)
{
  cin >> n;

  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }

  int y = Ypay();
  int m = Mpay();

  if (y < m)
  {
    cout << "Y " << y;
  }
  else if (m < y)
  {
    cout << "M " << m;
  }
  else
  {
    cout << "Y M " << y;
  }
}
