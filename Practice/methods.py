#practicing class methods
class Bird:

    num = 0
    @classmethod
    def initiate(change):
        change.num += 1;

    @classmethod
    def display(change, name):
        print("{} have {} wings".format(name,change.num))

Bird.initiate()
Bird.initiate()

Bird.display("pigeon")
Bird.display("Rabbit")
