import google.generativeai as genai
# import os

class NLPModel:
    def get_model(self):
        GOOGLE_API_KEY = "AIzaSyBfpyXurETB5BtCysAezpX0LRKWJhCFK-o"
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-pro")
            return model
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
class NLPapp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()
        
    def first_menu(self):
        while True:
            first_input = input(""" 
            Hi! How would you like to proceed?
            1. Not a member? Register
            2. Already a member? Login
            3. Exit
            """)
            if first_input in ["1", "2", "3"]:
                break
            else:
                print("Please enter a valid option.")
        if first_input == "1":
            self.__register()
        elif first_input == "2":
            self.__login()
        else:
            exit()
            
    def second_menu(self):
        while True:
            second_input = input("""
            Hi! How would you like to proceed?
            1. Sentiment Analysis
            2. Language Translation
            3. Language Detection
            4. Code Generation
            5. Text Summarization             
            """)
            if second_input in ["1", "2", "3","4","5"]:
                break
            else:
                print("loging out.....")
                exit()
            
        if second_input == "1":
            self.__sentiment_analysis()
        elif second_input == "2":
            self.__language_translate()
        elif second_input == "3":
            self.__language_detection()
        elif second_input=="4":
            self.code_generation()
        elif second_input=="5":
            self.text_sumeraise()
        else:
            exit()
            
    def __register(self):
        name = input("Enter your name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        
        if email in self.__database:
            print("Email already exists.")
        else:
            self.__database[email] = [name, password]
            print("Registration successful. Now you can login!")
            self.first_menu()
            
    def __login(self):
        email = input("Enter your email: ")
        password = input("Enter your Password: ")
        
        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login Successful!")
                self.second_menu()
            else:
                print("Incorrect password!")
                self.first_menu()
        else:
            print("Email not found. Please register first.")
            self.first_menu() 
            
    def __sentiment_analysis(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        if model:
            response = model.generate_content(f"Give me the sentiment of the sentence: {user_text}")
            results = response.text
            print(results)
        self.second_menu()
            
    def __language_translate(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        if model:
            response = model.generate_content(f"Give me the Bangla translation of the sentence: {user_text}")
            results = response.text
            print(results)
        self.second_menu()
        
    def __language_detection(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        if model:
            response = model.generate_content(f"Detect the language of the sentence: {user_text}")
            results = response.text
            print(results)
        self.second_menu()
        
    def code_generation(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        if model:
            response = model.generate_content(f"Write a Python function about: {user_text}")
            results = response.text
            print(results)
        self.second_menu()
    
    def text_sumeraise(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        if model:
            response = model.generate_content(f"Summarize this text: {user_text}")
            results = response.text
            print(results)
        self.second_menu()  

    
        
if __name__ == "__main__":
    # os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
    nlp = NLPapp()
