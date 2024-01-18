def zweierpotenz(n):
    if n == 0:
        return 1
    else: 
        if n%2 == 1:
            return 2*zweierpotenz(n-1)
        else:
            temp = zweierpotenz(n/2)
            return temp*temp
    
    
 
def main():
    wiederholen = True
    while wiederholen:
        exponent = int(input('Von welcher positiven Ganzzahl wollen sie die Zweierpotenz errechnen? '))
        if exponent < 0:
            print('Bitte eine Ganzzahl eingeben, die größer gleich  0 ist')
            continue
        wiederholen = False
    ergenis=zweierpotenz(exponent)
    print(f'Die 2 hoch {exponent} = {ergenis}')

   
if __name__ == '__main__':
    main()