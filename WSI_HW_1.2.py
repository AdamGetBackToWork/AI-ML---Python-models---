import time
import random

# function
function = "(x+2*y-7)^2 + (2*x+y-5)^2"
function_derivX = "10*x+8*y-34"
function_derivY = "8*x+10*y-38"
function_hesjan = 32  # "[10, 8], [8, 10]"
function_inv_hesjan = 32/7  # "[3/8 -1/4], [-1/4 1/4]"
# function


def DX(x, y):
    fun = eval(function_derivX)
    return fun


def DY(x, y):
    fun = eval(function_derivY)
    return fun


def Newton(inits, fun):
    x, y = inits

    # var_Newton
    iters = 6000  # the program starts to give correct answers around 3k iterations
    B = 10e-5
    # var_Newton

    while (iters > 0):
        dX = function_inv_hesjan * DX(x, y)
        dY = function_inv_hesjan * DY(x, y)
        iters -= 1
        x = x - B * dX
        y = y - B * dY

    return round(x, 2), round(y, 2)


def main():
    # x = int(input("Give x: "))
    # y = int(input("Give y: "))
    with open("Data.txt", "a") as f:
        f.write("Newton Method\n")
        for i in range(25):
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
            print("Initial x =", x, " y =", y)
            # f.write(f"Initial x = {x} y = {y} ")
            f.write(f"{x} {y} ")

            time_start = time.time()
            x, y = Newton((x, y), function)
            print(f"x = {x} y = {y}")
            print(f"Time of function: {round(time.time()-time_start, 2)}s")
            # f.write(f"Solution: x = {x} y = {y} ")
            # f.write(f"Soluton time = {round(time.time()-time_start, 2)}s\n")
            f.write(f"{x} {y} {round(time.time()-time_start, 2)}s\n")
        f.close()


main()
