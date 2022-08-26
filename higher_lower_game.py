from art import logo,vs
import game_data
import random

print(logo)









def comparing():
    to_continue=True
    score=0
    while to_continue==True:
        num_people=len(game_data.data)
        # print(num_people)
        



        for person in range(num_people):
            p1=random.choice(game_data.data)

        # print(p1)
        for person in range(num_people):
            p2=random.choice(game_data.data)
        
        
        p1_name=p1["name"]+", "+p1["description"]+", from "+p1["country"]
        p2_name=p2["name"]+", "+p1["description"]+", from "+p1["country"]
        print(f"Compare A: {p1_name}",vs,f"\n\nAgainst B:  {p2_name}")
        decision=input("Who has more followers? Type 'A' or 'B' :  ").strip().lower()

        p1_val=p1["follower_count"]
        p2_val=p2["follower_count"]
        
        # print(p1_val)
        # print(p2["follower_count"])
        
        if decision=="a":
            
            if p1_val>p2_val:
                print("Yes ! You are right!")
                score=score+1
                print("Your current score is : ",score)
                
            else:
                print(f"Nope ",p2["name"]," is more famous :D")
                print("Your final score is : ",score)
                to_continue=False
                
        if decision=="b":
            if p1_val>p2_val:
                
                print(f"Nope ",p1["name"]," is more famous :D")
                print("Your final score is : ",score)
                to_continue=False
                
                
            else:
                print("Yes ! You are right!")
                score=score+1
                print("Your current score is : ",score)
    
    

comparing()