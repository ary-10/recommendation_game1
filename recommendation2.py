import pandas as pd
from random import*
anime_data = {
    "Title": [
        "Spirited Away", "Your Name", "Akira", "Princess Mononoke", 
        "My Neighbor Totoro", "Grave of the Fireflies", "Howl's Moving Castle", 
        "The Girl Who Leapt Through Time", "A Silent Voice", "Weathering With You",
        "Ghost in the Shell", "The Wind Rises", "Paprika", 
        "Nausicaä of the Valley of the Wind", "5 Centimeters Per Second", 
        "Castle in the Sky", "Perfect Blue", "The Tale of the Princess Kaguya", 
        "The Secret World of Arrietty", "Wolf Children", "The Red Turtle", 
        "Children Who Chase Lost Voices", "Tokyo Godfathers", 
        "I Want to Eat Your Pancreas", "Flavors of Youth", 
        "Maquia: When the Promised Flower Blooms", "Promare", 
        "Sword of the Stranger", "The Garden of Words", "Summer Wars",
        "The Boy and the Beast", "Ride Your Wave", "Josee, the Tiger and the Fish", "The Anthem of the Heart", 
        "Tamako Love Story", "In This Corner of the World", "Mirai", "The Cat Returns",
        "The Place Promised in Our Early Days", "Liz and the Blue Bird", "Penguin Highway", 
        "Modest Heroes", "When Marnie Was There", "Only Yesterday", "The Garden of Sinners", 
        "Millennium Actress", "The Case of Hana and Alice", "Colorful", "The Girl from the Other Side", 
        "On-Gaku: Our Sound", "The Deer King", "The Wonderland", "A Whisker Away", "Okko's Inn",
        "Mary and the Witch's Flower", "Blame!", "Big Fish & Begonia",
        "Words Bubble Up Like Soda Pop", "The Empire of Corpses"
    ],
    
    "Genre": [
        "Fantasy", "Romance", "Sci-Fi", "Fantasy","Fantasy","Drama","Adventure","Sci-Fi","Romance","Romance","Sci-Fi","Biography", 
        "Sci-Fi", "Fantasy","Romance", "Fantasy","Psychological", 
        "Fantasy","Fantasy",  "Drama", 
        "Fantasy","Fantasy","Comedy", 
        "Drama", "Romance","Fantasy", 
        "Action","Action", "Romance", 
        "Sci-Fi","Fantasy", "Fantasy", "Romance", "Romance", "Romance", "Drama", 
        "Fantasy", "Fantasy", "Romance", "Drama", "Fantasy", "Fantasy", "Drama",
        "Romance", "Action", "Drama", "Drama", "Supernatural", "Fantasy", "Music", "Fantasy", "Fantasy",
        "Fantasy", "Fantasy", "Sci-Fi", "Fantasy", "Romance", "Romance", "Sci-Fi"
    ]
}
options={"types available":["romance","Sci-Fi","Drama", "Supernatural", "Fantasy", "Music","Psychological","comedy","adventure","biography"]}
fo=pd.DataFrame(options)
df=pd.DataFrame(anime_data)

try:
    answer=input("are you bored?do you feel like watching anime?yes?NO?")
except:
    print("somthing went wrong, try again!")

if answer.lower=="no":
    print("okay i thought i could help you choosing an anime to watch")
    try:
        answer2=input("do you want me to give you a suggestion?")
    except:
        print("somthing went wrong, try again!")
        
    if answer2.upper=="YES":

        print(fo)
        try:
            preferences=input("tell me what type you want to watch")
        except:
            print("somthing went wrong, try again!")
       
        print("hemmm now i will give you the best recommendation")
        t=[]
        for index, genre in enumerate(anime_data["Genre"]):
            
            if genre.lower() == preferences.lower():  
                t.append(anime_data["Title"][index])
        result=choice(t)
        print(result,"is a good option")
if answer.upper()=="YES":
    print(fo)
    preferences=input("tell me more about you type")
    print("cool")
    t=[]
    for index, genre in enumerate(anime_data["Genre"]):
            
        if genre.lower() == preferences.lower():  
            t.append(anime_data["Title"][index])
    result=choice(t)
    print(result,"is a good option")
try:        
    like=input("are you satisfied!yes?no?")
except:
    print("somthing went wrong, try again!")
if like.lower()=="yes":
    print("happy to hear this")
elif like.upper()=="NO":
    try:
        
        type=input("so what is the genre you want to chose?")
    except:
        print("something went wrong try again!")
    t=[]
    for index, genre in enumerate(anime_data["Genre"]):
        if genre.lower() == type.lower():  
            t.append(anime_data["Title"][index])
    result=choice(t)
    print(result,"!YOU WILL DEFINITELY LIKE THIS")
        
        
    

    
        