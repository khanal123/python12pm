class StaticMethod:
    x=10
    @staticmethod
    def test(name):
        print('',name)
    @classmethod
    def get(cls):
        print(cls.x)
StaticMethod.test('suman')
StaticMethod.get()