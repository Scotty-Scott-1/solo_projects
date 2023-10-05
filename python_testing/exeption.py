#!/usr/bin/python3

def main():


    try:
        myFile = open("mydatfa.txt", encoding="utf-8")

    except FileNotFoundError as ex:
        print("That file was not found")
        print(ex.args)

    else:
        print("File:", myFile.read())
        myFile.close()

    finally:
        print("Finished working with file :)")

    return

if __name__ == "__main__":
    main()
