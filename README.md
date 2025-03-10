# CIS 12, Chapter 7 Exercises

- <h2><b>Exercise 7.9.2</b></h2>

When comparing my version with the instructors, I'd say the instructor's version is better because it's more concise 
and takes into consideration that the word and forbidden letters might be upper case (or mixed case) and converts them 
to lowercase to allow for direct comparison. I also didn't realize at the time I was working on this exercise that the 
in operator can iterate through a string, so I needlessly put the forbidden letters into a list for comparison. So, to 
improve my code, I could get rid of the "passed" variable and just leave out the list altogether.

- <h2><b>Exercise 7.9.3</b></h2>

The two versions pretty much look the same, though I didn't take in consideration that I'd need to convert any 
upper/mixed case characters to lower case to allow for comparison, so I'd include that to improve my code.

- <h2><b>Exercise 7.9.4</b></h2>

The two versions are different, but I think both accomplish the same goal (outside of me forgetting to convert to lower 
case.) I'm not sure if either code needs to be improved or not and, if so, I wouldn't know in what way. My doctests all 
passed, so I feel like I got the idea, but I have no idea if the instructor's version is different because it covers all 
possible use cases or if it's just another way to do the same thing. 

- <h2><b>Exercise 7.9.5</b></h2>

This was a tough exercise! I really struggled with this at first and I even asked ChatGPT for help but the AI just kept
looping through the wrong suggestions that didn't help me at all, so I nearly gave up! Eventually I decided to move on 
to the other exercises and that's when I realized that I could use functions from other exercises to help me out - 
specifically "uses_all" and "uses_only". When comparing my code to the instructor's, I'd have to say, without question, 
the instructor's is much better. It's cleaner, much more concise, and it avoids reusing code through the use of imports
(which I absolutely forgot about in my scramble to figure out how to make the overall program <i>work</i>.) To improve 
my code, I'd get rid of the unnecessary function definitions and use imports instead. Otherwise, the two look pretty 
much the same with minor variations.

- <h2><b>Exercise 7.9.6</b></h2>

I think the two versions are more or less the same, though the return statements in the instructor's version are more 
concise so that makes the instructor's version the better one, for me. I still have trouble understanding what's being 
returned when everything is condensed into one line, so the only way I could improve my own code is to get better at 
understanding what the code is doing, so I can be more confident that the code will produce the results I want if I 
take the shortcuts built into Python.

- <h2><b>Exercise 7.9.8</b></h2>

ChatGPT said that this could be done and pretty much gave code that matched what the textbook got, but I don't 
understand the resulting code that was provided. To my understanding, uses_any only determines if any of the characters
in the word match the second str, but this doesn't determine if <i>all</i> the characters in the first string match 
<i>all</i> the characters in the second. So how does the code the textbook (and chatgpt) offer determine that?

