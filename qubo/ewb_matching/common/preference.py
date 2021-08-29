# operations to switch minimize / maximize.

class Algorithm :
    default = 'default'

    @staticmethod
    def is_sqa(algo) :
        if algo == Algorithm.default:
            return True
       
        return False
   
    
algorithm = Algorithm()




class Minimize :
    @staticmethod
    def sign(v) :
        return v.copy()
    @staticmethod
    def best(list) :
        return min(list)
    @staticmethod
    def sort(list) :
        return sorted(list)
    def __int__(self) :
        return 0

    
class Maximize :
    @staticmethod
    def sign(v) :
        return -v
    @staticmethod
    def best(list) :
        return max(list)
    @staticmethod
    def sort(list) :
        return sorted(list, reverse = true)
    def __int__(self) :
        return 1

minimize = Minimize()  #: telling solvers to minimize QUBO energy.
maximize = Maximize()  #: telling solvers to maximize QUBO energy.
