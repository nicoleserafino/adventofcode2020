def Find2():
    data = list()

    with open('C:\\Users\\nserafino\\Documents\\Other\\Advent of Code\\2020\\Day1\\input.txt', 'r') as file:
        for line in file:
            data.append(int(line.strip('\n'). strip('\r')))

    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] + data[j] == 2020:
                product = data[i] * data[j]
                print('variables: ', data[i], data[j])
                print('Product: ', product)

def Find3():
    data = list()

    with open('C:\\Users\\nserafino\\Documents\\Other\\Advent of Code\\2020\\Day1\\input.txt', 'r') as file:
        for line in file:
            data.append(int(line.strip('\n'). strip('\r')))

    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    product = data[i] * data[j] * data[k]
                    print('variables: ', data[i], data[j], data[k])
                    print('Product: ', product)    

Find2()
Find3()
