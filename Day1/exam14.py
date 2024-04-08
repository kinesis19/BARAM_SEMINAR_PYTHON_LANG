for i in range(1, 10):
    if i is 3: continue
    
    for j in range(1, 10):
        if j not in [2, 4, 6, 8]: continue
        print(f"{i} x {j} =  {i*j}")

    print('\n')


