def best_fit():
    # Initialize variables
    fragment = [0] * 20
    b = [0] * 20
    p = [0] * 20
    barray = [0] * 20
    parray = [0] * 20
    lowest = 9999

    # Input number of blocks and processes
    nb = int(input("Enter the number of blocks: "))
    np = int(input("Enter the number of processes: "))

    # Input sizes of blocks
    print("Enter the size of the blocks:")
    for i in range(1, nb + 1):
        b[i] = int(input(f"Block no.{i}: "))

    # Input sizes of processes
    print("Enter the size of the processes:")
    for i in range(1, np + 1):
        p[i] = int(input(f"Process no.{i}: "))

    # Best Fit Algorithm
    for i in range(1, np + 1):
        lowest = 9999
        temp = -1  # This is to store the index of the best fit block
        for j in range(1, nb + 1):
            if barray[j] == 0 and b[j] >= p[i] and (b[j] - p[i]) < lowest:
                lowest = b[j] - p[i]
                temp = j

        if temp != -1:
            barray[temp] = 1
            parray[temp] = i
            fragment[i] = lowest

    # Get the output of the results
    print("\nMemory Management Technique - Best Fit")
    print(f"{'Block No.':<10} {'Block Size':<12} {'Process No.':<16} {'Process Size':<16} {'Fragment':<12}")
    for i in range(1, nb + 1):
        if barray[i] == 1:
            process_index = parray[i]
            print(f"{i:<10} {b[i]:<12} {process_index:<16} {p[process_index]:<16} {fragment[process_index]:<12}")
        else:
            print(f"{i:<10} {b[i]:<12} {'Not Allocated':<16} {'Not Allocated':<16} {'No fragment':<12}")

# Call the function best_fit
best_fit()
