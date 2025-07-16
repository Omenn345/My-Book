greeting = input("Greeting:").title()

match greeting:
    case "Hello" | "Hello, Newman":
      print("$0")
    case "hey" | "How You Doing?" | "How's it going?":
        print("$20")
    case "What's happening?" | "What's Up?":
        print("$100")

