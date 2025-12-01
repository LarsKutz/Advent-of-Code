import os 
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



def solution(data):
    curr_state = 50
    zeros = 0
    for instr in data:
        if "L" in instr:
            curr_state = (curr_state - int(instr[1:])) % 100  
        else:
            curr_state = (curr_state + int(instr[1:])) % 100
        if curr_state == 0:
            zeros += 1

    return zeros


def solution2(data):
    pass


if __name__ == "__main__":
    file_path = os.getenv("INPUT", "../input.txt")
    with open(file_path, "r") as f:
        data = f.read().strip().split("\n")
        print(solution(data))