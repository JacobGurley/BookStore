import ArrayStack

print("Now Testing ArrayStack")

print("----------------------------Initial Creation----------------------------\n")
stack = ArrayStack.ArrayStack()
for i in range(97, 105):
    stack.push(chr(i))

print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']")
print("Backing Array Contents: ", stack.a, "\n\n")

print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayStack: ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']\tExpected Size: 8")
print("ArrayStack Contents: ", stack, "\tActual Size:", len(stack))

print("\n\n----------------------------Removing All Elements----------------------------\n")
j = 104
while (stack.size() > 0):
    print("Expected Removed Element:", chr(j), "\tActual Removed Element:", stack.pop())
    j -= 1

print("\n\n----------------------------Re-Creation----------------------------\n")
for i in range(105, 111):
    stack.push(chr(i))

print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['i' 'j' 'k' 'l' 'm' 'n' 0 0] ")
print("Backing Array Contents: ", stack.a, "\n\n")

print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayQueue: ['i' 'j' 'k' 'l' 'm' 'n' ]\tExpected Size: 6")
print("ArrayStack Contents: ", stack, "\tActual Size:", len(stack))

print("\n\n----------------------------Removing 2 Elements----------------------------\n")
for j in range(110, 108, -1):
    print("Expected Removed Element:", chr(j), "\tActual Removed Element:", stack.pop())
print("\nExpected ArrayQueue: ['i','j','k','l'] \tExpected Size: 4")
print("ArrayStack Contents: ", stack, "\tActual Size:", len(stack))

print("\n\n----------------------------Adding 3 Elements----------------------------\n")
for j in range(111, 114):
    stack.push(chr(j))

print("Expected ArrayQueue: ['i','j','k','l','o','p','q']  \tExpected Size: 7")
print("ArrayStack Contents: ", stack, "\tActual Size:", len(stack))

print("\n\n----------------------------Removing All Elements----------------------------\n")
expected_contents = ['i', 'j', 'k', 'l', 'o', 'p', 'q']
j = len(expected_contents)-1
while (stack.size() > 0):
    print("Expected Removed Element:", expected_contents[j], "\tActual Removed Element:", stack.pop())
    j -= 1
