def calculate_cube(x):
    return x**3
def calculate_square(x):
    return x**2
    
import pretty_print

def main():
    y=calculate_square(2)
    pretty_print.simple_print(y)
    z=calculate_cube(4)
    pretty_print.pro_print(z)
    
    
    
    
if __name__=='__main__':
    main()