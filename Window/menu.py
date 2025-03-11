def print_menu():
    while True:
        print("\n" + "-" * 22 + " MENU " + "-" * 22)
        print("\t1. [Info]   Xem thông tin gói tin")
        print("\t2. [Send]   Gửi gói tin")
        print("\t0. [Exit]   Thoát chương trình")
        print("-" * 50)
        
        try:
            choice = int(input("Nhập lựa chọn [0-2]: "))
            if 0 <= choice <= 2:
                return choice
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


if __name__=='__main__':
    print_menu()