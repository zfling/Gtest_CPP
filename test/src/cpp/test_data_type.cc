#include <iostream>
#include "gtest/gtest.h"

#include "test_data_types.h"

using namespace std;

class DataTypeTest : public testing::Test {
public:
    static void SetUpTestCase() {
        cout << "SetUpTestCase" << endl;
        CppDataType();
    }

    static void TearDownTestCase() {
        cout << "TearDownTestCase" << endl;
    }
    
protected:
    void SetUp() override {
        cout << "SetUp" << endl;
    }
    
    void TearDown() override {
        cout << "TearDown" << endl;	
    }
};

TEST_F(DataTypeTest, IntegerTypes) {
    EXPECT_EQ(1, (int)sizeof(char));
    EXPECT_EQ(2, (int)sizeof(short int));
    EXPECT_EQ(4, (int)sizeof(int));
    EXPECT_EQ(8, (int)sizeof(long int));
    EXPECT_EQ(8, (int)sizeof(long long int));
}

TEST_F(DataTypeTest, FloatingPointTypes) {
    EXPECT_EQ(4, (int)sizeof(float));
    EXPECT_EQ(8, (int)sizeof(double));
    EXPECT_EQ(16, (int)sizeof(long double));
}


