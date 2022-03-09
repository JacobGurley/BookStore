import Calculator
import BookStore
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import algorithms
def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    hash = ChainedHashTable.ChainedHashTable()
    while option != '0':
        print ("""
        1 Assign variable and value to expression 
        2 Introduce expression
        3 Print the expression with variables
        4 Check matched expression
        5 Print evaluated expression 
        0 Return to main menu
        """)
        option=input() 
        if option=="1":
            variable = input("Introduce the variable: ")
            value = float(input("Introduce the value: "))
            calculator.set_variable(variable,value)

        elif option=="2":
            expression = input("Introduce the mathematical expression: ")
            if expression == '':
                print("the expression is empty")
            elif calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option=="3":
            for i in expression:
                if calculator.dict.find(i) == None:
                    print(i,end='')
                else:
                    print(calculator.dict.find(i),end='')
        elif option =="4":
            expression = input("Introduce the mathematical expression: ")
            if expression == '':
                print("the expression is empty")
            elif calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == "5":
                answer = float(calculator.evaluate(expression))
                print("%.2f" % answer)
            #if answer == 0:
                #print("{} = {0.2f}".format(expression,answer))
            #else:
                #print("{} = {0.2f}".format(final,answer))





        ''' 
        Add the menu options when needed
        '''

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()

    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Reverse shopping cart
        7 Get best seller
        8 Find from index title
        9 Search Tree IndexSortedTitle
        10 kBestSeller
        11 mergeSort
        12 quickSort
        13 binarySearchbyTitle
        14 bfs2
        15 dfs2
        0 Return to main menu
        """)
        option=input() 
        if option=="r":
            bookStore.setRandomShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
            #bookStore.pathLength(0, 159811)
        elif option=="2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="4":
            bookStore.removeFromShoppingCart()
        elif option=="5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option=="6":
            bookStore.reverseShoppingCart()
        elif option=="7":
            bookStore.getbestseller()
        elif option=="8":
            indexTitle = input("Enter the Index of the book you would like to find: ")
            bookStore.findFromIndexTitle(indexTitle)
        elif option == "9":
            search = input("Enter the Index of the book you would like to find: ")
            bookStore.indexSortedTitle(search)
        elif option == "10":
            dubs = input ("Introduce the query to search: ")
            bookStore.kbestSeller(dubs)
        elif option == "11":
            bookStore.mergeSort()
        elif option == "12":
            bookStore.quickSort()
        elif option == "13":
            pre = str(input("enter prefix: "))
            bookStore.binarySearchTitle(pre)
        elif option == "14":
            r = int(input("Enter the index: "))
            s = int(input("Enter the distance from index: "))
            answer = bookStore.similarGraph.bfs2(r,s)
            for i in range(1, len(answer)):
                print(bookStore.bookCatalog.get(answer[i]))
        elif option == "15":
            r = int(input("Enter starting index: "))
            s = int(input("Enter destination: "))
            result = bookStore.similarGraph.dfs2(r,s)
            print("The degree of seperation is: ", result)








def menu_reverse_list():
    sllqueue = SLLQueue.SLLQueue()
    option = ""
    while option != '0':
        print("""
        1 Print SLList
        2 Add to SLList
        3 Reverse SLList
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            print(sllqueue)
        elif option == "2":
            lllllllllinput = (input("Enter a value to SLList: "))
            sllqueue.add(lllllllllinput)

        elif option == "3":
            sllqueue.reverse()

def menu_dLList():
    dllist = DLList.DLList()
    option = ""
    while option != '0':
        print("""
            1 Add to DLList
            2 Remove from DLList
            3 Print DLList
            4 Check if Palindrome 
            0 Return to main menu
            """)
        option = input()
        if option == "1":
            i = input("Enter an element to add to DLList: ")
            dllist.append(i)
        elif option == "2":
            i = input("Enter an element to remove from DLList: ")
            print(f"Word {dllist.remove(int(i) - 1)} at index {i} removed from DLList: ")
        elif option == "3":
            print("DLList: ", dllist)
        elif option == "4":
            if dllist.isPalindrome():
                print(f"{dllist} is palindrome")
            else:
                print(f"{dllist} is not a palindrome")


def menu_BinaryTree():
    bst = BinarySearchTree.BinarySearchTree()
    option = ""
    while option != '0':
        print("""
            1 Add Nodes and Values for Traversal
            2 Value of Nodes pre order
            3 Value of Nodes in order
            4 Value of Nodes post order
            5 Display Values of bf_traversal
            6 Print height of the tree
            0 return to main menu
            """)
        option = input()
        l = list()
        if option == '1':
            n = input("Enter the Node you would like to add: ")
            v = input("Enter the Value you would like to add: ")
            bst.add(n,v)
        elif option == '2':
            print(bst.pre_order(bst.r, l))
        elif option == '3':
            print(bst.in_order(bst.r, l))
        elif option == '4':
            print(bst.post_order(bst.r, l))
        elif option == '5':
            print(bst.bf_traverse())
        elif option == '6':
            print(bst.height())




#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        3 DLList
        4 Reverse
        5 BinaryTree
        0 Exit/Quit
        """)
        option=input()

        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()
        elif option =="3":
            menu_dLList()
        elif option == "4":
            menu_reverse_list()
        elif option == "5":
            menu_BinaryTree()

if __name__ == "__main__":
  main()
