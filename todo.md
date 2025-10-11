1_analyzer_ai/api_example.py rework mods
## Fix your Python chatbot from earlier

You got it 90% working. The bugs are simple. Let's finish it.

**Step 1 (5 minutes): Fix the quit bug**
```python
# Replace sys.stdin.readline() with input()
inn = input().strip()  # This removes the \n automatically
```

**Step 2 (10 minutes): Handle empty messages**
```python
if inn and inn != 'q':  # Check it's not empty
    print(send_to_cli(inn))
```

**Step 3 (15 minutes): Add conversation history**
```python
messages = []  # Store the conversation
# In your send_to_cli function, append both user and assistant messages
messages.append({"role": "user", "content": msg_to_cli})
# Send entire messages list to Claude API, not just the last message
```
remark on the history searach onthe appedn if making a dict or list or what

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
**Step 4 (20 minutes): Add error handling**
```python
try:
    response = send_to_cli(inn)
    print(response)
except anthropic.BadRequestError as e:
    print("Error: Message too short or invalid")
except Exception as e:
    print(f"Something went wrong: {e}")
```

**Step 5 (10 minutes): Test it properly**
- Run it
- Have a 3-message conversation
- Type 'q' to quit
- Verify it actually quits

**If you finish early:**
Add this one feature:
```python
# Save conversation to file when quitting
with open(f"chat_{datetime.now():%Y%m%d_%H%M%S}.txt", "w") as f:
    f.write("\n".join(all_messages))
```

**DO NOT:**
- Research how Claude's API works internally
- Read about async IO
- Optimize the code
- Add 10 features

**Just make it work. Ship one working thing in one hour.**

Timer starts now. Show me the working code in 60 minutes.