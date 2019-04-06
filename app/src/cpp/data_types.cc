#include <iostream>
#include "data_types.h"

using namespace std;

void CppDataType(void)
{
	cout << "Bytes of (char)         : " << sizeof(char) << endl;
	cout << "Bytes of (short int)    : " << sizeof(short int) << endl;
	cout << "Bytes of (int)          : " << sizeof(int) << endl;
	cout << "Bytes of (long int)     : " << sizeof(long int) << endl;
	cout << "Bytes of (long long int): " << sizeof(long long int) << endl;
	cout << "Bytes of (float)        : " << sizeof(float) << endl;
	cout << "Bytes of (double)       : " << sizeof(double) << endl;
	cout << "Bytes of (long double)  : " << sizeof(long double) << endl;
	return;
}

