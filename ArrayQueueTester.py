import ArrayQueue
print("Now Testing ArrayQueue")



print("----------------------------Initial Creation----------------------------\n")
queue = ArrayQueue.ArrayQueue()
for i in range(97, 105):
    queue.add(chr(i))

print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']")
print("Backing Array Contents: ", queue.a, "\n\n")

print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayQueue: ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']\tExpected Size: 8")
print("ArrayQueue Contents: ", queue, "\tActual Size:", len(queue))

print("\n\n----------------------------Removing All Elements----------------------------\n")
j = 97
while(queue.size() > 0):
    print("Expected Removed Element:", chr(j), "\tActual Removed Element:", queue.remove())
    j += 1

print("\n\n----------------------------Re-Creation----------------------------\n")
for i in range(105, 111):
    queue.add(chr(i))

print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['i' 'j' 'k' 'l' 'm' 'n' 0 0] ")
print("Backing Array Contents: ", queue.a, "\n\n")

print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayQueue: ['i' 'j' 'k' 'l' 'm' 'n' ]\tExpected Size: 6")
print("ArrayQueue Contents: ", queue, "\tActual Size:", len(queue))


print("\n\n----------------------------Removing 2 Elements----------------------------\n")
for j in range(105, 107):
    print("Expected Removed Element:", chr(j), "\tActual Removed Element:", queue.remove())
print("\nExpected ArrayQueue: ['k','l','m','n']\tExpected Size: 4")
print("ArrayQueue Contents: ", queue, "\tActual Size:", len(queue))

print("\n\n----------------------------Adding 3 Elements----------------------------\n")
for j in range(111, 114):
    queue.add(chr(j))

print("Expected ArrayQueue: ['k','l','m','n','o','p','q'] \tExpected Size: 7")
print("ArrayQueue Contents: ", queue, "\tActual Size:", len(queue))

print("\n\n----------------------------Removing All Elements----------------------------\n")
j = 107
while(queue.size() > 0):
    print("Expected Removed Element:", chr(j), "\tActual Removed Element:", queue.remove())
    j += 1