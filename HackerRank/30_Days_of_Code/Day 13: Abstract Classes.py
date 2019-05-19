# from abc import ABCMeta, abstractmethod
# class Book:
#     __metaclass__ = ABCMeta
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(self):
#         pass
#
# #Write MyBook class
# class MyBook(Book):
#     def __init__(self,title,author,price):
#         # self.title=title
#         # self.author=author
#         super().__init__(title, author)
#         self.price=int(price)
#     def display(self):
#         # super(self).display()
#         print "Title: %s"%self.title
#         print "Author: %s"%self.author
#         print "Price: %s"%self.price
#
# title=raw_input()
# author=raw_input()
# price=int(raw_input())
# new_novel=MyBook(title,author,price)
# new_novel.display()



# from abc import ABCMeta, abstractmethod
#
#
# class Book(object, metaclass=ABCMeta):
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     @abstractmethod
#     def display(self): pass
#
#
# class MyBook(Book):
#     def __init__(self, title, author, price):
#         super().__init__(title, author)
#         self.price = price
#
#     def display(self):
#         print("Title: " + self.title + "\nAuthor: " + self.author + "\nPrice: " + str(self.price))
#
#
# title = input()
# author = input()
# price = int(input())
# new_novel = MyBook(title, author, price)
# new_novel.display()

from abc import ABCMeta, abstractmethod
class Book():
    __metaclass__ =  ABCMeta
    def __init__(self, title, author):
		self.title = title
		self.author = author
    @abstractmethod
    def display(self):
		pass


# Write MyBook class
class MyBook(Book):
	def __init__(self, title, author, price):
		super(Book).__init__(title, author)
		self.price = price

	def display(self):
		print("Title:", self.title)
		print("Author:", self.author)
		print("Price:", self.price)


title = raw_input()
author = raw_input()
price = int(raw_input())
new_novel = MyBook(title, author, price)
new_novel.display()




# Java code:
# import java.util. *;
# abstract class Book {
#     String title;
#     String author;
#
#     Book(String title, String author) {
#         this.title = title;
#         this.author = author;
#     }
#
#     abstract void display();
# }
# class MyBook extends Book
#     {
#     int price;
#     MyBook(String t , String a , int p)
#         {
#         super(t,a);
#         this.price =p;
#     }
#     void display()
#         {
#         System.out.println("Title: "+title);
#         System.out.println("Author: "+author);
#         System.out.println("Price: "+price);
#     }
# }
# public class Solution {
#
#     public static void main(String[] args) {
#     Scanner scanner = new Scanner(System.in );
#     String title = scanner.nextLine();
#     String author = scanner.nextLine();
#     int price = scanner.nextInt();
#     scanner.close();
#
#     Book book = new MyBook(title, author, price);
#     book.display();
#     }
# }