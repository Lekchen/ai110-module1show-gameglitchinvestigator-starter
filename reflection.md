# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the game, it opened a Streamlit page called “Game Glitch Investigator.” It had a sidebar to choose the difficulty, a message asking the player to guess a number, and a text box to enter guesses. There were also buttons for Submit Guess, New Game, and an option to show hints, along with a debug section that displayed the secret number and other game details.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used CHatGPT and Copilot 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Copilot suggested moving the check_guess function from app.py into a separate file called logic_utils.py. This was correct because it separated the game logic from the user interface code, making the program easier to maintain and test. I verified the suggestion by running the game after the refactor and confirming that it still worked correctly. I also ran pytest to ensure the new test for the check_guess function passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At one point, Copilot suggested a fix that did not correctly adjust the hint messages in the check_guess function. The hint still told the player to go higher when the guess was already too high. I verified this by running the game and testing different guesses. After noticing the incorrect behavior, I manually corrected the logic so that guesses greater than the secret return “Too High – Go LOWER” and guesses lower than the secret return “Too Low – Go HIGHER.”
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
To verify my fixes, I created a pytest test in tests/test_game_logic.py that checks whether the check_guess function returns "Too High" when the guess is greater than the secret number. I ran pytest in the terminal and confirmed that the test passed. After that, I ran the application using streamlit run app.py and tested the game manually by entering guesses above and below the secret number. The hints now correctly guide the player in the right direction, confirming that the bug was successfully fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  ne test I ran checked whether the function correctly identifies when a guess is too high. The test used a guess of 60 against a secret number of 50 and verified that the function returns "Too High". When I ran pytest, the test passed, which showed that the logic in the check_guess function was working correctly.
- Did AI help you design or understand any tests? How?
Yes, AI helped me design the pytest test. Copilot suggested creating a simple test that compares a guess and a secret number to check the outcome of the check_guess function. This helped me understand how to write a basic pytest test and verify that the function behaved correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
One habit I want to reuse is writing small tests to verify important logic in my code. Using pytest helped me confirm that my fix worked and prevented the bug from coming back.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time I work with AI on a coding task, I would review the AI’s suggestions more carefully and test them step by step instead of assuming the code is correct.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can be helpful, but it still needs to be carefully reviewed and tested. AI can assist with ideas and code generation, but developers must verify that the logic works correctly.
