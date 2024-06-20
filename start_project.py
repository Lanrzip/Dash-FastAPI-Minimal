import subprocess
import os
import sys

def run_command(command, cwd):
    process = subprocess.Popen(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    # 定义各个命令和对应的目录
    commands = [
        {"command": "python app.py", "cwd": os.path.join(os.getcwd(), 'front-end')},
        {"command": "python app.py", "cwd": os.path.join(os.getcwd(), 'back-end')},
        {"command": "npx tailwindcss -i ./input.css -o ../assets/css/out.css --watch", "cwd": os.path.join(os.getcwd(), 'front-end', 'node')}
    ]

    processes = []

    for cmd in commands:
        print(f"Running command: {cmd['command']} in directory: {cmd['cwd']}")
        process = run_command(cmd['command'], cmd['cwd'])
        processes.append(process)

    # 等待所有子进程完成
    for process in processes:
        stdout, stderr = process.communicate()
        print(f"Command output: {stdout.decode()}")
        if stderr:
            print(f"Command error: {stderr.decode()}", file=sys.stderr)

if __name__ == "__main__":
    main()
