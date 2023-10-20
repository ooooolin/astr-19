import numpy as np

def main():
    print("x   |   sin(x) ")
    print("---------------------")

    x_values = np.linspace(0, 2 * np.pi, 1000)
    sin_values = np.sin(x_values)
    


    for i in range(len(x_values)):
        x = x_values[i]
        sin_value = sin_values[i]
        

        print(f"{x:.4f}\t| {sin_value:.4f}")

if __name__ == "__main__":
    main()