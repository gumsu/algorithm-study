#include <iostream>
#include <deque>

using namespace std;

int main(void){
  int t;
  cin >> t;

  for(int i = 0; i<t; i++){
    int n;
    cin >> n;

    deque<char> answer;

    for(int j = 0; j<n; j++){
      char c;
      cin >> c;

      if(answer.empty() || (c > answer.front())){
        answer.push_back(c);
      }
      else{
        answer.push_front(c);
      }
    }

    for(char c : answer){
      cout << c;
    }
    cout << "\n";
  }
}
