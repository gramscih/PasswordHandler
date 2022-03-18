import optparse

import abs_factory
import password_generator as pwd_gen

mgr_ins = abs_factory.get_manager_instance()

def generate_new(app):
    new_pwd = pwd_gen.generate_psw()
    mgr_ins.write({"app_name": app, "app_pwd": new_pwd})
    return new_pwd

def update_pwd(app):
    new_pwd = pwd_gen.generate_psw()
    mgr_ins.update(app, new_pwd)
    return new_pwd

def existing_options(app_data):
    run = True
    print("[+] You already have a password for [{}]. What would you like to do?...".format(app_data[0]))
    while run:
        print("1. Return existing password")
        print("2. Generate a new one & update")
        print("3. Exit")
        print("------------------------------------------------------------------------------------")
        opt = int(input("I am hearing: "))
        if opt == 1:
            print("[+] Password for the application {} is: {}".format(app_data[0], app_data[1]))
            print("------------------------------------------------------------------------------------")
            run = False
        elif opt == 2:
            new_pwd = update_pwd(app_data[0])
            print("[+] A new password was generated for {}, here it is: {}".format(app_data[0], new_pwd))
            run = False
        elif opt == 3:
            run = False 


def validate_app_name(app):
    app_pwd = mgr_ins.read(app)
    if not app_pwd:
        new_pwd = generate_new(app)
        print("[+] New password was generated for {}, here it is: {}".format(app, new_pwd))
    else:
        existing_options(app_pwd)

def main():
    parser = optparse.OptionParser()

    parser.add_option("-a", "--application", dest="app", help="Application name for what you need the password or generate a new one")

    (options, arguments) = parser.parse_args()

    if not options.app:
        app = input("[+] For with app you need the password dude: ")
        validate_app_name(app)
    else:
        validate_app_name(options.app)


if __name__ == "__main__":
    main()