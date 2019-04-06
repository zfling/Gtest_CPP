#include "container_lib.h"

std::vector<int> GetVectorFun(void)
{
    std::vector<int> v = {7, 5, 16, 8};
    
    v.push_back(25);
    v.push_back(13);

    return v;
}


