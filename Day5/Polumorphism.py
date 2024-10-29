class fruits:
    def color():
        pass

class Orange(fruits):
    def color(self):
        print('Orange is Orange in color')

class apple(fruits):
    def color(self):
        print('apple is red in color')

app = apple()
org = Orange()

for x in (app,org):
    x.color()