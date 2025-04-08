  # Lab4

1. List **all running processes** and save the output to `~/processes.txt`.  
2. Find the **PID (Process ID)** of the `sshd` service.  
3. Run a `sleep 500` command in the background, then **kill it** after 5 seconds.  

4. Install `apache2` service, edit the default HTML file (`/var/www/html/index.html`), and verify changes in a web browser.  
5. **Check if `sshd` (SSH service) is running**. If not, start and enable it.  
6. **Restart the `cron` service** and verify its status.  

7. Create a **compressed tarball** (`archive.tar.gz`) of `/var/log` and save it in your home directory.  
8. **Extract** the tarball into `~/logs_backup/`.  
9. Create a **non-compressed tarball** (`archive.tar`) of `/etc/ssh` and save it in `/tmp`.  

10. Compress `~/processes.txt` using `gzip`.  
11. **Decompress** it and compare file sizes using `ls -lh`.  

12. **Install `htop`** (a process viewer) using your package manager.  
13. **Search for the package `nginx`** (or `httpd`) but do not install it.  
14. **Remove the `vim` editor** (if installed) and then reinstall it.  

15. Use `wget` to download the Linux kernel source:  
    
    ```  
16. Use `curl` to fetch **Google’s homepage** and save it as `google.html`.  

17. **Create a new VM** (e.g., VirtualBox/Cloud instance), add a user to the `sudoers` group, and run `apt update && apt upgrade`.  
18. **Generate an SSH key pair** using `ssh-keygen`.  
19. **Copy your public key** to the remote server:  
20. **SSH into the server** and verify with `hostname`.  
21. **Transfer the archived file** (e.g., `archive.tar.gz`) to the remote server using ssh copy way (don’t copy/paste >>> you have to search)



## Solution


#### 1. ps aux > ~/processes.txt


------------------------------------------------------------------------------------------

#### 2.ps aux | grep sshd


------------------------------------------------------------------------------------------



#### 3./home/osama/Pictures/Screenshots/Screenshot from 2025-04-08 14-38-15.png

------------------------------------------------------------------------------------------

#### 4.sudo apt install apache2
      sudo nano /var/www/html/index.html
------------------------------------------------------------------------------------------

#### 5.sudo apt install openssh-server -y
     sudo systemctl start  ssh
     sudo systemctl status ssh


------------------------------------------------------------------------------------------



#### 6.sudo systemctl restart cron


------------------------------------------------------------------------------------------

#### 7.tar -czvf ~/archive.tar.gz /var/log


------------------------------------------------------------------------------------------

#### 8.tar -xzvf ~/archive.tar.gz -C ~/logs_backup/extractedlogs



------------------------------------------------------------------------------------------

#### 9. tar -cvf /tmp/archive.tar  /etc/ssh

------------------------------------------------------------------------------------------

#### 10. gzip ~/processes.txt 


------------------------------------------------------------------------------------------

#### 11.ls -lh ~/processes.txt ~/processes.txt.gz


------------------------------------------------------------------------------------------

#### 12. sudo apt install htop


------------------------------------------------------------------------------------------

#### 13.sudo apt search nginx


------------------------------------------------------------------------------------------

#### 14.sudo apt remove vim 



------------------------------------------------------------------------------------------

#### 15.wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.15.23.tar.xz



------------------------------------------------------------------------------------------

#### 16.sudo curl https://www.google.com -o google.html



------------------------------------------------------------------------------------------

#### 17. sudo useradd sayed 
     echo 'sayed:man7o'
     sudo visudo 'then edit'
     sudo apt update
     sudo apt upgrade



------------------------------------------------------------------------------------------

#### 18.sudo ssh-keygen -t rsa -b 4096 -C "usamashakerr@gmail.com"



------------------------------------------------------------------------------------------

#### 19.sudo ssh-copy-id -i /home/sayed/keyss.pub osama@192.168.1.8 <---------


------------------------------------------------------------------------------------------

#### 20.ssh osama@192.168.1.8



------------------------------------------------------------------------------------------

#### 21.scp home/sayed/archived.tar.gz osama@192.168.1.8:/home/osama/
