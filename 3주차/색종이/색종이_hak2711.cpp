#include <iostream>
#define MAX 100

using namespace std;

int board[MAX][MAX];

int main(void)
{
  int n;
  cin >> n;

  for (int i = 0; i < n; i++)
  {
    int x, y;
    cin >> x >> y;
    for (int j = 0; j < 10; j++)
    {
      for (int k = 0; k < 10; k++)
      {
        board[x + j][y + k] += 1;
      }
    }
  }

  int answer = 0;

  for (int i = 0; i < MAX; i++)
  {
    for (int j = 0; j < MAX; j++)
    {
      if (board[i][j] >= 1)
      {
        answer++;
      }
    }
  }

  cout << answer;
}
