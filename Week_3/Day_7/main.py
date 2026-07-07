from assistant import StudyAssistant

assistant = StudyAssistant()

while(True):
    print("\n--------Study Assistent---------")
    print("1. Ask Question")
    print("2. View History")
    print("3. Export History")
    print("4. Exit")
    print("--------------------------------")

    try:
        n = int(input("Choose: "))
    except ValueError:
        print("Please Enter  a number.")
        continue
    
    if n == 1:
        question = assistant.ask_question().strip().lower()
        answer = assistant.get_ai_response(question)
        print(answer)
        assistant.save_history(question, answer)
    elif n == 2:
        print('-----Conversation History-----')
        conversation = assistant.view_history()
        if not conversation:
            print("No conversation done yet.")
        else:
            for i, conv in enumerate(conversation, start=1):
                print(f"\nConversation {i}")
                print(f"Question: {conv['question']}")
                print(f"Answer: {conv['answer']}")  
    elif n == 3:
        assistant.export_history()
    elif n == 4:
        print("Bye!\n")
        break
    else:
        print("Invalid number choice.\n")