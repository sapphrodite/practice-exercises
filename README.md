# practice-exercises

**Python Exercise 1:** Fibonacci Numbers
<br>
Part A: Implement a function that iteratively calculates the Nth Fibonacci number, given an integer N.
<br>
Part B: Re-Implement the function from part A using recursion. Which version has better performance for large values of N? Why?
<br>

**Python Exercise 2:** FizzBuzz
<br>
Write a function that plays FizzBuzz (https://en.wikipedia.org/wiki/Fizz_buzz) for the numbers from 1 to N.
<br>

**Python Exercise 3:** Recursive Binary Search
<br>
Part A: Randomly generate an array containing 500 elements - make sure it's sorted!
<br>
Part B: Implement recursive binary search, returning -1 if the element is not found. Use this to search the array in part A for a given element.
<br>
Part C: Measure the time taken of binary search as array sizes increase. How does it perform for 2500 elements? 1,250,000?
<br>

**Python Exercise 4:** Basic Markov Chain
<br>
This one is rather difficult, and will definitely require a fair amount of research - ask if you don't understand something!
<br>
<br>
Before the ""AI" "Based"" text generators such as GPT-3, there were Markov chains. I want you to implement one that can generate a paragraph of text - although this is an incredibly ineffectual usage of these models, it's fun and provides good experience. Markov chains are an incredibly broad topic, but for this task we only need to understand a subset of their functionality. The important part of these models is that they are state-based, and only rely on the most recent state to inform what state the system will transition to - in practical situations, this negates the computationally expensive work of taking all the past history into account. For example, consider a model with 3 states - A, B, and C. From A, the model has a 50% chance of staying in A, 25% -> B, 25% -> C. For state B, the probabilities are 0% -> A, 50% -> B, 50% -> C.  When in state C, the probabilities are 60% -> A, 10% -> B, 30% -> C.
<br>
<br>
This can be summarized with the following table:
<br>
"A" : {{"A", 0.5}, {"B", 0.25}, {"C", 0.25}}
<br>
"B" : {{"A", 0.0}, {"B", 0.5}, {"C", 0.5}}
<br>
"C" : {{"A", 0.6}, {"B", 0.3}, {"C", 0.1}}
<br>


Using Python, this table can be implemented as a dictionary associating states with a tuple of probabilities - these probabilities themselves are a tuple containing the next state and the associated probability of transitioning to the state. In the case of this exercise, we can consider the different states of the model to be English words. For example, a predictive keyboard like those on smartphones could be implemented using Markov chains - hopefully no one does this, though. When the user types a word, the model can return the 3 words most likely to occur after the recently entered word. This represents a circumstance in the real world where the probabilities of the model can change as the software runs for longer and is provided with more input data.
<br>
<br>
Part A: Given the sample text file (markovChain/markovTestData.txt) generate a probability dictionary, counting which words are most likely to follow other words. The file markovOutput contains a reference probability dictionary to compare against.
<br>
Part B: Using the probability dictionary, make a function that can generate a paragraph!
<br>
<br>
 
 

**Git Exercise 1:** Forking and Repository Management
<br>
Part A: Make a GitHub account and fork my repository. This makes a copy on your own account, which you can modify
<br>
Part B: Using "git init", create a repository. What is the difference between a local and remote (GitHub) repository? Why not use "git clone" here?
<br>
<br>

**Git Exercise 2:** Authentication, Remote Repo Linkage
<br>
Part A: Using "git remote", connect your forked GitHub repository to your local repository.
<br>
Part B: usig "git pull", bring your local repository up to date with the one you forked.
<br>

**Git Exercise 3:** Commits, Pushes and Merges
<br>
Part A: When you have work to submit, put it in a folder with your name. With "git add" and "git commit", make a commit with your changes
<br>
Part B: Using "git push", push your commit to the remote repository. Read into the syntax - why are the branch and repository name included?
<br>
Part C: Go to my GitHub and send a merge request! Here, your code can be reviewed and you can receive feedback.
<br>
<br>

**Git Exercise 4:** git branch, git stash
<br>
Read up on these commands, and experiment - I don't know how to make an assignment to familiarize you with them, but they're rather important to know.
