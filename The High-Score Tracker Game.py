
isRunning = True



while isRunning:
    Control_input = input("\nDo you want to stop, Enter (Yes or NO): ")
    
    if Control_input.strip().lower() == "yes":
        print("---- Game session ended! -----\n")
        break
    elif Control_input.strip().lower() == "no":
          Game_Score = int(input("\nEnter game score: "))
          if Game_Score > 100:
               print("Wow! That’s a new high score!\n")
          elif Game_Score < 0:
              print("\nEntered wrong score format\n")    
          else:
               print(f"Good try, keep playing! \nYour high score is: {Game_Score} ")    
    else:
         print("\n---- Incorect choice, type yes or no. Try again ! ---\n")

    