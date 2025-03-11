from declare import *
from menu import *

def print_infor():
    """Hiển thị thông tin gói tin."""
    try:
        print("\n---------- Thông tin gói tin -------------")
        PKT_Default_Receive.show()
    except Exception as ex:
        print(f"Lỗi: {ex}")

def send_packet():
    """Gửi gói tin qua giao diện Ethernet."""
    try:
        print("\nGửi gói tin...")
        sendp(PKT_Default_Receive, iface=IFACE, verbose=True)
        print("✅ Gói tin đã được gửi thành công!")
    except Exception as ex:
        print(f"Lỗi khi gửi gói tin: {ex}")

def main():
    while True:
        choice = print_menu()
        if choice == 1:
            print_infor()
        elif choice == 2:
            send_packet()
        elif choice == 0:
            print("Thoát chương trình. Hẹn gặp lại! 👋")
            break

if __name__ == '__main__':
    main()