# Lab 3
   
1. Create a user account with the following attribute
   • username: “your first name”
   • Fullname/comment: “full name”
   • Password: islam
2. Create a user account with the following attribute
   • Username: baduser
   • Full name/comment: Bad User
   • Password: baduser
3. Create a supplementary (Secondary) group called pgroup with group ID of 30000
4. Create a supplementary group called badgroup
5. Add islam user to the pgroup group as a supplementary group
6. Modify the password of islam's account to password
7. Modify islam's account so the password expires after 30 days
8. Lock bad user account so he can't log in
9. Delete bad user account
10. Delete the supplementary group called badgroup
11. Create a folder called myteam in your home directory and change its permissions to read only for the owner.
12. Log out and log in by another user
13. Try to access (by cd command) the folder (myteam)
14. Using the command Line
    • Change the permissions of oldpasswd file to give owner read and write permissions and for group write and execute and execute only for the others (using chmod in 2 different ways)
    • Change your default permissions to be as above.
    • What is the maximum permission a file can have, by default when it is just created? And what is that for directory.
    • Change your default permissions to be no permission to everyone then create a directory and a file to verify.
15. Starting from your home directory, find all files that were modified in the last two day.
16. Starting from /etc, find files owned by root user.
17. Find all directories in your home directory.
18. Write a command to search for all files on the system that, its name is ".profile".
19. Identify the file types of the following: /etc/passwd, /dev/pts/0, /etc, /dev/sda
20. List the inode numbers of /, /etc, /etc/hosts.
21. Copy /etc/passwd to your home directory, use the commands diff and cmp, and Edit in the file you copied, and then use these commands again, and check the output.
22. Create a symbolic link of /etc/passwd in /boot.
23. Create a hard link of /etc/passwd in /boot. Could you? Why?

# Solution

1. #### sudo useradd -c 'osama shaker' -m shaker , then to change the password you can do it through "echo "shaker:islam" | sudo chpasswd" or go to the root then write "passwd shaker"

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2. #### sudo adduser -c 'Bad User' -m baduser ,then we can change the password through 'echo "baduser:badpassword" | sudo chpasswd' or from the root

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


3. #### sudo groupadd -g 30000 pgroup
   #### sudo usermod -aG pgroup shaker

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


4. #### sudo groupadd bad group
   #### sudo usermod -aG badgroup shaker

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


5. #### sudo usermod -aG pgroup shaker

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


6. #### echo "shaker:password" | sudo chpasswd

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


7. #### sudo passwd -x 30 shaker

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


8. #### sudo usermod -L baduser

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


9. #### sudo deluser baduser

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


10. #### sudo delgroup badgroup

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


11. #### sudo chown 400 /home/myteam

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


12. #### u should create a home dir if it's not exist to work

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


13. #### cannot access 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


14. a.
    ![image](https://github.com/user-attachments/assets/004cca67-b518-41a4-89ff-eee91e0edd35)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    b.
     ![image](https://github.com/user-attachments/assets/54cf9e16-f9df-4903-ae6e-40f4b67d7666)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


     c. 666 for a file , and 777 for a directory


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

     d.
    ![image](https://github.com/user-attachments/assets/2ec4d564-c1f2-4252-9b68-983bdf36146c)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


15.

![image](https://github.com/user-attachments/assets/d8a3d0bf-d0bf-460c-b775-03ca2855845d)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


16.
  #### ![image](https://github.com/user-attachments/assets/c219613d-4b8d-4d50-ad9a-b2db1176ad3b)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

17.
![image](https://github.com/user-attachments/assets/da0ebe65-2f4d-4357-b536-77c5ffe4a6d7)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


18. #### find /-type f -name '.profile'

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


19. #### sudo file /etc/passwd /dev/pts/0  /etc  /dev/sda

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


20.  #### ls -i /etc /etc/hosts

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


21. #### sudo diff /etc/passwd /home/oldpasswd

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



22. #### sudo ln -s /etc/passwd /boot/symbloicpasswd
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



23. #### to be reviewed
    ![image](https://github.com/user-attachments/assets/391cafad-3d20-4c79-9685-90b599edb799)
