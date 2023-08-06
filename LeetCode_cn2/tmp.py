
def l(a):
    print('000')
    return len(a)

a = [ 1, 2, 3, 4, 4,]
n = l(a)
if n > 3:
    print(f"List is too long ({n} elements, expected <= 10)")