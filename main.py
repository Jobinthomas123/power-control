from itachip2ir import VirtualDevice, iTach
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

# LG_power = "sendir,1:1,1,37878,1,1,341,171,22,21,22,21,22,63,22,21,22,21,22,21,22,21,22,21,22,63,22,63,22,21,22,63,22,63,22,63,22,63,22,63,22,21,22,21,22,21,22,63,22,21,22,21,22,21,22,21,22,63,22,63,22,63,22,21,22,63,22,63,22,63,22,63,22,1523,341,86,22,3649,341,86,22,3648,341,86,22,3700"
# Roku_power = 'sendir,1:1,1,37878,1,1,342,170,22,21,22,63,22,21,22,63,22,21,22,63,22,63,22,63,22,63,22,63,22,63,22,21,22,21,22,21,22,63,22,63,22,63,22,63,22,63,22,21,22,63,22,21,22,21,22,21,22,21,22,21,22,21,22,63,22,21,22,63,22,63,22,63,22,1446,342,170,22,21,22,63,22,21,22,63,22,21,22,63,22,63,22,63,22,63,22,63,22,63,22,21,22,21,22,21,22,63,22,63,22,63,22,63,22,63,22,21,22,63,22,21,22,21,22,63,22,21,22,21,22,21,22,63,22,21,22,63,22,63,22,21,22,1446,342,170,22,21,22,63,22,21,22,63,22,21,22,63,22,63,22,63,22,63,22,63,22,63,22,21,22,21,22,21,22,63,22,63,22,63,22,63,22,63,22,21,22,63,22,21,22,21,22,63,22,21,22,21,22,21,22,63,22,21,22,63,22,63,22,21,22,1446,342,170,22,21,22,63,22,21,22,63,22,21,22,63,22,63,22,63,22,63,22,63,22,63,22,21,22,21,22,21,22,63,22,63,22,63,22,63,22,63,22,21,22,63,22,21,22,21,22,63,22,21,22,21,22,21,22,63,22,21,22,63,22,63,22,21,22,3700'
# Toshiba_power = 'sendir,1:3,1,38109,1,1,343,171,22,21,21,64,22,21,22,21,21,21,22,21,22,21,22,21,21,64,22,21,21,64,22,64,21,64,22,63,22,64,21,22,21,21,22,64,21,64,22,21,22,21,21,21,22,64,21,21,22,64,22,21,21,21,22,64,21,64,22,64,21,21,22,64,21,3800'
# insignia_power = 'sendir,1:3,1,38226,1,1,342,172,21,22,21,64,21,65,21,22,21,22,21,22,21,22,21,64,21,65,21,22,21,65,21,22,21,22,21,22,21,22,21,22,21,64,21,64,21,64,21,65,21,22,21,22,21,22,21,22,21,22,21,22,21,22,21,22,21,64,21,64,21,64,21,64,21,1663,342,86,21,3673,342,86,21,3673,342,86,21,3800'


# Turn all on sequence
def toggle_all_on():
    left_wall_toggle_power()
    time.sleep(2)
    back_fill_toggle_power()
    time.sleep(2)
    signage_pa_side_toggle_power()
    time.sleep(2)
    signage_qr_side_toggle_power()
    time.sleep(2)
    pa_quiet_room_toggle_power()
    time.sleep(2)
    usher_quiet_room_toggle_power()
    time.sleep(2)
    nursery_toggle_power()
    time.sleep(2)
    signage_middle_hall_toggle_power()
    time.sleep(2)
    turn_on_main_projector()


# Turn all off sequence
def toggle_all_off():
    left_wall_toggle_power()
    time.sleep(2)
    back_fill_toggle_power()
    time.sleep(2)
    signage_pa_side_toggle_power()
    time.sleep(2)
    signage_qr_side_toggle_power()
    time.sleep(2)
    pa_quiet_room_toggle_power()
    time.sleep(2)
    usher_quiet_room_toggle_power()
    time.sleep(2)
    nursery_toggle_power()
    time.sleep(2)
    signage_middle_hall_toggle_power()
    time.sleep(2)
    turn_off_main_projector()


# Turn all signage on/off sequence
def toggle_all_signage():
    signage_pa_side_toggle_power()
    time.sleep(2)
    signage_qr_side_toggle_power()
    time.sleep(2)
    signage_middle_hall_toggle_power()


# Turn all Quiet Rooms on/off sequence
def toggle_all_aux():
    pa_quiet_room_toggle_power()
    time.sleep(2)
    usher_quiet_room_toggle_power()
    time.sleep(2)
    nursery_toggle_power()


# Wednesday Macro on
def wednesday_macro_on():
    left_wall_toggle_power()
    time.sleep(2)
    back_fill_toggle_power()
    time.sleep(2)
    signage_middle_hall_toggle_power()
    time.sleep(2)
    turn_on_main_projector()


# Wednesday Macro off
def wednesday_macro_off():
    left_wall_toggle_power()
    time.sleep(2)
    back_fill_toggle_power()
    time.sleep(2)
    signage_middle_hall_toggle_power()
    time.sleep(2)
    turn_off_main_projector()


# Saturday Macro
def saturday_macro():
    nursery_toggle_power()
    time.sleep(2)
    signage_middle_hall_toggle_power()


# Turn on projector
def turn_on_main_projector():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[0][1])

    conn1.commit()
    conn1.close()

    ip = ip.split("\n")
    ip = str(ip[0])

    url = ('http://' + ip)
    web = webdriver.Chrome()
    web.get(url)

    time.sleep(10)

    username = 'admin'
    user_xpath = web.find_element(By.XPATH, value='//*[@id="login"]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input')
    user_xpath.send_keys(username)

    time.sleep(2)
    password = 'admin'
    pass_xpath = web.find_element(By.XPATH, value='//*[@id="login"]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input')
    pass_xpath.send_keys(password)

    time.sleep(2)
    submit = web.find_element(By.XPATH, value='//*[@id="login"]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/button/div[2]/div/div/div')
    submit.click()

    time.sleep(45)
    on = web.find_element(By.XPATH, value='//*[@id="main"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/button/div[2]/div/div/div')
    on.click()

    web.quit()


# Turn off projector
def turn_off_main_projector():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[0][1])

    conn1.commit()
    conn1.close()

    ip = ip.split("\n")
    ip = str(ip[0])

    url = ('http://' + ip)
    web = webdriver.Chrome()
    web.get(url)

    time.sleep(10)

    username = 'admin'
    user_xpath = web.find_element(By.XPATH, value='//*[@id="login"]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input')
    user_xpath.send_keys(username)

    time.sleep(2)
    password = 'admin'
    pass_xpath = web.find_element(By.XPATH, value='//*[@id="login"]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input')
    pass_xpath.send_keys(password)

    time.sleep(2)
    submit = web.find_element(By.XPATH, value='//*[@id="login"]/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/button/div[2]/div/div/div')
    submit.click()

    time.sleep(45)

    off = web.find_element(By.XPATH, value='//*[@id="main"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/div[1]/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/button/div[2]/div/div/div')
    off.click()
    time.sleep(5)
    yes = web.find_element(By.XPATH, value='/html/body/div[5]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/button/div[2]/div/div/div')
    yes.click()

    web.quit()


# All ROKU TVS
def left_wall_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[2][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[1][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Left Wall TV", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


def signage_pa_side_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[3][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[1][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Signage - PA Side", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


def signage_qr_side_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[4][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[1][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Signage - Quiet Room Side", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


def signage_middle_hall_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()
    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[5][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[1][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Signage - Middle Hall", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


# ALL QUIET ROOM TVS
def pa_quiet_room_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[7][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[3][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Quiet Room - PA Side", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


def usher_quiet_room_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[8][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[3][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Quiet Room - Usher Side", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


# NURSERY TV
def nursery_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[6][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[2][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Nursery TV", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


# BACK TV
def back_fill_toggle_power():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()

    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    ip = str(ipaddresses[1][1])

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    ircodes = str(ircodes[0][1])

    conn2.commit()
    conn2.close()

    ip = ip.split("\n")

    commands = {
        "toggle_power": ircodes
    }

    itach = iTach(ipaddress=ip[0], port=4998)
    tv = itach.add(VirtualDevice(
        name="Back Fill TV", commands=commands))

    if __name__ == "__main__":
        print(tv.toggle_power())


root = tk.Tk()
root.geometry('310x440')
root.title('POWER CONTROL')


my_menu = Menu(root)
root.config(menu=my_menu)


def ip_login():
    def login_valid():
        user_in = user_entry.get()
        pass_in = pass_entry.get()
        if user_in == 'admin' and pass_in == 'admin':
            ip_set_login.destroy()
            ip_settings()
        elif user_in != 'admin' or pass_in != 'admin':
            tk.messagebox.showerror('Error', 'The username or password you entered is not valid')

    ip_set_login = Toplevel()
    ip_set_login.geometry('210x100')
    ip_set_login.title('Login')

    username_label = ttk.Label(ip_set_login, text="Username")
    username_label.grid(column=0, row=0)
    user_entry = ttk.Entry(ip_set_login, width=10)
    user_entry.grid(column=1, row=0)

    password_label = ttk.Label(ip_set_login, text="Password")
    password_label.grid(column=0, row=1)
    pass_entry = ttk.Entry(ip_set_login, show='*', width=10)
    pass_entry.grid(column=1, row=1)

    ip_login_button = ttk.Button(ip_set_login, text='Login', command=login_valid)
    ip_login_button.grid(column=1, row=3)


def ip_settings():
    # ipfile = open('IP Configs.txt')
    # ipaddresses = ipfile.readlines()
    # ipfile.close()
    conn1 = sqlite3.connect('ip_addresses.db')

    c1 = conn1.cursor()
    c1.execute("SELECT * FROM ips")
    ipaddresses = c1.fetchall()

    def ip_setting_confirm():
        ip_confirmation = messagebox.askyesno('Warning', 'Are you sure you want to save these settings?')

        if ip_confirmation:

            mp_ip_set = ip_set_main_projector_entry.get()
            bf_ip_set = ip_set_back_fill_entry.get()
            lw_ip_set = ip_set_left_wall_entry.get()
            sps_ip_set = ip_set_sign_pa_entry.get()
            sqs_ip_set = ip_set_sign_qr_entry.get()
            smh_ip_set = ip_set_sign_mh_entry.get()
            n_ip_set = ip_set_nursery_entry.get()
            qrps_ip_set = ip_set_qr_pa_entry.get()
            qrus_ip_set = ip_set_qr_us_entry.get()

            conn1update = sqlite3.connect('ip_addresses.db')

            c1update = conn1update.cursor()
            c1update.execute("""UPDATE ips SET
                tv_location = :location,
                ip_address = :ip
                
                WHERE oid = 1""",
                             {
                                 'location': 'Main Projector', 'ip': mp_ip_set
                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 2""",
                             {
                                 'location': 'Back Fill TV',
                                 'ip': bf_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 3""",
                             {
                                 'location': 'Left Wall TV',
                                 'ip': lw_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 4""",
                             {
                                 'location': 'Signage - PA Side',
                                 'ip': sps_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 5""",
                             {
                                 'location': 'Signage - QR Side',
                                 'ip': sqs_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 6""",
                             {
                                 'location': 'Signage - Middle Hall',
                                 'ip': smh_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 7""",
                             {
                                 'location': 'Nursery TV',
                                 'ip': n_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 8""",
                             {
                                 'location': 'QR - PA Side',
                                 'ip': qrps_ip_set

                             })

            conn1update.commit()

            c1update.execute("""UPDATE ips SET
                            tv_location = :location,
                            ip_address = :ip

                            WHERE oid = 9""",
                             {
                                 'location': "QR - Usher's Side",
                                 'ip': qrus_ip_set

                             })

            conn1update.commit()
            conn1update.close()

            '''
            

            one = mp_ip_set.split('\n')
            two = bf_ip_set.split('\n')
            three = lw_ip_set.split('\n')
            four = sps_ip_set.split('\n')
            five = sqs_ip_set.split('\n')
            six = smh_ip_set.split('\n')
            seven = n_ip_set.split('\n')
            eight = qrps_ip_set.split('\n')
            nine = qrus_ip_set.split('\n')

            if len(one) != 2:
                mp_ip_set = mp_ip_set + '\n'

            if len(two) != 2:
                bf_ip_set = bf_ip_set + '\n'

            if len(three) != 2:
                lw_ip_set = lw_ip_set + '\n'

            if len(four) != 2:
                sps_ip_set = sps_ip_set + '\n'

            if len(five) != 2:
                sqs_ip_set = sqs_ip_set + '\n'

            if len(six) != 2:
                smh_ip_set = smh_ip_set + '\n'

            if len(seven) != 2:
                n_ip_set = n_ip_set + '\n'

            if len(eight) != 2:
                qrps_ip_set = qrps_ip_set + '\n'

            if len(nine) != 2:
                qrus_ip_set = qrus_ip_set + '\n'

            ipfilechange = open('IP Configs.txt', 'w')
            ipaddresses[0] = mp_ip_set
            ipaddresses[1] = bf_ip_set
            ipaddresses[2] = lw_ip_set
            ipaddresses[3] = sps_ip_set
            ipaddresses[4] = sqs_ip_set
            ipaddresses[5] = smh_ip_set
            ipaddresses[6] = n_ip_set
            ipaddresses[7] = qrps_ip_set
            ipaddresses[8] = qrus_ip_set
            ipfilechange.writelines(ipaddresses)
            ipfilechange.close()
            '''

            ip_set.destroy()

        else:
            ip_set.destroy()

    ip_set = Toplevel()
    ip_set.geometry('310x410')
    ip_set.title('IP Configurations')

    ip_set_main_projector_label = ttk.Label(ip_set, text="Main Projector")
    ip_set_main_projector_label.grid(column=0, row=0)
    ip_set_main_projector_entry = ttk.Entry(ip_set, width=10)
    ip_set_main_projector_entry.insert(0, ipaddresses[0][1])
    ip_set_main_projector_entry.grid(column=1, row=0)
    ip_set_main_projector_entry.get()

    ip_set_back_fill_label = ttk.Label(ip_set, text="Back Fill TV")
    ip_set_back_fill_label.grid(column=0, row=1)
    ip_set_back_fill_entry = ttk.Entry(ip_set, width=10)
    ip_set_back_fill_entry.insert(0, ipaddresses[1][1])
    ip_set_back_fill_entry.grid(column=1, row=1)
    ip_set_back_fill_entry.get()

    ip_set_left_wall_label = ttk.Label(ip_set, text="Left Wall TV")
    ip_set_left_wall_label.grid(column=0, row=2)
    ip_set_left_wall_entry = ttk.Entry(ip_set, width=10)
    ip_set_left_wall_entry.insert(0, ipaddresses[2][1])
    ip_set_left_wall_entry.grid(column=1, row=2)
    ip_set_left_wall_entry.get()

    ip_set_sign_pa_label = ttk.Label(ip_set, text="Signage - PA Side")
    ip_set_sign_pa_label.grid(column=0, row=3)
    ip_set_sign_pa_entry = ttk.Entry(ip_set, width=10)
    ip_set_sign_pa_entry.insert(0, ipaddresses[3][1])
    ip_set_sign_pa_entry.grid(column=1, row=3)
    ip_set_sign_pa_entry.get()

    ip_set_sign_qr_label = ttk.Label(ip_set, text="Signage - QR Side")
    ip_set_sign_qr_label.grid(column=0, row=4)
    ip_set_sign_qr_entry = ttk.Entry(ip_set, width=10)
    ip_set_sign_qr_entry.insert(0, ipaddresses[4][1])
    ip_set_sign_qr_entry.grid(column=1, row=4)
    ip_set_sign_qr_entry.get()

    ip_set_sign_mh_label = ttk.Label(ip_set, text="Signage - Middle Hall")
    ip_set_sign_mh_label.grid(column=0, row=5)
    ip_set_sign_mh_entry = ttk.Entry(ip_set, width=10)
    ip_set_sign_mh_entry.insert(0, ipaddresses[5][1])
    ip_set_sign_mh_entry.grid(column=1, row=5)
    ip_set_sign_mh_entry.get()

    ip_set_nursery_label = ttk.Label(ip_set, text="Nursery TV")
    ip_set_nursery_label.grid(column=0, row=6)
    ip_set_nursery_entry = ttk.Entry(ip_set, width=10)
    ip_set_nursery_entry.insert(0, ipaddresses[6][1])
    ip_set_nursery_entry.grid(column=1, row=6)
    ip_set_nursery_entry.get()

    ip_set_qr_pa_label = ttk.Label(ip_set, text="QR - PA Side")
    ip_set_qr_pa_label.grid(column=0, row=7)
    ip_set_qr_pa_entry = ttk.Entry(ip_set, width=10)
    ip_set_qr_pa_entry.insert(0, ipaddresses[7][1])
    ip_set_qr_pa_entry.grid(column=1, row=7)
    ip_set_qr_pa_entry.get()

    ip_set_qr_us_label = ttk.Label(ip_set, text="QR - Usher\'s Side")
    ip_set_qr_us_label.grid(column=0, row=8)
    ip_set_qr_us_entry = ttk.Entry(ip_set, width=10)
    ip_set_qr_us_entry.insert(0, ipaddresses[8][1])
    ip_set_qr_us_entry.grid(column=1, row=8)
    ip_set_qr_us_entry.get()

    conn1.commit()
    conn1.close()

    ip_set_save_button = ttk.Button(ip_set, text='Save', command=ip_setting_confirm)
    ip_set_save_button.grid(column=1, row=9)


def ir_login():
    def login_valid():
        user_in = user_entry.get()
        pass_in = pass_entry.get()
        if user_in == 'admin' and pass_in == 'admin':
            ir_set_login.destroy()
            ir_settings()
        elif user_in != 'admin' or pass_in != 'admin':
            tk.messagebox.showerror('Error', 'The username or password you entered is not valid')

    ir_set_login = Toplevel()
    ir_set_login.geometry('210x100')
    ir_set_login.title('Login')

    username_label = ttk.Label(ir_set_login, text="Username")
    username_label.grid(column=0, row=0)
    user_entry = ttk.Entry(ir_set_login, width=10)
    user_entry.grid(column=1, row=0)

    password_label = ttk.Label(ir_set_login, text="Password")
    password_label.grid(column=0, row=1)
    pass_entry = ttk.Entry(ir_set_login, show='*', width=10)
    pass_entry.grid(column=1, row=1)

    ir_login_button = ttk.Button(ir_set_login, text='Login', command=login_valid)
    ir_login_button.grid(column=1, row=3)


def ir_settings():
    # irfile = open('ircodes.txt')
    # ircodes = irfile.readlines()
    # irfile.close()

    conn2 = sqlite3.connect('ir_addresses.db')

    c2 = conn2.cursor()
    c2.execute("SELECT * FROM irs")
    ircodes = c2.fetchall()

    def ir_setting_confirm():
        ir_confirmation = messagebox.askyesno('Warning', 'Are you sure you want to save these settings?')

        if ir_confirmation:
            lg_ir_set = ir_set_lg_label_entry.get()
            roku_ir_set = ir_set_roku_label_entry.get()
            t_ir_set = ir_set_toshiba_label_entry.get()
            i_ir_set = ir_set_insignia_label_entry.get()

            conn2update = sqlite3.connect('ir_addresses.db')

            c2update = conn2update.cursor()

            c2update.execute("""UPDATE irs SET
                            tv_brand = :brand,
                            ir_code = :ir

                            WHERE oid = 1""",
                             {
                                 'brand': 'LG', 'ir': lg_ir_set
                             })
            conn2update.commit()

            c2update.execute("""UPDATE irs SET
                                        tv_brand = :brand,
                                        ir_code = :ir

                                        WHERE oid = 2""",
                             {
                                 'brand': 'Roku', 'ir': roku_ir_set
                             })
            conn2update.commit()

            c2update.execute("""UPDATE irs SET
                                        tv_brand = :brand,
                                        ir_code = :ir

                                        WHERE oid = 3""",
                             {
                                 'brand': 'Toshiba', 'ir': t_ir_set
                             })
            conn2update.commit()

            c2update.execute("""UPDATE irs SET
                                        tv_brand = :brand,
                                        ir_code = :ir

                                        WHERE oid = 4""",
                             {
                                 'brand': 'Insignia', 'ir': i_ir_set
                             })
            conn2update.commit()
            conn2update.close()

            '''one_ir = lg_ir_set.split('\n')
            two_ir = roku_ir_set.split('\n')
            three_ir = t_ir_set.split('\n')
            four_ir = i_ir_set.split('\n')

            if len(one_ir) != 2:
                lg_ir_set = lg_ir_set + '\n'

            if len(two_ir) != 2:
                roku_ir_set = roku_ir_set + '\n'

            if len(three_ir) != 2:
                t_ir_set = t_ir_set + '\n'

            if len(four_ir) != 2:
                i_ir_set = i_ir_set + '\n'

            ipfilechange = open('ircodes.txt', 'w')
            ircodes[0] = lg_ir_set
            ircodes[1] = roku_ir_set
            ircodes[2] = t_ir_set
            ircodes[3] = i_ir_set

            ipfilechange.writelines(ircodes)
            ipfilechange.close()'''

            ir_set.destroy()

        else:
            ir_set.destroy()

    ir_set = Toplevel()
    ir_set.geometry('1000x175')
    ir_set.title('IR Configurations')

    ir_set_lg_label = ttk.Label(ir_set, text="LG")
    ir_set_lg_label.grid(column=0, row=0)
    ir_set_lg_label_entry = ttk.Entry(ir_set, width=1000)
    ir_set_lg_label_entry.insert(0, ircodes[0][1])
    ir_set_lg_label_entry.grid(column=1, row=0)
    ir_set_lg_label_entry.get()

    ir_set_roku_label = ttk.Label(ir_set, text="Roku")
    ir_set_roku_label.grid(column=0, row=1)
    ir_set_roku_label_entry = ttk.Entry(ir_set, width=1000)
    ir_set_roku_label_entry.insert(0, ircodes[1][1])
    ir_set_roku_label_entry.grid(column=1, row=1)
    ir_set_roku_label_entry.get()

    ir_set_toshiba_label = ttk.Label(ir_set, text="Toshiba")
    ir_set_toshiba_label.grid(column=0, row=2)
    ir_set_toshiba_label_entry = ttk.Entry(ir_set, width=1000)
    ir_set_toshiba_label_entry.insert(0, ircodes[2][1])
    ir_set_toshiba_label_entry.grid(column=1, row=2)
    ir_set_toshiba_label_entry.get()

    ir_set_insignia_label = ttk.Label(ir_set, text="Insignia")
    ir_set_insignia_label.grid(column=0, row=3)
    ir_set_insignia_label_entry = ttk.Entry(ir_set, width=1000)
    ir_set_insignia_label_entry.insert(0, ircodes[3][1])
    ir_set_insignia_label_entry.grid(column=1, row=3)
    ir_set_insignia_label_entry.get()

    ir_set_save_button = ttk.Button(ir_set, text='Save', command=ir_setting_confirm)
    ir_set_save_button.grid(column=0, row=9)


def app_config_login():
    def login_valid():
        user_in = user_entry.get()
        pass_in = pass_entry.get()
        if user_in == 'admin' and pass_in == 'admin':
            ip_config_login.destroy()
            app_config()
        elif user_in != 'admin' or pass_in != 'admin':
            tk.messagebox.showerror('Error', 'The username or password you entered is not valid')

    ip_config_login = Toplevel()
    ip_config_login.geometry('210x100')
    ip_config_login.title('Login')

    username_label = ttk.Label(ip_config_login, text="Username")
    username_label.grid(column=0, row=0)
    user_entry = ttk.Entry(ip_config_login, width=10)
    user_entry.grid(column=1, row=0)

    password_label = ttk.Label(ip_config_login, text="Password")
    password_label.grid(column=0, row=1)
    pass_entry = ttk.Entry(ip_config_login, show='*', width=10)
    pass_entry.grid(column=1, row=1)

    ir_login_button = ttk.Button(ip_config_login, text='Login', command=login_valid)
    ir_login_button.grid(column=1, row=3)


def app_ir_config_login():
    def login_valid():
        user_in = user_entry.get()
        pass_in = pass_entry.get()
        if user_in == 'admin' and pass_in == 'admin':
            ir_config_login.destroy()
            app_ir_config()
        elif user_in != 'admin' or pass_in != 'admin':
            tk.messagebox.showerror('Error', 'The username or password you entered is not valid')

    ir_config_login = Toplevel()
    ir_config_login.geometry('210x100')
    ir_config_login.title('Login')

    username_label = ttk.Label(ir_config_login, text="Username")
    username_label.grid(column=0, row=0)
    user_entry = ttk.Entry(ir_config_login, width=10)
    user_entry.grid(column=1, row=0)

    password_label = ttk.Label(ir_config_login, text="Password")
    password_label.grid(column=0, row=1)
    pass_entry = ttk.Entry(ir_config_login, show='*', width=10)
    pass_entry.grid(column=1, row=1)

    ir_login_button = ttk.Button(ir_config_login, text='Login', command=login_valid)
    ir_login_button.grid(column=1, row=3)


def app_config():
    def app_setup_save():
        mpip = app_config_entry_mp.get()
        bfip = app_config_entry_bf.get()
        lwip = app_config_entry_lw.get()
        spasip = app_config_entry_spas.get()
        sqrsip = app_config_entry_sqrs.get()
        smhip = app_config_entry_smh.get()
        ntip = app_config_entry_nt.get()
        qrpaip = app_config_entry_qrpa.get()
        qrusip = app_config_entry_qrus.get()

        conn1 = sqlite3.connect('ip_addresses.db')
        c1 = conn1.cursor()
        c1.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ips' ''')
        conn1 = sqlite3.connect('ip_addresses.db')
        if c1.fetchone()[0] != 1:
            c1 = conn1.cursor()

            c1.execute("""CREATE TABLE ips(
                            tv_location text,
                            ip_address text
                            )""")

            conn1.commit()
            conn1.close()

        conn1.commit()
        conn1.close()
####
        conn1 = sqlite3.connect('ip_addresses.db')
        c1 = conn1.cursor()
        c1.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ips' ''')

        columns = [i[1] for i in c1.execute('PRAGMA table_info(ips)')]

        if 'tv_location' not in columns:
            c1.execute('ALTER TABLE ips ADD COLUMN tv_location TEXT')

        elif 'ip_address' not in columns:
            c1.execute('ALTER TABLE ips ADD COLUMN ip_address TEXT')
####
        else:
            conn1 = sqlite3.connect('ip_addresses.db')

            c1 = conn1.cursor()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Main Projector',
                           'ip': mpip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Back Fill TV',
                           'ip': bfip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Left Wall TV',
                           'ip': lwip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Signage - PA Side',
                           'ip': spasip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Signage - QR Side',
                           'ip': sqrsip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Signage - Middle Hall',
                           'ip': smhip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'Nursery TV',
                           'ip': ntip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'QR - PA Side',
                           'ip': qrpaip
                       })

            conn1.commit()

            c1.execute("INSERT INTO ips VALUES (:location, :ip)",
                       {
                           'location': 'QR - Usher\'s Side',
                           'ip': qrusip
                       })

            conn1.commit()

            conn1.close()

            app_setup.destroy()

    app_setup = Toplevel()
    app_setup.geometry('310x440')
    app_setup.title('Power Control IP Setup')

    # Labels
    app_config_label_mp = ttk.Label(app_setup, text="Main Projector")
    app_config_label_mp.grid(column=0, row=0)

    app_config_label_bf = ttk.Label(app_setup, text="Back Fill TV")
    app_config_label_bf.grid(column=0, row=1)

    app_config_label_lw = ttk.Label(app_setup, text="Left Wall TV")
    app_config_label_lw.grid(column=0, row=2)

    app_config_label_spas = ttk.Label(app_setup, text="Signage - PA Side")
    app_config_label_spas.grid(column=0, row=3)

    app_config_label_sqrs = ttk.Label(app_setup, text="Signage - QR Side")
    app_config_label_sqrs.grid(column=0, row=4)

    app_config_label_smh = ttk.Label(app_setup, text="Signage - Middle Hall")
    app_config_label_smh.grid(column=0, row=5)

    app_config_label_nt = ttk.Label(app_setup, text="Nursery TV")
    app_config_label_nt.grid(column=0, row=6)

    app_config_label_qrpa = ttk.Label(app_setup, text="QR - PA Side")
    app_config_label_qrpa.grid(column=0, row=7)

    app_config_label_qrus = ttk.Label(app_setup, text="QR - Usher\'s Side")
    app_config_label_qrus.grid(column=0, row=8)

    # Entries
    app_config_entry_mp = ttk.Entry(app_setup, width=10)
    app_config_entry_mp.grid(column=1, row=0)

    app_config_entry_bf = ttk.Entry(app_setup, width=10)
    app_config_entry_bf.grid(column=1, row=1)

    app_config_entry_lw = ttk.Entry(app_setup, width=10)
    app_config_entry_lw.grid(column=1, row=2)

    app_config_entry_spas = ttk.Entry(app_setup, width=10)
    app_config_entry_spas.grid(column=1, row=3)

    app_config_entry_sqrs = ttk.Entry(app_setup, width=10)
    app_config_entry_sqrs.grid(column=1, row=4)

    app_config_entry_smh = ttk.Entry(app_setup, width=10)
    app_config_entry_smh.grid(column=1, row=5)

    app_config_entry_nt = ttk.Entry(app_setup, width=10)
    app_config_entry_nt.grid(column=1, row=6)

    app_config_entry_qrpa = ttk.Entry(app_setup, width=10)
    app_config_entry_qrpa.grid(column=1, row=7)

    app_config_entry_qrus = ttk.Entry(app_setup, width=10)
    app_config_entry_qrus.grid(column=1, row=8)

    app_set_save_button = ttk.Button(app_setup, text='Save', command=app_setup_save)
    app_set_save_button.grid(column=1, row=9)


def app_ir_config():
    def app_ir_setup_save():
        lgir = app_config_entry_lg.get()
        rir = app_config_entry_r.get()
        tir = app_config_entry_t.get()
        iir = app_config_entry_i.get()

        conn2 = sqlite3.connect('ir_addresses.db')
        c2 = conn2.cursor()
        c2.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='irs' ''')

        conn2 = sqlite3.connect('ir_addresses.db')
        if c2.fetchone()[0] != 1:
            c2 = conn2.cursor()

            c2.execute("""CREATE TABLE irs(
                    tv_brand text,
                    ir_code text
                    )""")

            conn2.commit()
            conn2.close()

        conn2.commit()
        conn2.close()

        conn2 = sqlite3.connect('ir_addresses.db')
        c2 = conn2.cursor()
        c2.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='irs' ''')

        columns = [i[1] for i in c2.execute('PRAGMA table_info(irs)')]

        if 'tv_brand' not in columns:
            c2.execute('ALTER TABLE irs ADD COLUMN tv_brand TEXT')

        elif 'ir_code' not in columns:
            c2.execute('ALTER TABLE irs ADD COLUMN ir_code TEXT')

        else:
            conn2.commit()
            conn2.close()

            conn2 = sqlite3.connect('ir_addresses.db')

            c2 = conn2.cursor()

            c2.execute("INSERT INTO irs VALUES (:brand, :ir)",
                       {
                           'brand': 'LG',
                           'ir': lgir
                       })

            conn2.commit()

            c2.execute("INSERT INTO irs VALUES (:brand, :ir)",
                       {
                           'brand': 'Roku',
                           'ir': rir
                       })

            conn2.commit()

            c2.execute("INSERT INTO irs VALUES (:brand, :ir)",
                       {
                           'brand': 'Toshiba',
                           'ir': tir
                       })

            conn2.commit()

            c2.execute("INSERT INTO irs VALUES (:brand, :ir)",
                       {
                           'brand': 'Insignia',
                           'ir': iir
                       })

            conn2.commit()
            conn2.close()

            app_ir_setup.destroy()

    app_ir_setup = Toplevel()
    app_ir_setup.geometry('1000x175')
    app_ir_setup.title('Power Control IR Setup')

    app_config_label_lg = ttk.Label(app_ir_setup, text="LG")
    app_config_label_lg.grid(column=0, row=0)

    app_config_label_r = ttk.Label(app_ir_setup, text="Roku")
    app_config_label_r.grid(column=0, row=1)

    app_config_label_t = ttk.Label(app_ir_setup, text="Toshiba")
    app_config_label_t.grid(column=0, row=2)

    app_config_label_i = ttk.Label(app_ir_setup, text="Insignia")
    app_config_label_i.grid(column=0, row=3)

    app_config_entry_lg = ttk.Entry(app_ir_setup, width=100)
    app_config_entry_lg.grid(column=1, row=0)

    app_config_entry_r = ttk.Entry(app_ir_setup, width=100)
    app_config_entry_r.grid(column=1, row=1)

    app_config_entry_t = ttk.Entry(app_ir_setup, width=100)
    app_config_entry_t.grid(column=1, row=2)

    app_config_entry_i = ttk.Entry(app_ir_setup, width=100)
    app_config_entry_i.grid(column=1, row=3)

    app_set_save_button = ttk.Button(app_ir_setup, text='Save', command=app_ir_setup_save)
    app_set_save_button.grid(column=1, row=4)


setting = Menu(my_menu)
my_menu.add_cascade(label="Settings", menu=setting)
setting.add_command(label="IP Configuration", command=ip_login)
setting.add_command(label="IR Configuration", command=ir_login)
setting.add_command(label="IP Initial Setup", command=app_config_login)
setting.add_command(label="IR Initial Setup", command=app_ir_config_login)
setting.add_command(label="Version 1.1")


all_on_label = ttk.Label(root, text="All ON")
all_on_label.grid(column=0, row=0)

all_on_button = ttk.Button(root, text="Power ON", command=toggle_all_on)
all_on_button.grid(column=0, row=1)

signage_all_on_label = ttk.Label(root, text="All OFF")
signage_all_on_label.grid(column=1, row=0)

signage_all_on_button = ttk.Button(root, text="Power OFF", command=toggle_all_off)
signage_all_on_button.grid(column=1, row=1)

nursery_all_on_label = ttk.Label(root, text="Signage")
nursery_all_on_label.grid(column=0, row=3)

nursery_all_on_button = ttk.Button(root, text="Power ON/OFF", command=toggle_all_signage)
nursery_all_on_button.grid(column=0, row=4)

qr_all_on_label = ttk.Label(root, text="QR/Nursery")
qr_all_on_label.grid(column=1, row=3)

qr_all_on_button = ttk.Button(root, text="Power ON/OFF", command=toggle_all_aux)
qr_all_on_button.grid(column=1, row=4)

macros_label = ttk.Label(root, text="MACROS")
macros_label.grid(column=0, row=5)

qr_all_on_button = ttk.Button(root, text="Wednesday ON", command=wednesday_macro_on)
qr_all_on_button.grid(column=0, row=6)

qr_all_on_button = ttk.Button(root, text="Saturday ON", command=saturday_macro)
qr_all_on_button.grid(column=1, row=6)

qr_all_on_button = ttk.Button(root, text="Wednesday OFF", command=wednesday_macro_off)
qr_all_on_button.grid(column=0, row=7)

qr_all_on_button = ttk.Button(root, text="Saturday OFF", command=saturday_macro)
qr_all_on_button.grid(column=1, row=7)

individual_label = ttk.Label(root, text="INDIVIDUAL CONTROLS")
individual_label.grid(column=0, row=8)

projector_on_label = ttk.Label(root, text="Main Projector")
projector_on_label.grid(column=0, row=9)

projector_on_button = ttk.Button(root, text="Power ON", command=turn_on_main_projector)
projector_on_button.grid(column=0, row=10)

projector_off_label = ttk.Label(root, text="Main Projector")
projector_off_label.grid(column=1, row=9)

projector_off_button = ttk.Button(root, text="Power OFF", command=turn_off_main_projector)
projector_off_button.grid(column=1, row=10)

left_wall_label = ttk.Label(root, text="Left Wall TV")
left_wall_label.grid(column=0, row=11)

left_wall_button = ttk.Button(root, text="Power ON/OFF", command=left_wall_toggle_power)
left_wall_button.grid(column=0, row=12)

back_fill_label = ttk.Label(root, text="Back Fill TV")
back_fill_label.grid(column=1, row=11)

back_fill_button = ttk.Button(root, text="Power ON/OFF", command=back_fill_toggle_power)
back_fill_button.grid(column=1, row=12)

sign_pa_label = ttk.Label(root, text="Signage - PA Side")
sign_pa_label.grid(column=0, row=13)

sign_pa_button = ttk.Button(root, text="Power ON/OFF", command=signage_pa_side_toggle_power)
sign_pa_button.grid(column=0, row=14)

sign_qr_label = ttk.Label(root, text="Signage - QR Side")
sign_qr_label.grid(column=1, row=13)

sign_qr_button = ttk.Button(root, text="Power ON/OFF", command=signage_qr_side_toggle_power)
sign_qr_button.grid(column=1, row=14)

sign_middle_label = ttk.Label(root, text="Signage - Middle Hall")
sign_middle_label.grid(column=0, row=15)

sign_middle_button = ttk.Button(root, text="Power ON/OFF", command=signage_middle_hall_toggle_power)
sign_middle_button.grid(column=0, row=16)

nursery_label = ttk.Label(root, text="Nursery TV")
nursery_label.grid(column=1, row=15)

nursery_button = ttk.Button(root, text="Power ON/OFF", command=nursery_toggle_power)
nursery_button.grid(column=1, row=16)

qr_pa_label = ttk.Label(root, text="QR - PA Side")
qr_pa_label.grid(column=0, row=17)

qr_pa_button = ttk.Button(root, text="Power ON/OFF", command=pa_quiet_room_toggle_power)
qr_pa_button.grid(column=0, row=18)

qr_usher_label = ttk.Label(root, text="QR - Usher's Side")
qr_usher_label.grid(column=1, row=17)

qr_usher_button = ttk.Button(root, text="Power ON/OFF", command=usher_quiet_room_toggle_power)
qr_usher_button.grid(column=1, row=18)


root.mainloop()
