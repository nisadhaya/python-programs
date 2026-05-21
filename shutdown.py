import os
seconds = int(input("Enter time in seconds to shutdown: "))
os.system(f"shutdown /s /t {seconds}") 
print(f"System will shutdown in {seconds} seconds.")
