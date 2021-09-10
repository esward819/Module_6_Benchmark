from typing import List
from dataclasses import dataclass

@dataclass
class Science:
  title: str
  name: str
  description: str
  votes: int


projects: List[Science] = [
]
votes: List[int] = [
]


def action_input() -> str:
  action = input("[project] or [done]>")
  if valid_action(action):
    pass
  else:
    print("Invalid Action")
  return action


def valid_action(action: str) -> bool:
  return action == "project" or action == "done"

def add_project(projects: List[Science]) -> None:
  title = input("Title: ")
  name = input("Student Name: ")
  desc = input("Description: ")
  projects.append(Science(title, name, desc, 0))


def voting(projects: List[Science]) -> None:
    vote = input("Which project (title)? ")
    for project in projects:
      if vote == project.title:
        project.votes += 1
    print("Please vote for a valid project.")

def vote_counter(projects: List[Science]) -> None:
  for project in projects:
    votes.append(project.votes)

def winner(project: List[Science], votes: List[int]) -> None:
  vote_counter(projects)
  for project in projects:
      if project.votes == max(votes):
        print(f"{project.title} is the winner!")

def main() -> None:
  while True:
    action = action_input()
    if action == "project":
      add_project(projects)
    elif action == "done" and len(projects) == 0:
      print("No projects were provided.")
      quit()
    elif action == "done":
      break
  while True:
    action = input("[vote] or [done]")
    if action == "vote":
      voting(projects)
    elif action == "done":
      winner(projects, votes)
      break
if __name__ == '__main__':
  main()
