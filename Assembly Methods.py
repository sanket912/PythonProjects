# This Program will calculate the Assembly method required
# Updated now

NP = int(input("The Total Number of Products Made, NP: "))  # Can only be equal to one.
if NP == 1:
    print("We can Now Proceed.")
else:
    print("NP can only be equal to 1!")

NA = int(input("Total Number of Parts per Assembly, NA: "))
NT = int(input("Total Number of Parts required to make all variants, NT: "))  # Different parts for different variants
                                                                              # of the same product. Inout the total
                                                                              #  number of parts to manufacture all the
                                                                              #  variants.
ND = int(input("Number of design changes during product life, ND: "))
AnP = int(input("The Total Annual Production is, AnP (in Millions): "))
SH = int(input("Number of Worker Shifts, SH: "))
VS = float(AnP / SH)  # Volume manufactured per shift

print("Annual Production per shift is: ", VS)

WA = int(input("Annual Salary per worker, WA: "))
QE = int(input("Automation Investment per worker, QE: "))
RI = float(SH * QE / WA)  # The Company Investment Potential
print("Company Investment Potential, RI: ", RI)

# Assembly Methods

MA = "Manual Assembly"
MM = "Manual Assembly with Mechanical Assistance"
AI = "Automatic Assembly with Indexing Machine"
AF = "Automatic Assembly with Free Transfer"
AP = "Automatic Assembly with Programmable Work-heads"
AR = "Automatic Assembly with Robots"

# Loop Start

if NT < 1.5 * NA and ND < 0.5 * NA:


    if RI >= 5.0:

        if VS > 0.65 * 10**6:
            if NA >= 16:
                print("The preferred Assembly Method is", AF)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AF)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.65 * 10**6 >= VS > 0.4 * 10**6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AI)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.4 * 10**6 >= VS > 0.2 * 10**6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AI, "or", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif VS <= 0.2 * 10**6:
            print("The preferred Assembly Method is", MM)


    elif 5.0 > RI > 2.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AF)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AF, "or", AI)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AI)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MM)


    elif 2.0 >= RI >= 1.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AF)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AI, "or", AF)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MM, "or", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AI)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM, "or", AI)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MM)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MM, "or", MA)


    elif RI < 1.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MM, "or", AF)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM, "or", AI)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MM)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MM)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MA)


elif NT >= 1.5 * NA or ND >= 0.5 * NA:

    if RI >= 5.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AP)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AP)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI, "or", MM)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AI)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MM)


    elif 5.0 > RI > 2.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AP)
            elif NA <= 6:
                print("The preferred Assembly Method is", AI, "or", AP)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", AP)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MA)


    elif 2.0 >= RI >= 1.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP, "or", MM)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM, "or", AP)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM, "or", AP)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", AP)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MA, "or", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MA, "or", MM)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MA)


    elif RI < 1.0:

        if VS > 0.65 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MM)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MM)

        elif 0.65 * 10 ** 6 >= VS > 0.4 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MA, "or", MM)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MA, "or", MM)
            elif NA <= 6:
                print("The preferred Assembly Method is", MA, "or", MM)

        elif 0.4 * 10 ** 6 >= VS > 0.2 * 10 ** 6:
            if NA >= 16:
                print("The preferred Assembly Method is", MA)
            elif 15 >= NA >= 7:
                print("The preferred Assembly Method is", MA)
            elif NA <= 6:
                print("The preferred Assembly Method is", MA)

        elif VS <= 0.2 * 10 ** 6:
            print("The preferred Assembly Method is", MA)
