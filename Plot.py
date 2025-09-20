import math
import matplotlib.pyplot as plt
import pandas as pd

class Node:
    def __init__(self, Current_Coin: int):
        self.Starting_Coin = Current_Coin 
        self.Iron_Ingot_Per_Bow = 1 
        self.Dweamer_Ingot_Per_Bow = 2 
        self.Iron_Ingot_Cost = 11 
        self.Dweamer_Ingot_Cost = 47 
        self.Bow_Sale_Price = 156
        self.Iron_Cost_Per_Bow = (self.Iron_Ingot_Per_Bow*self.Iron_Ingot_Cost)
        self.Dweamer_Cost_Per_Bow = (self.Dweamer_Ingot_Per_Bow*self.Dweamer_Ingot_Cost)
        self.Cost_Per_Bow = self.Iron_Cost_Per_Bow + self.Dweamer_Cost_Per_Bow
        self.Profit_Per_Bow = self.Bow_Sale_Price - self.Cost_Per_Bow

    def Generate_Figure(self, Loops: int, Coin: list, Title: str, Visible_Data_Point=5):
        """
        Loops range starts from 0 to account for the starting coin value
        You can also change the number of visible data points, it will default to 5 (theres no reason for 5 just think it looks fine)
        """
        loops = list(range(0,Loops+1))
        coin = Coin

        plt.plot(loops, coin)

        step = max(1, len(loops) // Visible_Data_Point)  

        for x, y in zip(loops[::step], coin[::step]):
            plt.text(x, y, f"{y:,.0f}", fontsize=8, ha='left', va='bottom')

        plt.title(f"Growth Of {Title}")
        plt.xlabel("Loop #")
        plt.ylabel("Total Coin")
        plt.grid(True)

        

    def Generate_Graph(self, Loops_list: int, Coins_list: list, Titles: list, Visible_Data_Point=5):
        for loops in range(0, len(Coins_list)):
            plt.figure(loops+1)
            self.Generate_Figure(Loops_list[loops], Coins_list[loops], Titles[loops])
            

        plt.show()
        

    def Loop(self) -> dict:
        """
        Runs a single loop needs to be put in a for or while loop
        Does NOT update self.Start_Coin so it can be used to display single
        Update self.Start_Coin with the loop_result['Profit'] for next loop
        Bows Made will also equal Iron_Ingots
        """
        Money_On_Iron = math.floor(self.Starting_Coin * self.Iron_Cost_Per_Bow / self.Cost_Per_Bow)
        Money_On_Dweamer = math.floor(self.Starting_Coin * self.Dweamer_Cost_Per_Bow / self.Cost_Per_Bow)

        Iron_To_Buy = math.floor(Money_On_Iron / self.Iron_Ingot_Cost)
        Dweamer_To_Buy = math.floor(Money_On_Dweamer / self.Dweamer_Ingot_Cost)

        Coin_Post_Loop = Iron_To_Buy  * self.Bow_Sale_Price

        Loop_Result = {
            "Iron_Ingot": Iron_To_Buy,
            "Dweamer_Ingot": Dweamer_To_Buy,
            "Profit": Coin_Post_Loop,
        }

        return Loop_Result


##Running 

Loop_Limit = 10
Current_Coin = 6723

BowLoop = Node(Current_Coin)
Coin_Profits = [Current_Coin]
Iron_Ingots = [0]
Dweamer_Ingots = [0]
Titles = ["Coin", "Iron", "Dweamer"]
df_list = []

for i in range(0, Loop_Limit):
    result = BowLoop.Loop()

    Coin_Profits.append(result['Profit'])
    Iron_Ingots.append(result['Iron_Ingot'])
    Dweamer_Ingots.append(result['Dweamer_Ingot'])
    df_list.append(result)

    BowLoop.Starting_Coin = result['Profit'] #Updating starting Coin to calculate next step in loop

Data_Points = [Coin_Profits, Iron_Ingots, Dweamer_Ingots]
df = pd.DataFrame(df_list)
print(df)

BowLoop.Generate_Graph([Loop_Limit, Loop_Limit, Loop_Limit], Data_Points, Titles)
