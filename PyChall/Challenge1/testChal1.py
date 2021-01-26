#returns true if passes
def testOne(newString):
    string = 'AABBBDFFFF'
    result = False
    if newString == [['A',2],['B',3],['D',1],['F',4]]:
        result = True
    return result

def testTwo(newString):
    result = False
    return result
# runs all the tests in this file
def main():
    print("test one passed: %r\n" %testOne(newstring))
    print("test two passed: %r\n" %testTwo(newstring))

    # if test fails, break look into exceptions
    return

main()
