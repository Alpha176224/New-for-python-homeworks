class Vector:
    def __init__(self, *args):
        self.dimensional_size=len(args)
        for place in range(len(args)):
            setattr(self,f'p{place}',args[place])

    def __str__(self):
        my_tuple=tuple(value for value in self.__dict__.values())[1:]
        return f"Vector{my_tuple}"
    
    def __add__(self,other):
        try:
            if not isinstance(other, Vector):
                raise TypeError
            if self.dimensional_size!=other.dimensional_size:
                raise ValueError
            newslist=list()
            for index in range(1,self.dimensional_size+1):
                newslist.append(list(self.__dict__.values())[index]+list((other.__dict__.values()))[index])
        except TypeError:
            return f'TypeError: Can only add a Vector to another Vector.'
        except ValueError:
            return f'ValueError: Vectors must have the same dimension to be added.\nYou are trying to add {self.dimensional_size}-dimensional vector to {other.dimensional_size}-dimensional vector.'
        else:
            return Vector(*newslist)   
    def __sub__(self,other):
        try:
            if not isinstance(other, Vector):
                raise TypeError
            if self.dimensional_size!=other.dimensional_size:
                raise ValueError
            newslist=list()
            for index in range(1,self.dimensional_size+1):
                newslist.append(list(self.__dict__.values())[index]-list((other.__dict__.values()))[index])
        except TypeError:
            return f'TypeError: Can only subract a Vector to another Vector.'
        except ValueError:
            return f'ValueError: Vectors must have the same dimension to be subtracted.\nYou are trying to subtract {self.dimensional_size}-dimensional vector to {other.dimensional_size}-dimensional vector.'
        else:
            return Vector(*newslist)
    def __mul__(self,other):
        try:
            if not isinstance(other, Vector):
                raise TypeError
            if self.dimensional_size!=other.dimensional_size:
                raise ValueError
            dot_product=0
            for index in range(1,self.dimensional_size+1):
                dot_product+=((list(self.__dict__.values())[index])*(list(other.__dict__.values())[index]))
            return dot_product
        except TypeError: 
            return f'TypeError: Can only calculate dot product for two Vectors.'
        except ValueError:
            return f'ValueError: Vectors must have the same dimension to calculate dot product.\nYou are trying to calculate dot product for {self.dimensional_size}-dimensional vector and {other.dimensional_size}-dimensional vector.'
    def __rmul__(self, other):
        try:
            if not isinstance(other, (int, float)):
                raise TypeError
            newslist=list()
            for values in list(self.__dict__.values())[1:]:
                newslist.append(values*other)
            return Vector(*newslist)
        except TypeError:
            return f'TypeError: Can only calculate Scalar multiplication for a number and Vector.'
    
    def magnitude(self):
        sum_of_squares=0
        for _ in list(self.__dict__.values())[1:]:
            sum_of_squares+=_**2
        return sum_of_squares**(1/2)
    def normalize(self):
        if self.magnitude() == 0:
            raise ValueError("Cannot normalize a zero vector")
        newslist_to_normalize=list()
        for _ in list(self.__dict__.values())[1:]:
            newslist_to_normalize.append(_/self.magnitude())
        return Vector(*newslist_to_normalize)
    