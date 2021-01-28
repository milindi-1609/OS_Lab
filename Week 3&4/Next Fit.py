def NextFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    j = 0
    for i in range(n):
        while j < m:
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break
            j = (j + 1) % m
    print("Process No. Process Size Block no.")
    for i in range(n):
        print(i + 1, "         ", processSize[i],
              end="     ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blockSize = [5, 10, 20]
    processSize = [10, 20, 5]
    m = len(blockSize)
    n = len(processSize)
    NextFit(blockSize, m, processSize, n)
