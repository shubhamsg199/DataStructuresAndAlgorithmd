class Item:
    def __init__(self,name,type,price):
        self.name = name
        self.type = type
        self.price = price

class Store:
    def __init__(self,inventory):
        self.inventory = inventory

    def buyItem(self,name,qty):
        sum = 0
        for x,y in self.inventory.items():
            if name == x.name:
                if qty <= y:
                    sum += x.price * qty
                    self.inventory[x] -= qty
                    break
                elif qty > y:
                    sum += x.price * y
                    self.inventory[x] = 0
                    break
                else:
                    sum = 0

            else:
                sum = 0

        return sum


if __name__ == '__main__':
    d = {}
    n = int(input())
    for i in range(n):
        name = input().capitalize()
        type = input()
        price = int(input())
        q = (Item(name,type,price))
        stock = int(input())
        d[q] = stock

    store = Store(d)
    a = int(input())
    for i in range(a):
        k = input().capitalize()
        quantity = int(input())
        res = store.buyItem(k,quantity)
        if res == 0:
            print(k,"is not available")
        else:
            print("Bill of the item ",k,"=",res)

    print("Stock in Hand:")
    for t,u in d.items():
        print(t.name.capitalize(),u)