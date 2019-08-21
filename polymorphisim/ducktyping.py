class duck:
    def talk(self):
        print('quack quack')

class human:
    def talk(self):
        print("hello")

def callTalk(obj):
    obj.talk();

d=duck()
callTalk(d)

h=human()
callTalk(h)
