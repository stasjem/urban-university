import time
from multiprocessing import Pool

filenames = [f'file {number}.txt' for number in range(1, 5)]

def read_info(name):
    all_data = []
    if isinstance(name,list):
        for names in name:
            with open(names, "r") as file:
                for i in file.readlines():
                    if i == "":
                        print("Конец")
                        break
                    else:
                        all_data.append(i)

    elif isinstance(name,str):
        with open(name, "r") as file:
            for i in file.readlines():
                if i == "":
                    print("Конец")
                    break
                else:
                    all_data.append(i)


if __name__ == '__main__':
    time1 = time.time()
    read_info(filenames)
    time2 = time.time()
    print(time2-time1,"(линейный)")

    time1 = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info,filenames)
    time2 = time.time()
    print(time2-time1,"(мультипроцессный)")

