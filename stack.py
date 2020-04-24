def stackOperations():
    # Declare a stack using a list
    namesstack = []

    namesstack.append('Joydeep')
    namesstack.append('Pushpita')
    namesstack.append('Ashis')
    namesstack.append('Debopriya')

    print('..................')
    print('Stack Initially...')
    print(namesstack)
    print('..................')

    print('First pop: ' + namesstack.pop())
    print('Second pop: ' + namesstack.pop())
    print('Third pop: ' + namesstack.pop())

    print('Adding a few more names..')

    namesstack.append('Joydeep')
    namesstack.append('Sourajit')
    namesstack.append('Shanaya')

    print('..................')
    print('Stack Now....')
    print(namesstack)
    print('..................')

#  ---- Call the function ---
stackOperations()