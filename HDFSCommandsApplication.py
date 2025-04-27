import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

def hdfs_command(base_command, use_path=True, two_paths=False):
    if two_paths:
        src_path = simpledialog.askstring('HDFS Source Path', 'Enter the source path:')
        if not src_path:
            return
        dst_path = simpledialog.askstring('HDFS Destination Path', 'Enter the destination path:')
        if not dst_path:
            return
        command = f'{base_command} {src_path} {dst_path}'
    elif use_path:
        path = simpledialog.askstring('HDFS Path', 'Enter the HDFS file or directory path:')
        if not path:
            return
        command = f'{base_command} {path}'
    else:
        command = base_command

    run_command(command)

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)
        status.config(text="Command executed successfully.")
    except subprocess.CalledProcessError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, e.output)
        status.config(text="Command failed.")

root = tk.Tk()
root.title(' HDFS Manager')
root.geometry('700x700')
root.configure(bg="#f0f4f7")

tk.Label(root, text=" HDFS Manager", font=('Arial', 25, 'bold'), bg="#f0f4f7", fg="#2c3e50").pack(pady=10)

frame_manage = tk.LabelFrame(root, text="File & Directory Operations", padx=10, pady=10, bg="#e8f0fe")
frame_manage.pack(padx=10, pady=5, fill="both", expand=True)

frame_transfer = tk.LabelFrame(root, text="Transfer Operations", padx=10, pady=10, bg="#e8f0fe")
frame_transfer.pack(padx=10, pady=5, fill="both", expand=True)

frame_navigation = tk.LabelFrame(root, text="Navigation & Viewing", padx=10, pady=10, bg="#e8f0fe")
frame_navigation.pack(padx=10, pady=5, fill="both", expand=True)

frame_control = tk.LabelFrame(root, text="Hadoop Services Control", padx=10, pady=10, bg="#e8f0fe")
frame_control.pack(padx=10, pady=5, fill="both", expand=True)

output_text = tk.Text(root, height=10, width=80, bg="white", fg="black")
output_text.pack(pady=10)

status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#dfe6e9")
status.pack(side=tk.BOTTOM, fill=tk.X)

def delete_lab1():
    hdfs_command('hdfs dfs -rm -r -f ', use_path=True)

def list_custom_path():
    hdfs_command("hdfs dfs -ls", use_path=True)

def view_content():
    hdfs_command("hdfs dfs -cat", use_path=True)

def create_dir():
    hdfs_command('hdfs dfs -mkdir', use_path=True)

def copy_hdfs_file():
    hdfs_command("hdfs dfs -cp", two_paths=True)

def move_hdfs_file():
    hdfs_command("hdfs dfs -mv", two_paths=True)

def upload_local_hdfs():
    hdfs_command('hdfs dfs -put', two_paths=True)

def download_hdfs_local():
    hdfs_command('hdfs dfs -get', two_paths=True)

def start_hdfs():
    run_command('start-dfs.sh')

def start_yarn():
    run_command('start-yarn.sh')

def stop_hdfs():
    run_command('stop-dfs.sh')

def stop_yarn():
    run_command('stop-yarn.sh')


# Manage
tk.Button(frame_manage, text='Create Directory', command=create_dir, width=30, bg="#74b9ff", fg="white").pack(pady=5)
tk.Button(frame_manage, text='Delete /lab1 Directory', command=delete_lab1, width=30, bg="#d63031", fg="white").pack(pady=5)

# Transfer
tk.Button(frame_transfer, textS='Upload Files (Local to HDFS)', command=upload_local_hdfs, width=30, bg="#00b894", fg="white").pack(pady=5)
tk.Button(frame_transfer, text='Download Files (HDFS to Local)', command=download_hdfs_local, width=30, bg="#00cec9", fg="white").pack(pady=5)
tk.Button(frame_transfer, text='Copy Files (HDFS to HDFS)', command=copy_hdfs_file, width=30, bg="#0984e3", fg="white").pack(pady=5)
tk.Button(frame_transfer, text='Move Files (HDFS to HDFS)', command=move_hdfs_file, width=30, bg="#6c5ce7", fg="white").pack(pady=5)

# Navigation
tk.Button(frame_navigation, text='List Custom HDFS Path', command=list_custom_path, width=30, bg="#fdcb6e", fg="black").pack(pady=5)
tk.Button(frame_navigation, text='View File Content', command=view_content, width=30, bg="#fab1a0", fg="black").pack(pady=5)

# Control
tk.Button(frame_control, text='Start HDFS', command=start_hdfs, width=30, bg="#55efc4", fg="black").pack(pady=5)
tk.Button(frame_control, text='Start YARN', command=start_yarn, width=30, bg="#81ecec", fg="black").pack(pady=5)
tk.Button(frame_control, text='Stop HDFS', command=stop_hdfs, width=30, bg="#ffeaa7", fg="black").pack(pady=5)
tk.Button(frame_control, text='Stop YARN', command=stop_yarn, width=30, bg="#fab1a0", fg="black").pack(pady=5)

root.mainloop()
