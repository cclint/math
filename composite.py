
def Composite():
        alpha = []
        beta = []
        for elements in range(1,1000):
                if elements > 1:
                         for numbers in range(1, elements + 1): 
                              if elements % numbers == 0: 
                                      alpha.append(elements) 
                if alpha.count(elements) > 2:
                        beta.append(elements)
        return beta


print(Composite())
