#include "cmath"
#include "iostream"
using namespace std;

//double global = 15.0;


int main() {
   double x = 3.33;
   double a = x + 10000;
   unsigned int i = 16;
   //double b = global + x + 9999;
   double b = x + 9999;
   i++;
   double result = sqrt(a) - sqrt(b);
   int xx = i + result;


   if(i < 10)
      i++;
   else
      i--;

   while(i < 10) {
      i++;
   }

   int j = 0;
   for(;j < 10;j++) {
      i++;
   }
   
   cout << result << endl;
   return 0;
}