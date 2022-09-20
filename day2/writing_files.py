import sys


def writing_to_text_files():
    with open("my_fancy_file.txt", 'w') as f:
        f.write("1")  # no newline at the end
        f.write("2")  # no newline at the end
        f.write("3")  # no newline at the end
        f.write("4\n")  # now we add a new line
        f.write("5\n")  # again
    with open("my_fancy_file.txt") as f:
        print(f"{f.read() = }")
    lines_of_text = [
        "Knowledge is power.",
        "Power to do evil... or power to do good.",
        "Power itself is not evil.",
        "So knowledge itself is not evil.",
        "― Veronica Roth, Allegiant",
    ]
    with open("power_quote.txt", 'w') as f:
        f.writelines(lines_of_text)
    with open("power_quote.txt") as f:
        print(f.readlines())

def writing_to_text_files2():
    with open("my_fancy_file.txt", 'w') as f:
        f.write("1")  # no newline at the end
        f.write("2")  # no newline at the end
        f.write("3")  # no newline at the end
        f.write("4\n")  # now we add a new line
        f.write("5\n")  # again
    with open("my_fancy_file.txt") as f:
        print(f"{f.read() = }")
    lines_of_text = [
        "Knowledge is power.\n",
        "Power to do evil... or power to do good.\n",
        "Power itself is not evil.\n",
        "So knowledge itself is not evil.\n",
        "― Veronica Roth, Allegiant\n",
    ]
    with open("power_quote.txt", 'w') as f:
        f.writelines(lines_of_text)
    with open("power_quote.txt") as f:
        print(f.readlines())

def insert_random_file():
    import pathlib
    my_path = pathlib.Path("dir1/dir3/dir5/random.txt")
    # my_path.unlink()
    # my_path.parent.rmdir()
    my_path.parent.mkdir()
    with my_path.open('w') as f:
        print("This is a random selection of text abasjdgjasd;jfnaugasdjo", file=f)



def creating_and_modifying_paths():
    import pathlib
    import datetime
    my_path = pathlib.Path("dir7/new_file.txt")  # a non-existent path
    col1 = 80
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # with my_path.open('w') as f: # FileNotFoundError
    #     print(f"{datetime.datetime.now() = }\n", file=f) # another way to write to a file
    my_path.parent.mkdir()  # need to create the parent first
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")
    with my_path.open('w') as f:  # write
        print(f"{datetime.datetime.now() = }\n", file=f)  # another way to write to a file
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # my_path.parent.rmdir() # FileExistsError
    my_path.unlink()
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    my_path.parent.rmdir()
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")


def parsing_text_files():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:  # files are iterators
            print(row.strip())  # remove trailing \n
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            cols = row.strip().split("\t")
            print(cols)

def parsing2_text():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            if row[0] != '#':
                cols = row.strip().split("\t")
                if cols[2] == 'exon':
                    extra_col = float(cols[4]) - float(cols[3])
                    extra_col_str = str(extra_col)
                    cols.append(extra_col_str)
                    print(cols)

def correct_function():
    data = range(10)
    with open("file.txt", "w") as f:
        for d in data:
            f.write(str(d) + "\n")
        print("Success?")

def reading_shuffled():
    with open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f:
        chr_set = set()
        for row in f:
            cols = row.strip().split("\t")
            if cols[0] in chr_set:
                print("This needs to be written to a chr " + cols[0] + " only file!")
            else:
                chr_set.add(cols[0])
                print("Need to make a file to write to for chr " + cols[0])
            #print(chr_set)


def main():
    # writing_to_text_files()
    # creating_and_modifying_paths()
    # parsing_text_files()
    # writing_to_text_files2()
    # insert_random_file()
    # parsing2_text()
    # correct_function()
    reading_shuffled()
    return 0


if __name__ == '__main__':
    sys.exit(main())
