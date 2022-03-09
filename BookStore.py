import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time
import SLLStack
import SLLQueue
import DLList
import MaxQueue
import SortableBook

import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue() #changed from SLLQueue
        self.bookSortedCatalog = None
        #self.indexKeys = ChainedHashTable.ChainedHashTable()
        self.similarGraphs = None
        self.indexKeys = None

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = DLList.DLList() #changed to DLList
        #self.indextitle = ChainedHashTable.ChainedHashTable() #lab3
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.indexKeys = ChainedHashTable.ChainedHashTable()
        self.searchTree = BinarySearchTree.BinarySearchTree()

        with open(fileName, encoding='UTF-8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                #book = SortableBook.SortableBook(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.indexKeys.add(s.key, i)
                #self.bookSortedCatalog.append(book)
                #self.bookSortedCatalog.append(s)
                i = i + 1

        self.similarGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding='UTF-8') as f:
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1,len(l)):
                    j = self.indexKeys.find(l[k])
                    if j is not None:
                        self.similarGraph.add_edge(i,j)
                i = i + 1
                #self.bookSortedCatalog.append(book)
                #self.indextitle.add(title ,s) #lab3
                #self.searchTree.add(title, s)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        
    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue() #changed to SLLQueue
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

   
    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''

        start_time = time.time()
        index = -1
        #if infix == "":
            #print("Exception Error")
        #else:

        for i in self.bookCatalog:
            index +=1
            if infix == "":
                print(f"{i.title}) is at index {index}")

                if index >= 49:
                    break
            elif infix in i.title:
                print(f"{i.title}) is at index {index}")

            elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")


    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")


    def getbestseller(self):
        best = MaxQueue.MaxQueue()
        for x in self.shoppingCart:
            best.add(x)
        print(best.max())

    def reverseShoppingCart(self):
        start_time = time.time()
        self.shoppingCart.reverse()
        elapsed_time = time.time() - start_time
        print(f"Reversing ShoppingCart in {elapsed_time} seconds")

    def findFromIndexTitle(self, t: str):
        start_time = time.time()
        book = self.indextitle.find(t)
        if book != None:
            self.shoppingCart.add(book)
            print(f"Found {book}")
        else:
            print(f"Sorry, {t} was not found...")
        elapsed_time = time.time() - start_time
        print(f"Loading books by IndexTitle in {elapsed_time} seconds")

    def indexSortedTitle(self, t: str):
        start_time = time.time()
        book = self.searchTree.find(t)
        if t == "":
            print("Sorry, no book found.")
        elif book != None:
            self.shoppingCart.add(book)
            print(f"Found {book}")
        else:
            print(f"Sorry, {t} was not found...")
        elapsed_time = time.time() - start_time
        print(f"Loading books by SortedTitle in {elapsed_time} seconds")


    def kbestSeller(self, infix: str):
        index = 0
        best = BinaryHeap.BinaryHeap()
        counter = 0
        for i in self.bookCatalog:
            index +=1
            if infix == "":
                print("No books found")
                if index >= 1:
                    break

            if infix in i.title:
                x = i.rank * -1
                best.add(Book.Book(i.key,i.title,i.group,x,i.similar))

        for j in range(len(best)):
            r = best.remove()
            print(str(r.rank * -1),": ",r.title)
            counter +=1
            if counter == 10:
                break


    def SortableBookst(self, prefix : str, choice : int):
        start_time = time.time()

        merge = []
        quick = []
        index = 0

        for i in self.bookCatalog:
            index = index + 1
            if prefix == "":
                print("No books found")
                if index >= 1:
                    break

            if i.title.startswith(prefix):
                a = index, i.title
                if choice == 0:
                    merge.append(a)

                elif choice == 1:
                    quick.append(a)

        if choice == 0:
            print(f"Merge Sorted ", algorithms.merge_sort(merge))
        elif choice == 1:
            print(f"Quick Sorted ", algorithms.quick_sort(quick))
        elapsed_time = time.time() - start_time
        print(f"Sorting books completed in {elapsed_time} seconds")



    def mergeSort(self):
        booktitle = ArrayList.ArrayList()
        for y in self.bookSortedCatalog:
            booktitle.append(y.title)
        algorithms.merge_sort(booktitle)
        algorithms.merge_sort(self.bookSortedCatalog)


    def quickSort(self):
        booktitle = ArrayList.ArrayList()
        for y in self.bookSortedCatalog:
            booktitle.append(y.title)
        algorithms.quick_sort(booktitle)
        algorithms.quick_sort(self.bookSortedCatalog)
    def binarySearchTitle(self, title: str):
        start_time = time.time()
        if title == "":
            return None
        bookSortedCatalog = ArrayList.ArrayList()
        booktitle = ArrayList.ArrayList()
        for x in self.bookSortedCatalog:
            bookSortedCatalog.append(x)
        for y in bookSortedCatalog:
            booktitle.append(y.title)
        algorithms.quick_sort(bookSortedCatalog)
        algorithms.quick_sort(booktitle)
        i = not None
        while i is not None:
            i = algorithms.binary_search(booktitle, title)
            if i is not None:
                print(i,bookSortedCatalog[i])
                booktitle.set(i, "None")
        elapsed_time = time.time() - start_time
        print(f"Binary Search Completed in {elapsed_time} seconds")

















