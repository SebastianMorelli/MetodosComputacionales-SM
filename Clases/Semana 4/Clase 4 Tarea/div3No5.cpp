//Este código halla los números de 0 a 100 divisibles entre 3 pero no entre 5

#include <iostream>
using namespace std;

int main()
{
  for (int i=0; i <= 100; i++)
  {
    if(i%3 == 0 && i%5 != 0)
    {
      cout<<i<<endl;
    }
  }
  return 0;
}
