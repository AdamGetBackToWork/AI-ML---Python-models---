import time
import random

# function
function = "(x+2*y-7)^2 + (2*x+y-5)^2"
function_derivX = "10*x+8*y-34"
function_derivY = "8*x+10*y-38"
# function


def DX(x, y):
    fun = eval(function_derivX)
    return fun


def DY(x, y):
    fun = eval(function_derivY)
    return fun


def gradient(inits, function_grad):
    x, y = inits

    # var_gradient
    iters = 20000  # the program starts to give correct answers around 10k iterations
    B = 10e-5  # epsilon adjusted to the function and number of iterations
    # var_gradient

    while (iters > 0):
        iters -= 1
        x = x - B * DX(x, y)
        y = y - B * DY(x, y)

    return round(x, 2), round(y, 2)


def main():
    # x = int(input("Give x: "))
    # y = int(input("Give y: "))
    with open("Data.txt", "a") as f:
        # f.write("Gradient Descent Method\n")
        for i in range(25):
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
            print("Initial x =", x, " y =", y)
            # f.write(f"Initial x = {x} y = {y} ")
            f.write(f"{x} {y} ")

            time_start = time.time()
            x, y = gradient((x, y), function)
            print(f"x = {x} y = {y}")
            print(f"Time of function: {round(time.time()-time_start, 2)}s")
            # f.write(f"Solution: x = {x} y = {y} ")
            # f.write(f"Soluton time = {round(time.time()-time_start, 2)}s\n")
            f.write(f"{x} {y} {round(time.time()-time_start, 2)}s\n")
        f.close()


main()
