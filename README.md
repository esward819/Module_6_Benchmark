# List - Benchmark: Science Fair

In this benchmark you will create a program to collect and vote on science fair projects.

When you start your program it should prompt the user to enter project details until they are done. Each project should have a title, student name, brief description, and a number of votes for it.

Once the science fair project information is collected. You should allow users to vote on the projects until they enter "done". If no projects were submitted, your program should close without collecting votes or showing the winner.

Once the votes are collected, you should display the winner of the science fair. For simplicity sake in this benchmark, you don't have to handle the case where there is a tie. Any project with the maximum number of votes is acceptable.

Examples: 

```
[project] or [done]> project
Title: Project 1
Student Name: Natalie
Description: I did a lot of science. I learned stuff good.
[project] or [done]> project
Title: Even More Science Than Other Science Things
Student Nume: Abed
Description: Like... a lot more science.
[project] or [done]> done
[vote] or [done]> vote
Which project (title)? Project 1
[vote] or [done]> vote
Which project (title)? Even More Science Than Other Science Things
[vote] or [done]> vote
Which project (title)? Project 1
[vote] or [done]> vote
Which project (title)? Project 1
[vote] or [done]> done
Project 1 is the winner!
```

```
[project] or [done]> done
No projects were provided.
```

### Rubric

- [ ] Collects arbitrarily many science fair project descriptions.
    - Projects have: title, student name, description, and a number of votes.
- [ ] Collects arbitrarily many votes on the provided projects.
- [ ] Displays the winner after voting is completed.
    - For simplicity, your code doesn't have to handle the case of a tie.
- [ ] Displays the winner

### Style Guide

- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.
