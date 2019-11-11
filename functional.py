import numpy as np
import xml.etree.ElementTree as xml
import string
from colorama import *


class Funct:
    def __init__(self):
        my_list = ["Calgary", "Chicago", "New Jersey", "Montreal", "New Jersey"]
        self.my_list = my_list

    def add(self):
        print(self.my_list)
        print("Add element")
        while True:
            element = input()
            if not element:
                break
            if len(self.my_list) <= 10:
                self.my_list.append(element)
            else:
                self.my_list.pop(0)
                self.my_list.append(element)
            print(self.my_list)
        print("Your list is: %s" % self.my_list)

    def remove(self):
        print(self.my_list)
        print("Remove element")
        while self.my_list:
            try:
                element = input()
                if not element:
                    break
                elif element:
                    self.my_list.remove(element)
                    print(self.my_list)
            except:
                print("Element doesn't exist")
        print(self.my_list)

    def reverse(self):
        new_list = []
        print(self.my_list)
        print("Reversed string")
        for i in self.my_list:
            new_list.append(i[::-1])
        print(new_list)

    def search(self):
        print(self.my_list)
        print("Input element to find in list")
        while True:
            element = input()
            if not element:
                break
            if element in self.my_list:
                print("Element %s is located at %s position" % (element, self.my_list.index(element)))
            else:
                print("Couldn't find any match")

    def count(self):
        new_list = []
        for i in self.my_list:
            cur = len(i)
            new_list.append(cur)
        print(new_list)

    def compare(self):
        counter = {}
        for elem in self.my_list:
            counter[elem] = counter.get(elem, 0) + 1
        doubles = {element: count for element, count in counter.items() if count > 1}
        print(doubles)

    def create_xml(self):
        head = xml.Element(r'?xml version="1.0"?')
        root = xml.Element("Appointsments")
        head.append(root)
        appt = xml.Element("Appointment")
        root.append(appt)
        for i in self.my_list:
            element = xml.SubElement(appt, "bravo")
            element.text = "%s" % str(i)
        tree = xml.ElementTree(root)
        with open("my_xml.xml", "wb") as file:
            tree.write(file)

    def from_file(self):
        new_list = [word.split(' ') for word in open("text.txt", "r", encoding="utf8").readlines()]
        print(new_list)

    def character_check(self):
        from collections import defaultdict
        char_count = defaultdict(int)
        for word in self.my_list:
            for char in word:
                char_count[char] += 1
        print(char_count)

    def inner_search(self):
        print(self.my_list)
        print("Input str to search for in list:")
        while True:
            element = input()
            for item in self.my_list:
                if element in item:
                    print("%s was found in %s " % (element, item))
                else:
                    print("%s wasn't found in %s" % (element, item))
