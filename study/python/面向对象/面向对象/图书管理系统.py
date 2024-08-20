#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27
class Book:
    def __init__(self, title, author, publish_date):
        self.title = title
        self.author = author
        self.publish_date = publish_date

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publish_date(self):
        return self.publish_date


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        添加图书到图书馆的图书列表中
        """
        self.books.append(book)

    def borrow_book(self, title):
        """
        根据书名借出图书，如果找到对应书名的图书，则从图书列表中移除，并返回该图书对象
        """
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                return book

    def return_book(self, book):
        """
        将归还的图书对象添加到图书列表中
        """
        self.books.append(book)

    def show_books(self):
        """
        显示当前图书馆中所有图书的书名、作者和出版日期
        """
        for book in self.books:
            print("书名：", book.get_title())
            print("作者：", book.get_author())
            print("出版日期：", book.get_publish_date())


# 测试
# 创建一个图书馆实例
library = Library()

# 创建几本图书并添加到图书馆中
book1 = Book("Python编程入门", "张三", "2021-01-01")
book2 = Book("Java编程基础", "李四", "2021-02-01")
book3 = Book("C++高级编程", "王五", "2021-03-01")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# 显示所有图书
library.show_books()

# 借出一本图书并打印出借出的书名
borrowed_book = library.borrow_book("Java编程基础")
if borrowed_book:
    print("借出的书：", borrowed_book.get_title())

# 再次显示所有图书
library.show_books()

# 归还图书并打印出归还的书名
library.return_book(borrowed_book)
print("归还书籍：", borrowed_book.get_title())

# 最后再次显示所有图书
library.show_books()
