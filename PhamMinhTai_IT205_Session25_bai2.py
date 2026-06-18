class NetflixAccount:
    """
    Netflix Account Class
    Demonstrates:
    - Encapsulation
    - Property
    - Static Method
    - Class Method
    """

    # Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []


    @property
    def password(self):
        """
        Return hidden password instead of real password.
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Validate password length.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password


    @property
    def plan(self):
        """
        Read-only plan property.
        """
        return self.__plan


    @staticmethod
    def validate_email(email):
        """
        Check email format.
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        Update global profile limit.
        """
        cls.max_profiles = new_limit


    def add_profile(self, profile_name):

        if len(self.profiles) >= NetflixAccount.max_profiles:
            print(
                "Đã đạt giới hạn số lượng Profile trên tài khoản này"
            )
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công!")

    def upgrade_plan(self, new_plan):

        valid_plans = [
            "Basic",
            "Standard",
            "Premium"
        ]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ")
            return

        self.__plan = new_plan
        print(f"Đã nâng cấp lên gói {new_plan}")

    def display_info(self):

        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Platform: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Plan: {self.__plan}")

        if self.profiles:
            print("Profiles:")
            for index, profile in enumerate(
                self.profiles,
                start=1
            ):
                print(f"{index}. {profile}")
        else:
            print("Profiles: []")

        print(
            f"Max Profiles Allowed: {NetflixAccount.max_profiles}"
        )


current_account = None

while True:

    print("\n===== NETFLIX ACCOUNT MANAGER =====")
    print("1. Đăng ký tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Thêm người xem")
    print("4. Nâng cấp gói cước")
    print("5. Cập nhật chính sách Netflix")
    print("6. Thoát chương trình")
    print("===================================")

    choice = input("Chọn chức năng (1-6): ")


    if choice == "1":

        print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")

        while True:

            email = input("Nhập Email: ")

            if NetflixAccount.validate_email(email):
                break

            print(
                "Email không hợp lệ, vui lòng chứa ký tự '@' và '.'"
            )

        account = NetflixAccount(email)

        while True:

            try:
                password = input("Nhập mật khẩu: ")

                account.password = password
                break

            except ValueError as e:
                print(e)

        current_account = account

        print("Đăng ký tài khoản thành công!")


    elif choice == "2":

        if current_account is None:
            print(
                "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
            )
        else:
            current_account.display_info()


    elif choice == "3":

        if current_account is None:
            print(
                "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
            )
            continue

        print("\n--- THÊM PROFILE ---")

        profile_name = input(
            "Nhập tên Profile mới: "
        )

        current_account.add_profile(profile_name)


    elif choice == "4":

        if current_account is None:
            print(
                "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
            )
            continue

        print("\n--- NÂNG CẤP GÓI CƯỚC ---")
        print("1. Basic")
        print("2. Standard")
        print("3. Premium")

        plan_choice = input(
            "Chọn gói cước: "
        )

        plan_map = {
            "1": "Basic",
            "2": "Standard",
            "3": "Premium"
        }

        if plan_choice in plan_map:
            current_account.upgrade_plan(
                plan_map[plan_choice]
            )
        else:
            print("Lựa chọn không hợp lệ")


    elif choice == "5":

        print(
            "\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---"
        )

        print(
            f"Giới hạn hiện tại: {NetflixAccount.max_profiles}"
        )

        try:

            new_limit = int(
                input(
                    "Nhập số lượng Profile tối đa mới: "
                )
            )

            if new_limit <= 0:
                print(
                    "Giới hạn Profile phải lớn hơn 0"
                )
            else:

                NetflixAccount.update_max_profiles(
                    new_limit
                )

                print(
                    f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}"
                )

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ")


    elif choice == "6":

        print(
            "Cảm ơn bạn đã sử dụng Netflix Account Manager!"
        )

        break

    else:
        print("Lựa chọn không hợp lệ")