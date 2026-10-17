1. How many tests did you write in Part A, and how many lines of production code? What is the ratio? </br>
<b><u>Answer</u></b> 9 test. I have 40 lines of production code. Ratio is 9:40

2. When was your bar red for the longest time, and what made it last so long? </br>
<b><u>Answer</u></b> Step A8: (200 g + 1 oz) × 2 because they have to work with many method and many class together

3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right? </br>
<b><u>Answer</u></b> Yes, each choice was right.
    - Fake It: Used in Step A1 (hardcoding 600 for multiplication), which was right because it quickly proved our test infrastructure worked.   
    - Triangulated: Used in Step A2 (adding a second test with multiplication by 2), which was right because it forced us to write the actual formula instead of a constant.   
    - Obvious Implementation: Used when writing simple methods like __eq__ or __repr__, which was right because the logic was straightforward and safe.

4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?</br> 
<b><u>Answer</u></b> All in list is done.

5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method? </br>
<b><u>Answer</u></b> if i have to design it first on the paper, i might not wrote this method in Quantity class because i might wrote it on Converter only

6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design? </br>
<b><u>Answer</u></b> for part 0 i feel i look in production more than look on the test, for while i look in the code i will imagination the direction together. Part A i think it like to scope our code and direction of this project, so i think i might use technique from Part A 