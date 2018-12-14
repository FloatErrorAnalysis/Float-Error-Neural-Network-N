#include "cmath" 
using namespace std;
double sqrt_minus_error(double x) {
   return sqrt(25*x+1) - sqrt(25*x);
}