#include <iostream>
#include "gtest/gtest.h"

#include "test_container_lib.h"

using namespace std;

class ContainerLibTest : public testing::Test {
public:
    static void SetUpTestCase() {

    }

    static void TearDownTestCase() {

    }
    
protected:
    void SetUp() override {
    }
    
    void TearDown() override {
    }
};

TEST_F(ContainerLibTest, vector_test_1) {
    std::vector<int> v = GetVectorFun();
    int expects[] = {7, 5, 16, 8, 25, 13};
    for (unsigned int loop = 0; loop < v.size(); ++loop) {
        EXPECT_EQ(expects[loop], v[loop]);
    }
}

