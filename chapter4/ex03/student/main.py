def skip_integers(args*):
    for i in args:
        if type(i) == int:
                continue
        else:
             print(i)
             