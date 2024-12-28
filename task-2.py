import turtle
from typing import Union, Optional

def koch_snowflake(t: turtle.Turtle, length: float, depth: int) -> None:
    if depth == 0:
        t.forward(length)
    else:
        length_third: float = length / 3
        koch_snowflake(t, length_third, depth - 1)
        t.left(60)
        koch_snowflake(t, length_third, depth - 1)
        t.right(120)
        koch_snowflake(t, length_third, depth - 1)
        t.left(60)
        koch_snowflake(t, length_third, depth - 1)

def draw_full_snowflake(depth: int, size: float = 300) -> None:
    window: turtle.Screen = turtle.Screen()
    window.title("Снежинка Коха")
    window.bgcolor("black")

    t: turtle.Turtle = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.penup()

    t.goto(-size/2, size/3)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, size, depth)
        t.right(120)

    t.hideturtle()
    window.exitonclick()

def main() -> None:
    while True:
        try:
            depth: int = int(input("Введите уровень рекурсии (рекомендуется 0-6): "))
            if depth < 0:
                print("Уровень рекурсии должен быть положительным числом")
                continue
            if depth > 6:
                print("Внимание: высокие уровни рекурсии могут занять много времени!")
                response: str = input("Продолжить? (y/n): ")
                if response.lower() != 'y':
                    continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число")

    draw_full_snowflake(depth)

if __name__ == "__main__":
    main()