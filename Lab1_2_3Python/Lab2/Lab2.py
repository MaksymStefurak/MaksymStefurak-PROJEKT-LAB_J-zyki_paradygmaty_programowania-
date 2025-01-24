#Zad1
import re
from collections import Counter


stop_words= {"i", "a", "the", "and","is", "it", "in", "on","for","of", "to","at","this"}

def analizowanieTekstu(text):




    slowa=re.findall(r'\\b\\w+\\b',text)

    zdania=list(filter(bool, re.split(r'[.!?]', text)))
    akap=list(filter(bool, text.split("\\n")))

    word_count = len(slowa)
    sentence_count = len(zdania)
    paragraph_count = len(akap)




    transform_text= " ".join(
        map(lambda word: word[::-1]

        if word.lower().startswith("a")

        else word, slowa)
    )

    return {
        "word_count": word_count,

        "sentence_count": sentence_count,

        "paragraph_count": paragraph_count,

        "transform_text": transform_text
    }


sample_text = (
   "lorem ipsum dolor "
   ""
   "igfhewfhwehfjew fjjhwejfhewjf iefkmj djawn  aaaa a a erthemfwemndkaldm, aghdfhdb aghfejd good agood "
   " hello dark jdfhgjf hello hghsfhs hello fjshej hello fhjsfghsf hello  alala a alalal ala lala allalal alala lala laa ala ala ala alalalalala "
   ""
   "     alalalalalal alalalaal    alalala la "
   " lslslslsl ls lsl sl sl ls ls ls ls ls "
   )


result=analizowanieTekstu (sample_text)


print("Liczba słów:", result["word_count"])

print("Liczba zdań:", result["sentence_count"])

print("Liczba akapitów:", result["paragraph_count"])

print("Tekst po transformacji:", result["transform_text"])

#Zad2
import numpy as np

def validate_matrices_for_addition(mat1, mat2):
    return mat1.shape == mat2.shape

def validate_matrices_for_multiplication(mat1, mat2):
    return mat1.shape[1] == mat2.shape[0]

def perform_operation(operation, matrices):
    try:
        if operation == "add":
            if not validate_matrices_for_addition(matrices[0], matrices[1]):
                return "Error: Matrices must have the same dimensions for addition."
            return matrices[0] + matrices[1]

        elif operation == "multiply":
            if not validate_matrices_for_multiplication(matrices[0], matrices[1]):
                return "Error: Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication."
            return matrices[0] @ matrices[1]

        elif operation == "transpose":
            return [np.transpose(mat) for mat in matrices]

        else:
            return "Error: Unsupported operation. Supported operations are add, multiply, and transpose."

    except Exception as e:
        return f"Error while performing operation: {str(e)}"

def parse_matrix(matrix_str):
    try:
        return np.array(eval(matrix_str))
    except Exception as e:
        raise ValueError(f"Invalid matrix format: {matrix_str}. Error: {str(e)}")

def main():
    print("Matrix Operations System")
    print("Supported operations: add, multiply, transpose")
    
    while True:
        print("\n--- New Operation ---")
        operation = input("Enter operation (add/multiply/transpose or 'exit' to quit): ").strip().lower()

        if operation == "exit":
            print("Exiting the system. Goodbye!")
            break

        try:
            if operation in ["add", "multiply"]:
                mat1_str = input("Enter the first matrix (e.g., [[1, 2], [3, 4]]): ").strip()
                mat2_str = input("Enter the second matrix (e.g., [[5, 6], [7, 8]]): ").strip()

                mat1 = parse_matrix(mat1_str)
                mat2 = parse_matrix(mat2_str)

                result = perform_operation(operation, [mat1, mat2])

            elif operation == "transpose":
                mat_str = input("Enter the matrix to transpose (e.g., [[1, 2], [3, 4]]): ").strip()
                mat = parse_matrix(mat_str)

                result = perform_operation(operation, [mat])

            else:
                print("Unsupported operation. Try again.")
                continue

            print("Result:")
            print(result)

        except ValueError as ve:
            print(f"Input Error: {str(ve)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()

#Zad3
def analiza_danych(data):


    liczby = list(filter(lambda x: isinstance(x, (int, float)), data))

    licz_maks = max(liczby) if liczby else None




    napis = list(filter(lambda x: isinstance(x, str), data))
    dluzszy_napis = max(napis, key=len) if napis else None

    return {

        "maksymalna_liczba": licz_maks,
        "najdłuższy_napis": dluzszy_napis
    }



data = [
    57, "apple", 127.89, "banana", "grape", "peach", 100, "tree"
]

result = analiza_danych(data)

print("Największa liczba:", result["maksymalna_liczba"])
print("Najdłuższy napis:", result["najdłuższy_napis"])

#Zad4
from functools import reduce
import numpy as np


def operacje_macierzowe(macierz1, macierz2, operacja):
    if operacja=='suma':

        return np.add(macierz1, macierz2)

    elif operacja== 'iloczyn':
        return np.dot(macierz1, macierz2)



def poloczenie(macierze, operacja):
    return reduce(lambda m1, m2: operacje_macierzowe(m1, m2, operacja), macierze)


macierz1=np.array([[22, 34], [3, 4]])
macierz2=np.array([[5, 53], [12, 21]])
macierz3=np.array([[7, 11], [8, 25]])


macierze= [macierz1, macierz2, macierz3]


operacja =input("Jaką chcęsz operację, wybierz suma / iloczyn: ").strip().lower()


if operacja=='suma' or operacja =='iloczyn':

    wynik = poloczenie(macierze, operacja)

    print(f"Wynik operacji '{operacja}' na macierzach:\n{wynik}")
else:
    print("Błąd!")

