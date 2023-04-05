# Python program to demonstrate 
# main() function 
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# print("Hello")

# # Defining main function
# def main():
#     print("hey there")


# # Using the special variable 
# # __name__
# if __name__=="__main__":
#     main()
