#include <iostream>

using namespace std;

int main(void)
{
  int t;
  cin >> t;

  int answer[3] = {
      0,
  };

  while (t >= 10)
  {
    if (t >= 300)
    {
      answer[0] += (t / 300);
      t %= 300;
    }
    else if (t >= 60)
    {
      answer[1] += (t / 60);
      t %= 60;
    }
    else
    {
      answer[2] += (t / 10);
      t %= 10;
    }
  }

  if (t != 0)
  {
    cout << -1;
  }
  else
  {
    cout << answer[0] << " " << answer[1] << " " << answer[2];
  }
}
