# Programmer: Cory DeMar
# ComSc 20
# Assognment #13
# Part 1: Planetary Density
# 4-26-17

def avg(data):
    #find avarage of a list of input data. if list is empty, return zero.
    if len(data) > 0:
        result = sum(data) /len(data)
    else:
        result = 0
    return result

def median(data):
    #find median of a list of input data; sort a copy of the original data to avoid clobbering orginal.
    copy = data [:]
    copy.sort()
    n = len(copy)
    if len(copy) % 2 == 0:
        result = (copy[(n//2)] + copy[(n//2) - 1]) / 2.0 #if amount is Even
    else:
        result = copy[(n-1) // 2]  #if amount is odd
        return result
    
def main():
    infile = open('density.txt', 'r')
    density = []
    for line in infile:
        data = line.split()
        density.append(float(data[1]))
    infile.close()

    # Figure out stats
    min_density = min(density) #free
    max_density = max(density) #free
    avg_density = avg(density)
    median_density = median(density)

    print ('Minimum density:', format(min_density, '.2f'))
    print ('Maximum Density:', format(max_density, '.2f'))
    print ('Average Density:', format(avg_density, '.2f'))
    print ('Median Density:', format(median_density, '.2f'))
    
main()
