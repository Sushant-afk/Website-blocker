from tkinter import messagebox

ip_address = '127.0.0.1'
host_path = r'C:\Windows\System32\drivers\etc\hosts'

def blockWebsite(website):
    website = website.strip('\n')
    if len(website) > 12:
        messagebox.showwarning("warning", "Enter a valid website name")
    website_path = ip_address + ' www.' + website + '.com\n'
    with open(host_path, 'r+') as host_file:
        in_block_list = False
        for line in host_file:
            if line == website_path:
                in_block_list = True
                break
        if in_block_list is False:
            host_file.write(website_path)
            messagebox.showinfo("success", website + ' is blocked')
        else:
            messagebox.showinfo("", website + ' is already in block list')
        

def getBlockedWebsites():
    list = []
    with open(host_path, 'r') as host_file:
        for line in host_file:
            if len(line) > 10 and line[:9] == ip_address:
                list.append(line[10:].strip('\n'))
    return list

def removeFromBlocklist(website):
    website = website.strip('\n')
    website_path = ip_address + ' ' + website
    print(website_path, len(website_path))
    with open(host_path, 'r+') as host_file:
        lines = host_file.readlines()
        host_file.seek(0)
        for line in lines:
            if line.strip('\n') != website_path:
                host_file.write(line)
            else:
                pass
        host_file.truncate()
