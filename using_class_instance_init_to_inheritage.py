'''
class App:
    def __init__(self):
        
        self.tetris=Tetris(self)#
    def draw(self):
        self.tetris.draw_grid()

class Tetris: # all Tetromino in the field
    def __init__(self,app):
        self.app=app
    def draw_grid(self):
        print(self.app)

char_a=App()
char_a.draw()
'''
class A:
    def __init__(self):
        self.b = B(self)  # 创建类B的实例对象，并将类A的实例作为参数传递
        # 通过在init中建立实例对象，实现 将自身类实例传递给其他类作为实例变量
        print(type(self.b))
        self.param=5
        print("run initial A")
    
    def position(self):
        print("run position() in A")
        return self.b.get()
        # 类A的方法实现，返回位置信息
    
class B:
    def __init__(self, a):
        self.a = a  # 将类A的实例保存为类B的实例变量
        print(type(self.a))
        print("run initial B")
    
    def get(self):
        position = self.a.param  # 使用类A的实例调用其position方法获取位置信息
        print("run get() in B")
        return position
    
a_instance=A()
print(a_instance.position())


'''
# result
<class '__main__.A'>
run initial B
<class '__main__.B'>
run initial A
run position() in A
run get() in B
5
'''