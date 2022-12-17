
go = "go"
stop = "stop"
dangerous = "yellow"
green = "green"
red = "red"
yellow = "yellow"
go = red
green = stop
dangerous = yellow
if go == red:
    print("human can cross and car must be stop.")
if stop == green:
    print("Car can be go and human must be stop.")
if yellow == dangerous:
    print("Please wait it dangerous.")
else:
    print("The electric cut out.")




#Police and man
#you can enter this word for ordered this program : "_can_go?" , "_stop?" and "_can_cross" ;

#let
walk_go = "_can_go?"
walk_stop = "_stop?"
dangerous1 = "_can_cross"

road_green = walk_stop
road_red = walk_go
road_yellow = dangerous1
human_police = input("Please use ordered words")

#Solution,
if human_police == walk_go:
    print("Yes, you can go safely.")
elif human_police == walk_stop:
    print("Sure, you want to die?")
elif human_police == dangerous1:
    print("Stop! Stop! too dangerous.")
else:
    print("The electric cut out")

