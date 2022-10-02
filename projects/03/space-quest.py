print("\n")
print('''                                 ::: =,    ;
                             ;;=;;===      M
                ,=YVRMBBMMR=,   :i=
              :iVRRMMMMMMBMMM :=;  ==;======
             =tYMMMMMMBBMMM;=Y ,::;==iMMMMMMMMMM
            ;tYVBBMMVMMMM =; .,,,::;;=YVBBMMMMMMMMM
            ;tYVVYRMMM;=ti ...,,,;::==iMVMMMMMMMMMMMM
            ,=tYRBM;;tVB, ....,  ,::;====YVBMMMMMMMMMM
        ..   ,=t =tYVRB, .....,,,,=:;:;;i=VYMMRMMMMMMMM
       ;;..  ,===iYVVRY .....,,,;,,,,,:;;==t=RBMMMMMMMMM
     :;;:;=;,...       .......,,,,,,,,,:;;==Y=tYMMMMMMMM
    ;.,:,.....         ....,,,,,,,,,,,,,:;;;==YYMRMMMMMM;
    .......             .,,,,,,,,,,,,,,,,::;;;=YtVBMMMMM
  ;t ...                .,,,,,,,,,,,,,,,,,::;;i=RiRMMMMM
  ,=..                    .,,,,,,,,,,,,,,,:::;;=iYBBMM
                           .,,,,,,,,,,,,,,,,::;;;;tVB
          :VMM               .,,,,,,,,,,,,:,,,::;;=
         ,;VBM                 .,,,,,,,,,,,,,:,::
         ,,==                      `,,,,,,,''')
print("\n")
print("Your spaceship has been severly damaged by an unexpected malfuncion.")
print("You've lost all propulsion and you are accelerating toward the surface of an alien planet.\n")
choice1 = input("Do you try to [land] your ship or [eject]? ").lower()
if choice1 == "land":
    print("\nYou grab the controls and divert auxiliary power to your shields.")
    print("Your flight path takes you to a swampy area of the planet covered in strange vegetation.")
    print("Your ship crashes into the ground and luckily your shields hold. You exit the ship and look around.\n")
    print("To the east, you see what looks like rising [smoke]. To the west are some [mountains].\n")
    choice11 = input("Where do you want to go? ").lower()
    print(f"\nYou grab your supplies and head toward the {choice11}.\n")
    if choice11 == "smoke":
        print(
            "As you come nearer to the smoke you see what looks to be a small village of lizard people. They regard you with apprehension.")
        print(
            "One of the villagers approaches you and raises his hand. He points at your supplies and makes a hissing noise.\n")
        choice111 = input("Do you [give] your supplies to the lizardman, or [refuse]? ")
        if (choice111 == "give"):
            print("\nThe lizard man takes your pack and rummages through it.")
            print(
                "Satisfied that you do not have any weapons, he invites you to join the other villagers at the camp fire.")
            print("After a long night of delicious food and festivities, you learn that there is a starport nearby.")
            print("You reach the starport and are able to board a transport back to your homeworld.")
            print("\nYOU SURVIVED\n")
        else:
            print("\nYou refuse to let the lizardman take your belongings. You need them to survive!")
            print(
                "Unfortunately, the lizard people now regard you as a threat. They toss a net over you and wrestle you to the ground.")
            print("Something heavy slams into your head, and the world goes black.")
            print("The smell of smoke pulls you from your sleep. Your hands and legs are tied to a pole.")
            print("It appears that the lizard people have decided to have you for dinner.")
            print("\nGAME OVER\n")
    else:
        print("You arrive at the mountains. There are a few caves that might make a good [shelter].")
        print(
            "Or you could try to climb to the top of the mountain to see if you can get a good [radio] signal and call for help.\n")
        choice121 = input("What do you want to do? ")
        if choice121 == "shelter":
            print("\nYou head for the nearest cave to seek shelter.")
            print("Unfortunately it looks like something else had the same idea.")
            print("A giant crab-like creatuer is waiting for you inside, and it is hungry...")
            print("\nGAME OVER\n")
        else:
            print("\nYou reach the top of the mountain and are able to get a good radio signal.")
            print("You are able to contact a nearby starport and they agree to send out a rescue party.")
            print("\nYOU SURVIVED\n")
if choice1 == "eject":
    print("\nYou hit the eject button and are catapulted into space.")
    print("You watch as your prized spaceship crashes to the planet in a billowing fireball.")
    print("You have survived for now, but the planet's gravity is slowly pulling you closer and closer.")
    print("Soon you will enter the atmosphere and suffer the same fate as your ship.")
    print("But for now, you have a long time to regret your decision.")
    print("\nGAME OVER\n")
