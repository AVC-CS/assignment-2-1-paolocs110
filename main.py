def main():

    males = int(input("Enter the number of males: "))
    females = int(input("Enter the numer of females: "))

    total = males+females
    m_perc = f"{males/total:.2%}"
    f_perc = f"{females/total:.2%}"

    print(f"The total number of students: \t{total}")
    print(f"The number of males and females \t {males} \t {females}")
    print(f"The percentage of males and females \t {m_perc} \t {f_perc}")
    return m_perc, f_perc


if __name__ == '__main__':
    main()
