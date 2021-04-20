global userList, properties
userList = []
properties = ['username', 'reputation', 'badges', 'posts']

class User:
    def __init__(self, username, reputation, badges, posts):
        for prop in properties:
            setattr(self, prop, locals()[prop])
    
    def __add__(self, other):
        return User([getattr(self, prop) + getattr(other, prop) for prop in properties])

    def __sub__(self, other):
        struct = []
        for prop in properties:
            lhs = getattr(self, prop)
            rhs = getattr(other, prop)
            if [type(lhs), type(rhs)] == [[int, float], [int, int]]:
                struct.append(lhs - rhs)
            elif [type(lhs), type(rhs)] == [[string, string]]:
                struct.append(lhs + rhs)
       
        return User(struct)

    def __mul__(self, other):
        struct = []
        for prop in properties:
            lhs = getattr(self, prop)
            rhs = getattr(other, prop)
            if [type(lhs), type(rhs)] == [[int, float], [int, int], [string, int]]:
                struct.append(lhs * rhs)
            elif [type(lhs), type(rhs)] == [[string, string]]:
                struct.append(lhs + rhs)
       
        return User(struct)

    def __truediv__(self, other):
        struct = []
        for prop in properties:
            lhs = getattr(self, prop)
            rhs = getattr(other, prop)
            if [type(lhs), type(rhs)] == [[int, float], [int, int]]:
                struct.append(lhs / rhs)
            elif [type(lhs), type(rhs)] == [[string, string]]:
                struct.append(lhs + rhs)
       
        return User(struct)

    def __floordiv__(self, other):
        struct = []
        for prop in properties:
            lhs = getattr(self, prop)
            rhs = getattr(other, prop)
            if [type(lhs), type(rhs)] == [[int, float], [int, int]]:
                struct.append(lhs // rhs)
            elif [type(lhs), type(rhs)] == [[string, string]]:
                struct.append(lhs + rhs)
       
        return User(struct)
   
    def __eq__(self, other):
        this = that = 0
        for prop in properties[1:]:
             this += getattr(self, prop)
	           that += getattr(other, prop)
	      return this == that

    def __lt__(self, other):
	      this = that = 0
        for prop in properties[1:]:
             this += getattr(self, prop)
	           that += getattr(other, prop)
	      return this < that

    def __le__(self, other):
	      this = that = 0
        for prop in properties[1:]:
             this += getattr(self, prop)
	           that += getattr(other, prop)
	      return this <= that

    def __ne__(self, other):
	      this = that = 0
        for prop in properties[1:]:
             this += getattr(self, prop)
	           that += getattr(other, prop)
	      return this != that

    def __ge__(self, other):
	      this = that = 0
        for prop in properties[1:]:
             this += getattr(self, prop)
	           that += getattr(other, prop)
	      return this >= that

    def __gt__(self, other):
	      this = that = 0
        for prop in properties[1:]:
             this += getattr(self, prop)
	           that += getattr(other, prop)
	      return this > that
