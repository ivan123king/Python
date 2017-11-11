__author__ = 'lenovo'

def make_pizza(size,*tips):
    print("make size "+str(size)+"px with follow tips:",end=' ')
    for tip in tips:
        print(tip,end=',')

# make_pizza(56,'mill','milk')