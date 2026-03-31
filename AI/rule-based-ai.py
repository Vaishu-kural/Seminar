print("Welcome to CADDAM Software Solutions Training Institute Chatbot")
print("Type 'bye' to exit the chat.\n")

company_name = "CADDAM Software Solutions Training Institute"

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print(f"Bot: Hello! Welcome to {company_name}. How can I help you today?")

    elif user == "company":
        print(f"Bot: {company_name} provides professional technical and software training for students and professionals.")

    elif user == "courses":
        print("Bot: We offer the following courses:")
        print("1. Python Programming")
        print("2. Java Programming")
        print("3. Full Stack Web Development")
        print("4. Full Stack Development using AI")
        print("5. Artificial Intelligence")
        print("6. Data Science")
        print("7. Data Science using AI")
        print("8. Data Analyst")
        print("9. CAD / CATIA Design")
        print("\nType any course name like 'python', 'java' or 'data analyst' to know details.")

    elif user == "python":
        print("Bot: Python Programming")
        print("Duration: 2 Months")
        print("Details: Basics, OOP, Automation, Projects")

    elif user == "java":
        print("Bot: Java Programming")
        print("Duration: 3 Months")
        print("Details: Core Java, OOP, JDBC, Collections, Exception Handling, Mini Projects")

    elif user == "full stack":
        print("Bot: Full Stack Web Development")
        print("Duration: 4 Months")
        print("Details: HTML, CSS, JavaScript, React.js, Node.js, Python, Django, Java, Spring Boot")

    elif user == "full stack using ai":
        print("Bot: Full Stack Development using AI")
        print("Duration: 6 Months")
        print("Details: AI Tools for Web Development, ChatGPT for coding, AI UI Design, AI Code Automation")

    elif user == "artificial intelligence" or user == "ai":
        print("Bot: Artificial Intelligence")
        print("Duration: 3 Months")
        print("Details: Machine Learning, Deep Learning Basics, AI Projects")

    elif user == "data science":
        print("Bot: Data Science")
        print("Duration: 4 Months")
        print("Details: Python for Data Science, Statistics, Pandas, NumPy, Data Visualization")

    elif user == "data science using ai":
        print("Bot: Data Science using AI")
        print("Duration: 5 Months")
        print("Details: AI Data Processing, AutoML Tools, AI Model Training")

    elif user == "data analyst":
        print("Bot: Data Analyst")
        print("Duration: 2 Months")
        print("Details: Advanced Excel, SQL, Python for Analysis, Power BI, Tableau")

    elif user == "cad" or user == "catia" or user == "cad / catia design":
        print("Bot: CAD / CATIA Design")
        print("Duration: 3 Months")
        print("Details: 3D Modeling, Surface Design, Sheet Metal Design")

    elif user == "course details":
        print("Bot: Type a specific course name to get its details.")
        print("Example: python, java, full stack, data analyst, ai")

    elif user == "ietp":
        print("Bot: IETP stands for Industrial Engineering Training Program.")
        print("It includes practical industry-level training, live projects, and certification.")

    elif user == "fees":
        print("Bot: Fees vary depending on the course. Please contact our office for detailed fee structure.")

    elif user == "contact":
        print("Bot: Contact Details:")
        print("CADDAM Software Solutions Training Institute")
        print("Address: Chennai, Tamil Nadu, India")
        print("Phone: +91-9876543210")
        print("Email: info@caddam.com")

    elif user == "bye":
        print("Bot: Thank you for contacting CADDAM Software Solutions Training Institute. Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")
        print("Type 'courses' to see all courses or enter a course name like 'python' or 'java'.")