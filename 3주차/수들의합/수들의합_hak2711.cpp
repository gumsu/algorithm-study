#include <iostream>

using namespace std;

int main(void){
  unsigned int s;
  cin >> s;

  int n = 0;
  int x = 1;

  while(true){
    n++;
    if((s-x)>x){
      s-=x;
      x++;
    }
    else{
      break;
    }
  }

  cout <<n;
}
