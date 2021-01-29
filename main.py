from __future__ import annotations
from typing import List


class Ebay:
    def attach(self, buyer): pass
    def detach(self, buyer): pass
    def notify(self): pass


class Subject(Ebay):
    status: List
    buyer: List[Buyer] = []
    def attach(self, observer):
        print("Ebay: Добавился подписчик.")
        self.buyer.append(observer)

    def detach(self, observer):
        self.buyer.remove(observer)

    def notify(self):
        print("Ebay: Идет оповещение...")
        for observer in self.buyer:
            observer.update(self)

    def action(self, _status):
        print("\nEbay: Поступление товара.")
        self.status = _status

        print(f"Ebay: В наличии появилось: {self.status}")
        self.notify()

class Buyer:
    def update(self, _subject): pass

class Buyer_a(Buyer):
    _name: str
    name: str
    c: List = []
    f: List = []

    def prod(self, _name):
        self.name = _name

    def update(self, _subject):

        for a in self.name:
            for b in _subject.status:
                if a == b:
                    self.c.append(a)

        if self.c == self.name:
            print("Buyer_a: Reacted")
        else:
            self.f = list(set(self.name) - set(self.c))

            print("Buyer_a: Данного продукта нет в наличии: ", self.f)

class Buyer_b(Buyer):
    _name: str
    name: str
    c: List = []
    f: List = []

    def prod(self, _name):
        self.name = _name

    def update(self, _subject):

        for a in self.name:
            for b in _subject.status:
                if a == b:
                    self.c.append(a)

        if self.c == self.name:
            print("Buyer_b: Reacted")
        else:
            self.f = list(set(self.name) - set(self.c))

            print("Buyer_b: Данного продукта нет в наличии: ", self.f)

class Buyer_c(Buyer):
    _name: str
    name: str
    c: List = []
    f: List = []
    def prod(self, _name):
        self.name = _name
    def update(self, _subject):

        for a in self.name:
            for b in _subject.status:
                if a == b:
                    self.c.append(a)

        if self.c == self.name:
            print("Buyer_c: Reacted")
        else:
            self.f = list(set(self.name) - set(self.c))

            print("Buyer_c: Данного продукта нет в наличии: ", self.f)





subject = Subject()

sub_a = Buyer_a()
a = ["Kartoshka", "Rise"]
sub_a.prod(a)
subject.attach(sub_a)

sub_b = Buyer_b()
b = ["Moloko", "Pomidor"]
sub_b.prod(b)
subject.attach(sub_b)

sub_c = Buyer_c()
c = ["Cok", "Pirog"]
sub_c.prod(c)
subject.attach(sub_c)


subject.action(["Cok", "Pirog","Moloko", "Kartoshka", "Rise", "Tea", "Spoon"])
