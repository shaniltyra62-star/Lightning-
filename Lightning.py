# LIGHTNING INTERPRETER - MOBILE VERSION
import re
import random

print("🌩️ LIGHTNING INTERPRETER 🌩️")
print("Ready for Lightning code!")

def run_lightning():
    variables = {}
    output = []
    
    # Get code from user
    print("\n📝 Enter your Lightning code (type 'RUN' on new line to execute):")
    code_lines = []
    while True:
        line = input()
        if line.strip() == 'RUN':
            break
        code_lines.append(line)
    
    code = '\n'.join(code_lines)
    
    # Simple interpreter
    lines = [l.strip() for l in code.split('\n') if l.strip()]
    
    for line in lines:
        try:
            # tro={variable}
            if 'tro={' in line:
                var = line.split('tro={')[1].split('}')[0]
                variables[var] = None
                output.append(f"Declared variable: {var}")
            
            # print(=message=)
            elif 'print (=' in line:
                msg = line.split('print (=')[1].split('=)')[0]
                output.append(msg.replace('-', ' '))
            
            # >> input
            elif line.startswith('>>'):
                var = line[2:].strip()
                if var in variables:
                    user_input = input(f"Enter value for {var}: ")
                    variables[var] = user_input
                    output.append(f"{var} = {user_input}")
            
            # if# condition
            elif 'if#' in line:
                parts = line.replace('if#', '').replace(':', '').split('==')
                if len(parts) == 2:
                    var, value = parts[0].strip(), parts[1].strip()
                    if var in variables and str(variables[var]) == value:
                        output.append(f"Condition TRUE: {var} == {value}")
                    else:
                        output.append(f"Condition FALSE: {var} == {value}")
            
            # return!=[value]
            elif 'return!=' in line:
                val = line.split('return!=')[1].split(']')[0].replace('[', '')
                output.append(f"Return: {val}")
                
        except Exception as e:
            output.append(f"Error: {e}")
    
    # Show results
    print("\n⚡ EXECUTION RESULTS:")
    for line in output:
        print(f"→ {line}")

# Main menu
while True:
    print("\n" + "="*40)
    print("1. Run Lightning code")
    print("2. Example: Hello World") 
    print("3. Example: Mood Checker")
    print("4. Exit")
    
    choice = input("Choose: ")
    
    if choice == '1':
        run_lightning()
    elif choice == '2':
        # Auto-run hello world
        code = """
import# Light
({
    tro={message}
    print (=hello-world=)
    print (=welcome-to-lightning=)
    return!=[success]
})
"""
        print("Running Hello World example...")
        # Simulate running the code
        print("→ hello world")
        print("→ welcome to lightning") 
        print("→ Return: success")
    elif choice == '3':
        # Auto-run mood checker
        print("Running Mood Checker...")
        mood = input("How are you feeling? (happy/sad/tired): ")
        if mood == 'happy':
            print("→ Great! 😊")
            print("→ Return: smile")
        elif mood == 'sad':
            print("→ Sorry 😔")
            print("→ Return: hug")
        else:
            print("→ I understand 😐")
            print("→ Return: support")
    elif choice == '4':
        break