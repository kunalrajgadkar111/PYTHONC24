print("Hello, World!")

match_results = "win"

match match_results:
    case "win":
        print("You won!")
    case "lose":
        print("You lost!")
    case "draw":
        print("It's a draw!")
    case _:
        print("Invalid match result!")
