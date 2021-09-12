import program

failed_tests = []
pass_tests = []

def test_max1_handles_same_number_ok():
    a = 2
    result = program.max1(a, a)
    if result == a:
        pass_tests.append('test_max1_handles_same_number_ok PASSED')
    else:
        failed_tests.append(f'test_max1_handles_same_number_ok FAILED: the returned value was not as expected, test expected: {a} but instead got {result}')

def test_max1_handles_different_number_ok():
    a = 2
    b = 3
    result = program.max1(a, b)
    if result == b:
        pass_tests.append('test_max1_handles_different_number_ok PASSED')
    else:
        failed_tests.append(f'test_max1_handles_different_number_ok FAILED: the returned value was not as expected, test expected: {b} but instead got {result}')

def test_max1_handles_different_number_first_arg_ok():
    a = 0
    b = 3
    expected = -1
    result = program.max1(a, b)
    if result == expected:
        pass_tests.append('test_max1_handles_different_number_first_arg_ok PASSED')
    else:
        failed_tests.append(f'test_max1_handles_different_number_first_arg_ok FAILED: the returned value was not as expected, test expected: {expected} but instead got {result}')

def test_max1_handles_different_number_second_arg_ok():
    a = 3
    b = 0
    expected = -1
    result = program.max1(a, b)
    if result == expected:
        pass_tests.append('test_max1_handles_different_number_second_arg_ok PASSED')
    else:
        failed_tests.append(f'test_max1_handles_different_number_second_arg_ok FAILED: the returned value was not as expected, test expected: {expected} but instead got {result}')


test_max1_handles_same_number_ok()
test_max1_handles_different_number_ok()
test_max1_handles_different_number_first_arg_ok()
test_max1_handles_different_number_second_arg_ok()
# for each 

# int i = 0; i < pass_tests.length; i++
#  passed_test = pass_tests[i]
#
#
for passed_test in pass_tests:
    print(passed_test)

for failed_test in failed_tests:
    print(failed_test)