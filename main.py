def meny():
    print("---------------Meny---------------")
    print("1. Visa alla atomer")
    print("2. Träna på atomnummer")
    print("3. Träna på atombeteckningar")
    print("4. Träna på atomvikter")
    print("5. Sluta")
    print("----------------------------------")

meny()
option = int(input("Vad vill du göra?: "))

if option == 1:
    #Val 1 har kallats
    print("Val 1 har kallats")
if option == 3:
    #Val 3 har kallats
    print("Val 3 har kallats")


else:
    print("Inget val från menyn valdes, välj vad som ska göras från menyn: ")
    start_meny()