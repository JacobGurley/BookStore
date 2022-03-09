print("Now testing ArrayList: ")
import ArrayList
arraylist = ArrayList.ArrayList()

for i in range(97, 105):
    arraylist.append(chr(i))


print("----------------------------Initial Creation----------------------------")
print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']")
print("Backing Array Contents: ", arraylist.a, "\n\n")

print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayList: ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']\tExpected Size: 8")
print("ArrayList Contents: ", arraylist, "\tActual Size:", len(arraylist), "\n\n")


print("----------------------------Removing Index 2: Shift Right Expected ----------------------------")
r = arraylist.remove(2)
print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['a' 'a' 'b' 'd' 'e' 'f' 'g' 'h']")
print("Backing Array Contents: ", arraylist.a)
print("Expected Removed Element: c")
print("Actual Removed Element:", r, "\n\n")

print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayList: ['a' 'b' 'd' 'e' 'f' 'g' 'h']\tExpected Size: 7")
print("ArrayList Contents: ", arraylist, "\tActual Size:", len(arraylist), "\n\n")

print("----------------------------Adding at Index 4: Shift Right Expected ----------------------------")
arraylist.add(4, "x")
print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['h' 'a' 'b' 'd' 'e' 'x' 'f' 'g']")
print("Backing Array Contents: ", arraylist.a, "\n\n")


print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayList: ['a' 'b' 'd' 'e' 'x' 'f' 'g' 'h']\tExpected Size: 8")
print("ArrayList Contents: ", arraylist, "\tActual Size:", len(arraylist), "\n\n")

print("----------------------------Adding at Index 3: Shift Left Expected ----------------------------")
arraylist.add(3, "y")
print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['b' 'd' 'y' 'e' 'x' 'f' 'g' 'h' 0 0 0 0 0 0 0 'a']  ")
print("Backing Array Contents: ", arraylist.a, "\n\n")


print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayList: ['a' 'b' 'd' 'y' 'e' 'x' 'f' 'g' 'h']\tExpected Size: 9")
print("ArrayList Contents: ", arraylist, "\tActual Size:", len(arraylist), "\n\n")

print("----------------------------Removing Index 6: Shift Left Expected ----------------------------")
r = arraylist.remove(6)
print("INTERNAL OPERATIONS")
print("Expected Backing Array: ['b' 'd' 'y' 'e' 'x' 'g' 'h' 'h' 0 0 0 0 0 0 0 'a']")
print("Backing Array Contents: ", arraylist.a)
print("Expected Removed Element: f")
print("Actual Removed Element:", r, "\n\n")


print("DATA STRUCTURE APPEARANCE")
print("Expected ArrayList: ['a' 'b' 'd' 'y' 'e' 'x' 'g' 'h']\tExpected Size: 8")
print("ArrayList Contents: ", arraylist, "\tActual Size:", len(arraylist), "\n\n")