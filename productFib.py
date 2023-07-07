#Difficulty: 5 kyu

def productFib(prod):
    sequence = []
    def fibSequence(v, n):
        if len(sequence) == 0:
            sequence.append(n)
            sequence.append(v)
            return v * n
        else:
            sequence.append(v + n)
            return (sequence[len(sequence)-1] * sequence[len(sequence)-2])
    
    n = 0
    f = 1
    fibProduct = 0
    
    while fibProduct < prod:
        fibProduct = fibSequence(f, n)
        f = sequence[len(sequence)-1]
        n = sequence[len(sequence)-2]
        
        
    if fibProduct == prod:
        # Check if prod is a value smaller than fibProduct, as the loop cannot run otherwise
        try:
            return [sequence[len(sequence) - 2], sequence[len(sequence) - 1], True]
        # If so, return the first and second values of Fibonacci sequence manually
        except IndexError:
            return [n, f, True]
            
    else:
        return [sequence[len(sequence) - 2], sequence[len(sequence) - 1], False]

if __name__ == "__main__":
    print(productFib(4895))
