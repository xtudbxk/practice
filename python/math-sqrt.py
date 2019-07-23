
# 牛顿法
def sqrt(x):
    test_x = x/2
    last_test_x = test_x
    test_x = (test_x+x/test_x)/2
    while(abs(last_test_x-test_x)>1e-5):
        last_test_x = test_x
        test_x = (test_x+x/test_x)/2
    return test_x

if __name__ == "__main__":
    print(f"x:5,sqrt of x:{sqrt(5)}")
    print(f"x:9,sqrt of x:{sqrt(9)}")
    print(f"x:10.5,sqrt of x:{sqrt(10.5)}")

