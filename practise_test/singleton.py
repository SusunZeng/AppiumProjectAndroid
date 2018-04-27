# #coding=utf-8
#
#
# import threading
#
# class SingletonType(type):
#     _instance_lock = threading.Lock()
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
#         return cls._instance
#
# class Foo(metaclass=SingletonType):
#     def __init__(self,name):
#         self.name = name
#
#
# obj1 = Foo('name1')
# obj2 = Foo('name2')
# print('打印：',obj1,obj2)
#

#coding=utf-8
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class MyClass:
    """实际生成实例的类
    """
    foo = "foo"
    def display(self):
        return (id(self))


@singleton
class OtherClass:
    """另一个类
    """
    pass
