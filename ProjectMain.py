import matplotlib.pyplot as plt

#recieving a list of tuples  ((1 2000), (2 3222), (3 2121))
def makeGraph(List):
    x = [0]
    y = [0]

    for sublist in List:
        x.append(sublist[0])
        y.append(sublist[1])

    plt.bar(x, y, color=('blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'))
    plt.title('Frequency over time')
    plt.xlabel('Months')
    plt.ylabel('Times occurred')
    plt.show()


#test case
makeGraph(((1, 2000), (2, 3033) , (4, 2121), (3, 2001), (5, 2000), (6, 3033) , (7, 2121), (8, 2001), (9, 2000), (10, 3033) , (11, 2121), (12, 2001), (13, 20000), (14, 2000), (15, 3033) , (16, 2121), (17, 2001), (18, 2000), (19, 3033) , (20, 2121), (21, 2001), (22, 2000), (23, 3033) , (24, 2121), (0, 2001)))