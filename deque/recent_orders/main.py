from collections import deque

def main():
    foods = deque(["pizza","chicken salad","spinach dip","waffles","ham and egg tacos","buffalo wings"],5)
    print(foods)
    return foods

if __name__ == "__main__":
    main()