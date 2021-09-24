#include <iostream>
#include <string>

using namespace std;

int numCnt[10];

int main(void)
{
  int A, B, C;

  cin >> A >> B >> C;

  string s = to_string(A * B * C);

  for (auto c : s)
  {
    numCnt[c - '0']++;
  }

  for (auto c : numCnt)
  {
    cout << c << "\n";
  }
}
