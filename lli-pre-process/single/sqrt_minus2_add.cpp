#include "cmath"
#include "iostream"
using namespace std;
int main() {
   double x = 0;
   double a = x + 10000;
   double b = x + 9999;
   double result = sqrt(a) - sqrt(b);
   cout << result << endl;
   return 0;
}