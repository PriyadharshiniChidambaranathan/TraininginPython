scoreIn = input("Enter score:")
try:
    s = float(scoreIn)
    try:
        if s > 1.0:
            print ("Out of Upper Range")
        elif s >= 0.9:
            print ("A")
        elif s >= 0.8:
            print ("B")
        elif s >= 0.7:
            print ("C")
        elif s >= 0.6:
            print ("D")
        elif s < 0.6:
            print ("F")
    except:
        print ("Out of Lower Range")
except:
    print ("Numeric Data Only")
