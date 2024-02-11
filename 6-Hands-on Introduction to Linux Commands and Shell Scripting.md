## W1 ❉ Introduction to linux 
📓**Introduction to Linux**
 **➡ Introducing Linux and Unix**
- **Unix Overview:**
  - Unix is a family of operating systems.
  - Popular Unix-based operating systems include:
    - Oracle Solaris (and Open Solaris)
    - FreeBSD
    - HP-UX
    - IBM AIX
    - Apple macOS (popular desktop OS).

- **Origins of Unix:**
  - Original Unix created in the 1960s at AT&T Bell Labs for PDP-7 computer.
  - Rewritten in C in the 1970s, making it portable to various hardware architectures.
  - UC Berkeley developed Berkeley Software Distribution (BSD) in the late 1970s.

- **Introduction to Linux:**
  - Linux is a family of Unix-like operating systems.
  - Developed as a free, open-source version of Unix.
  - Key features include being free, open source, multi-user, supporting multitasking, and portability.

- **Development of Linux:**
  - In the 1980s, GNU (GNU's not Unix) developed at MIT, offering Unix system tools.
  - Linus Torvalds developed the Linux kernel in 1991.
  - GNU and Linux were unified in 1992, leading to popular Linux operating systems.

- **Linux Mascot and Popularity:**
  - In 1996, "Tux" the penguin became the official Linux mascot.
  - BSD-based macOS runs on millions of devices.
  - Linux is widely used in servers, supercomputers, data centers, and gaining popularity among PC users.

- **Common Use Cases for Linux:**
  - Linux is used in billions of smartphones via the Android operating system.
  - Widely used in supercomputers, enterprise and cloud data centers.
  - Many people install Linux on their PCs for learning or daily use.

 **➡ Linux Distributions**
- **What is a Linux Distribution (Distro):**
  - A Linux distribution is a specific flavor of the Linux operating system.
  - Also referred to as a "distro."
  - All Linux distributions must use the Linux kernel, the core component enabling hardware usage.

- **Distinguishing Features of Linux Distros:**
  - Each Linux distro has:
    - Unique default utilities, including commands and prepackaged applications.
    - Its own graphical user interface (GUI).
    - Support for specific commands in a shell.
    - Varying levels of support, community-backed or commercial, with different release models (LTS or rolling release).

- **Overview of Specific Linux Distros:**
  - **Debian:**
    - One of the earliest distros, released in 1993.
    - Known for stability, reliability, and full open source.
    - Supports multiple hardware architectures.
    - Highly regarded in the server space.
    - Largest community-run distro.

  - **Ubuntu:**
    - First official release in 2004, Debian-based.
    - Developed and managed by Canonical.
    - Three official editions: Desktop, Server, and Core.
  
  - **Red Hat Linux:**
    - Stable, reliable, and fully open source.
    - Managed by Red Hat, an IBM subsidiary.
    - Shipped as Red Hat Enterprise Linux (RHEL), focused on enterprise customers.

  - **Fedora:**
    - Known for stability, security, and unique firewall features.
    - Actively developed, sponsored by Red Hat.
    - Used as a testing ground for RHEL.

  - **SUSE Linux Enterprise:**
    - Available in Server (SLES) and Desktop (SLED) editions.
    - Supports various architectures, including ARM for Raspberry Pi.
    - Maintained by the open-source software company, SUSE.

  - **Arch Linux:**
    - Unique, do-it-yourself approach for high customization.
    - Highly configurable but requires a strong understanding of Linux.
    - Emphasizes access to the newest software with less stability guarantee.

- **Key Takeaways:**
  - Linux distros can be differentiated by user interfaces, shell applications, and how the operating system is supported and built.
  - Design of a Linux distro is tailored to a specific audience.
  - Debian is known for stability and reliability in the server space.
  - Red Hat Enterprise Linux focuses entirely on enterprise customers.
  - SUSE Linux Enterprise supports various architectures, including ARM for Raspberry Pi.

 **➡ Overview of Linux Architecture**
- **Layers in a Linux System:**
  - **1-User Interface (UI):**
    - Outermost layer allowing user interaction with the system.
    - May include a Graphical User Interface (GUI) for desktop versions.
  
  - **2-Application Layer:**
    - Includes system daemons, shells, user apps, and tools.
    - Applications communicate with the operating system for task execution.

  - **3-Operating System (OS):**
    - Manages system stability, job scheduling, and time tracking.
    - Built on top of the Linux kernel.

  - **4-Linux Kernel:**
    - Core component managing memory, processing, and security.
    - Performs lower-level vital operations.
    - Interacts with the hardware layer.

  - **5-Hardware Layer:**
    - Consists of physical or electronic devices in the computer.
    - Includes CPU, RAM, storage, screen, and peripheral devices.

- **Roles of Each Layer:**
  - **User Interface:**
    - Allows users to control applications using a keyboard or mouse.

  - **Application Layer:**
    - Encompasses system tools, programming languages, shells, and user apps.

  - **Operating System:**
    - Manages vital system functions, detects errors, and performs file management.

  - **Linux Kernel:**
    - Lowest-level software with complete control.
    - Bridges apps and hardware using "system calls."
    - Performs memory and process management, manages device drivers, and ensures system security.

  - **Hardware Layer:**
    - Includes CPU, RAM, storage, screen, and peripherals.

- **Linux Filesystem:**
  - Collection of files on the machine.
  - Top level is the root directory ("/").
  - Tree-like structure with directories like /bin, /usr, /home, /boot, and /media.
  - Files and directories organized based on their purpose.
  - Root directory contains many other directories and files with designated purposes.

- **Key Takeaways:**
  - Linux system comprises five layers.
  - User Interface enables user interaction.
  - Applications execute tasks and communicate with the OS.
  - Linux Kernel performs vital operations and interacts with hardware.
  - Hardware includes physical or electronic components.
  - Linux Filesystem is a tree-like structure organizing directories and files based on their purpose.

 **➡ Linux Terminal Overview**

- **Linux Shell:**
  - An OS-level application interpreting commands.
  - Historically the primary way to interact with Unix and Linux systems.
  - Remains popular for its flexibility and scripting capabilities.
  - Examples include Bash and Zsh.

- **Linux Terminal:**
  - An application or user interface where users enter and receive command output.
  - Commands can be used for tasks like file operations, data extraction, and searching.

- **Interaction with Linux Terminal:**
  - User enters a command in the terminal.
  - Command relayed to the shell.
  - OS components and kernel interpret the command for hardware execution.
  - Results sent back to the terminal for user information.

- **Terminal User Interface:**
  - Most terminals have a similar interface.
  - Command line for entering commands.
  - Cursor (command prompt) indicates where typed text will display.

- **Current Working Directory:**
  - Represents the location where the shell looks for commands.
  - Displayed in the command prompt.
  - Path structure (e.g., /home/me/Documents) indicates directory hierarchy.

- **Special Paths:**
  -  (~) refers to the user's home directory.
  - Single slash at the beginning (/) refers to the root directory.
  - Two periods (..) refer to the parent directory.
  - A single period (.) refers to the current directory.

- **Executing Programs in the Terminal:**
  - Running the Python application using `python myprogram.py`.
  - Demonstrating program output in the terminal.

- **Key Takeaways:**
  - Linux shell interprets commands and remains a popular choice for interaction.
  - A terminal is an interface to enter and receive command output.
  - Commands can be used for various tasks, and navigation is facilitated by the `cd` command.

```bash

>>To view the contents of the current directory:>>
ls

>>To list the contents of a specific directory:>>
ls /path/to/directory

>>----------------------->>

>>To change to a specific directory:>>
cd /path/to/directory

>>To go up one level:>>
cd ..

>>To go back to the home directory:>>
cd ~

>>----------------------->>
>>To create a new directory:>>
mkdir new_directory

>>----------------------->>

>>To remove an empty directory:>>
rmdir empty_directory

>>To remove a directory and its contents recursively:>>
rm -r directory_to_remove

>>----------------------->>
>>To copy a directory and its contents:>>
cp -r source_directory destination_directory

>>----------------------->>
>>To move a directory:>>
mv source_directory destination_directory

>>To rename a directory:>>
mv old_directory_name new_directory_name

>>----------------------->>
>>To print the current working directory:>>
pwd

>>----------------------->>
>>To find files and directories based on certain criteria:>>
find /path/to/search -name "filename"

>>----------------------->>
```

## W2 ❉ Introduction to linux commands
📓**Informational, Navigational, & Management Commands**
 **➡ Getting Help for Linux Commands**
```bash
>>----------------------->>
>> return your current username
whoami

>>----------------------->>
>> prints the kernel name
uname 

>> prints all the system information.
uname -a

>>----------------------->>
>> lists each process that is currently running and its PID (process id).
ps
>>----------------------->>
>> "table of processes" command provides a dynamic, real-time view of your system
top

>>----------------------->>
>> echo command displays the given text on the screen
echo "Welcome to the linux lab"

>> special characters
\n	>> Start a new line
\t	>> Insert a tab
-e >> when working with special characters

echo -e "This will be printed \nin two lines"
>>----------------------->>
>> date command displays the current date and time.
date

>> displays the current date in mm/dd/yy format:
date "+%D"
date "+Specifier"

Specifiers
%d	>> Displays the day of the month (01 to 31)
%h	>> Displays the abbreviated month name (Jan to Dec)
%m	>> Displays the month of year (01 to 12)
%Y	>> Displays the four-digit year
%T	>> Displays the time in 24 hour format as HH:MM:SS
%H	>> Displays the hour

>>----------------------->>

```

 **➡ Navigating and Managing Files and Directories**
 
```bash

>>----------------------->>
>>print the name of the directory you are currently working in.
pwd

>>----------------------->>
>> To list the files and directories in the current directory
ls
>>To list all files starting with b in the /bin directory
* is a special character called a wildcard. It is used to represent any string of characters.

ls /bin/b*

>> To list all files ending in r in the /bin directory
ls /bin/*r

ls -
-a	 >> list all files, including hidden files
-d	 >> list directories only, do not include files
-h	 >> with -l and -s, print sizes like 1K, 234M, 2G
-l	 >> include attributes like permissions, owner, size, and last-modified date
-S	 >> sort by file size, largest first
-t	 >> sort by last-modified date, newest first
-r	 >> reverse the sort order

combined the options -l and -a by using the shorter notation, -la

>>----------------------->>
>> mkdir to create a new directory(folder)
mkdir scripts 

>>----------------------->>
>>touch command to create an empty file named
touch myfile.txt

>> date command to verify the date change:
date -r myfile.txt

>>----------------------->>
>>find command conducts a search of the entire directory tree starting from the given directory name.

find /etc -name \'*.txt\' 
>>----------------------->>
>> rm command is used to delete files, ideally with the -i option, which creates a prompt to ask for confirmation before every deletion.

rm -i myfile.txt

>>----------------------->>
>> mv to rename users.txt to user-info.txt by entering the following command:

mv users.txt user-info.txt

>> move user-info.txt to the /tmp directory as follows:
mv user-info.txt /tmp

>>----------------------->>
>> cp command to copy user-info.txt, which is now in your /tmp directory, to your current working directory:

cp /tmp/user-info.txt user-info.txt


```

 **➡ Security: Managing File Permisions and Ownership**
**File ownership and permissions**
There are three possible levels of file ownership in Linux: user, group, and other:

-**user** at the time of creation, becomes the owner of that file by default. A 
-**group** of users can also share ownership of a file. 
-**The other** category essentially refers anyone in the universe with access to your Linux machine
Only an official owner of a file is allowed to change its permissions

```bash
>>----------------------->>
>> more command to print the contents of the new file_name
more file_name
>>----------------------->>
>> ls command with the -l option displays the file (default) permissions: 
ls -l file_name

rw-r--r--

(rw-) define the user permissions, 
the next three (r--) the group pemissions, 
and the final three (r--) the other permissions.
rwxrwxrwx

r	>> read
w	>> write
x	>> execute

```

 **Directory permissions**
The permissions for directories are similar but distinct for files. Though directories use the same rwx format, the symbols have slightly different meanings.

```bash
r	>> List directory contents using ls command
w	>> Add or remove files or directories
x	>> Enter directory using cd command

```

 **Making a file private**
 revoke read permissions from your group and all other users by using the chmod
```bash
chmod change mode command can be used with both files and directories.
r, w, x	>> Permissions: read, write, and execute
u,g, o 	>> User categories: user, group, and all others
+, -	>> Operations: grant and revoke


go-r is the permission change to be applied, which in this case means removing for the group (g) and others (o)

chmod go-r file_name
ls -l file_name
>>----------------------->>
 >> following command revokes read permissions for all users (user, group, and other) on the file usdoi.txt:
 
chmod -r usdoi.txt               

>> to remove the read permission only for 'other' category, enter the following:
chmod o-r usdoi.txt

```

 **Executable files**
A Linux file is executable if it contains instructions that can be directly interpreted by the operating system.They're also referred to as binaries or executables.

A shell script is a plain text file that can be interpreted by a shell.
📓**Working with Text Files, Networking & Archiving Commands**
 **➡ Viewing file contents**

 ```bash
>> cat command displays the contents of small files 
 
cat file_name
>>----------------------->>
more see only as many lines as will fit on your terminal window at once.
more file_name

less command displays the first page of the file
less file_name

>>----------------------->>
>>head will print the first 10 lines of a file
head usdoi.txt

>>Print only the first 3 lines of text from the file usdoi.txt
head -3 usdoi.txt

>>----------------------->>
>> tail will print the last 10 lines of the file usdoi.txt
tail usdoi.txt

>> Print the last 2 lines of the file usdoi.txt
tail -2 usdoi.txt

```
 
 **➡ Getting basic text file stats**
```bash
>>----------------------->>
>> wc to find the number of lines, words, and characters in a file
wc usdoi.txt

 152 1330 8121 usdoi.txt
 Nlines Nwords Nchar

>>count of lines
wc -l usdoi.txt

>>count of words
wc -w usdoi.txt

>>number of characters
wc -c usdoi.txt

>>----------------------->>
>>sort command to display the lines of a file sorted alphanumerically.

sort usdoi.txt

>>sort in reverse orde
sort -r usdoi.txt

>>----------------------->>
>> uniq  will drop any lines in the file that are identical
uniq zoo.txt
```
 
 **➡ Basic text wrangling: extracting lines and fields**

```
>>----------------------->>
>> grep command allows you to specify a pattern and search for lines within a file that match that pattern.

grep people usdoi.txt

-n	>> Along with the matching lines, also print the line numbers
-c	>> Get the count of matching lines
-i	>> Ignore the case of the text while matching
-v	>> Print all lines which do not contain the pattern
-w	>> Match only if the pattern matches whole words

print all the lines from the /etc/passwd file which do not contain the pattern login:
grep -v login /etc/passwd

>>----------------------->>
>>cut command allows you to view only specific fields from each line of text in a file.

>>cut with the -c option to view only the first two characters of each line:
cut -c -2 zoo.txt

>>view each line starting from the second character:
cut -c 2- zoo.txt

>>cut command can also be used to extract a field from a delimited file.

>>extract just the phone numbers for each person listed in the file using the -d (delimiter) and f (field) options as follows:

cut -d "," -f2 names_and_numbers.csv
```

 **➡ Basic text wrangling: merging lines as fields**
```bash
>>----------------------->>
>>paste command to view the two files merged together,.line-by-line, as columns delimited by a Tab character:

paste zoo.txt zoo_ages.txt

>>specify a comma , as delimeter
paste -d "," zoo.txt zoo_ages.txt
```
 ---
### A Brief Introduction to Networking

 **➡ Computer Networks ⬅️**

A **computer network** is a set of computers that are able to communicate with each other and share **resources** provided by **network nodes**.

> Examples of computer networks include Local Area Networks (LANs), Wide Area Networks (WANs), and the entire Internet. The Internet, or World Wide Web, is essentially a giant network of computer networks.

A network **resource** is any object, such as a file or document, which can be _identified_ by the network.

> An object is identifiable if it can be assigned a unique name and address that the network can use to identify and access it.

A **network node** is any device that participates in a network.

> A network can include any device which is not necessarily a computer but is part of the network’s infrastructure. Examples of network nodes include modems, network switches, hubs, and wifi hotspots.

 **➡ Hosts, Clients, and Servers ⬅️**

A **host** is a special type of node in a computer network - it is a computer that can function as a **server** or a **client** on a network.

A **server** is a host computer that is able to accept a connection from a **client** host and fulfill certain resource requests made by the client.

Many hosts can perform either role, acting as both client and server.

 **➡ Packets and Pings ⬅️**

A **network packet** is a formatted chunk of data that can be transmitted over a network.

Today's computer networks typically use communication protocols that are based on such packets of information. 
Every packet consists of two types of data: 
1. the **control information** data about how and where to deliver the payload
2. the **payload** is the message being sent.

The `ping` command works by sending special 'echo request' packets to a host and waiting for a response from the host.

 **➡ URLs and IP Addresses ⬅️**

IP stands for "Internet Protocol" which defines the format of data transmitted over the internet or a local network.

An **IP address** is a code used to uniquely identify any host on a network.

> An IP address can be used to establish a connection to a host and exchange packets with it, for example using the `ping` command. In addition to their payload, IP packets - a type of network packet that conforms to the Internet Protocol - contain the IP addresses of the source and destination hosts.

A **URL** (_Uniform Resource Locator_) known as a web address

> A URL uniquely identifies a web resource and enables access to that resource. Typically the resource that a URL points to is a web page, but it can also be used for tasks such as transferring files, sending emails, and accessing databases.

> For example, the URL to the Wikipedia page for URL is `https://en.wikipedia.org/wiki/URL`. Just like for a typical URL, its format indicates a protocol (`https`), a hostname (`en.wikipedia.org`), and a file name (`/wiki/URL`).

---

### Working with Networking Commands

 **➡ View configuration info about your network ⬅️**

A **hostname** is a name that is assigned to a computer or device on a network, and it is used to identify and communicate with that device.

To view the current hostname, run the command below:
 `hostname`

An **IP address** (Internet Protocol address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.

You can use the `-i` option to view the IP address of the host:

 `hostname -i`

**Display network interface configuration**

 `ifconfig` command is used to configure or display network interface parameters for a network.

To display the configuration of all network interfaces of your system, enter:

 `ifconfig`

To display the configuration of a particular device, such as the ethernet adapter `eth0`, enter:
 `ifconfig eth0`


`eth0` is usually the primary network interface that connects your server to the network.

 **➡ Test network connectivity ⬅️**

**Test connectivity to a host**

Use the `ping` command to check if `www.google.com` is reachable. 
The command keeps pinging data packets to server at `www.google.com` and prints the response it gets back. (Press `Ctrl`+`c` to stop pinging.)

 `ping www.google.com`

If you want to ping only a limited number of times, use `-c` option.
`ping -c 5 www.google.com`

**➡ View or download data from a server ⬅️**

**Transfer data from a server**
`curl` to access the file at the following URL and display the file's contents on your screen:

 `curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt`

To access the file at the given URL and also save it in your current working directory, use the `-O` option:
`curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt`

**Download file(s) from a URL**
`wget` command to download file
 `wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt`

---
### Archiving and Compressing Files
 **➡ File and folder archiving and compression ⬅️**

**Create and manage file archives**

The `tar` command allows you to pack multiple files and directories into a single archive file.

The following command creates an archive of the entire `/bin` directory and writes the archive to a single file named `bin.tar`.  

The options used are as follows:

|Option|Description|
|---|---|
|-c|Create new archive file|
|-v|Verbosely list files processed|
|-f|Archive file name|

 `tar -cvf newfile.tar /directory`
 `tar -cvf bin.tar /bin`



To see the list of files in the archive, use the `-t` option:
 `tar -tvf bin.tar`


To untar the archive or extract files from the archive, use the `-x` option:
 `tar -xvf bin.tar`


**Package and compress archive files**

The `zip` command allows you to compress files.

The following command creates a zip file named `config.zip` consisting of all the files with extension `.conf` in the `/etc` directory.
 
 `zip filname.zip /directory`

 `zip config.zip /etc/*.conf`

The **`-r`** option can be used to zip an entire directory.
 `zip -r bin.zip /bin`

**Extract, list, or test compressed files in a ZIP archive**

 `unzip` command allows you to extract files.

To list the files of the archive `config.zip`, enter the following:
 `unzip -l config.zip`


The following command extracts all the files in the archive `bin.zip`.
`-o` option to force overwrite in case you run the command more than once
`unzip -o bin.zip`







---
## W3 ❉ Introduction to Shell Scripting
### A Brief Introduction to Shell Variables
 **➡ shell variable ⬅️**

Shell variables offer a powerful way to store and later access or modify information such as numbers, character strings, and other data structures by name.
Consider the following example.


 `$ firstname=Jeff`
 `$ echo $firstname`
output  `Jeff`

to call variable
 `$ echo $variable`

 **➡ Reading user input into a shell variable at the command line ⬅️**

 another way to create a shell variable, using the `read` command.  
`$ read lastname`


on the command line, the shell waits for you to enter some text:
 `$ read lastname`  
 `Grossman`  
 
 `$ echo $lastname`  
 `Grossman`
 
 you can echo the values of multiple variables at once.
 `$ echo $firstname $lastname`  
 `Jeff Grossman`  

---
### Getting Started with Shell Scripting
 
 **➡ Create and execute a basic shell script ⬅️**
`#` Comments are not executed by the shell.

to run the shell file command to execute it:

 `bash greet.sh`

**➡ Using a shebang line ⬅️**
"shebang" is the first line in a script file in Unix-like operating systems that starts with 
`#!` followed by the path to the interpreter that the script should be run with. It's also known as a "hashbang" or "pound bang".

 ```bash
 #!/bin/bash
```
### Examples of Pipes

 **➡ pipes ⬅️**
pipes are commands in Linux which allow you to use the output of one command as the input of another.
![[Pasted image 20240209110539.jpg]]

Pipes `|` use the following format:
 `[command 1] | [command 2] | [command 3] ... | [command n]`

There is no limit to the number of times you can chain pipes in a row!

**Pipe examples**

**Combining commands**

Let's start with a commonly used example. Recall the following commands:

- `sort` - sorts the lines of text in a file and displays the result
- `uniq` - prints a text file with any consecutive, repeated lines collapsed to a single line

With the help of the pipe operator, you can combine these commands to print all the unique lines in a file.

Suppose you have the file `pets.txt` with the following contents:
 `$ cat pets.txt`
 `goldfish`
 `dog`
 `cat`
 `parrot`
 `dog`
`goldfish`
 `goldfish`

combining the two commands in the correct order - by first using `sort` then `uniq` - you get back:
Since `sort` sorts all identical items consecutively, and `uniq` removes all consecutive duplicates, combining the commands prints only the unique lines from `pets.txt`

 `$ sort pets.txt | uniq`
 `cat`
 `dog`
 `goldfish`
 `parrot`

**Applying a command to strings and files**

Some commands such as `tr` only accept _standard input_ - normally text entered from your keyboard - but not strings or filenames.

 `tr` (translate) - replaces characters in input text
 `tr [OPTIONS] [target characters] [replacement characters]`

we can use piping to apply the command to strings and file contents.

With strings, you can use `echo` in combination with `tr` to replace all the vowels in a string with underscores `_`:

1. `$ echo "Linux and shell scripting are awesome\!" | tr "aeiou" "_"`
2. `L_n_x _nd sh_ll scr_pt_ng _r_ _w_s_m_!`

to replace all the _consonants_ (any letter that is not a vowel) with an underscore - you can use the `-c` option:

 `$ echo "Linux and shell scripting are awesome\!" | tr -c "aeiou" "_"`
 `_i_u__a_____e______i__i___a_e_a_e_o_e_`

With files, you can use `cat` in combination with `tr` to change all of the text in a file to uppercase as follows:

 `$ cat pets.txt | tr "[a-z]" "[A-Z]"`
 `GOLDFISH`
 `DOG`
 `CAT`
 `PARROT`
 `DOG`
 `GOLDFISH`
 `GOLDFISH`
 
 **Extracting information from JSON Files:**
use this json file to get the current price of Bitcoin (BTC) in USD, by using grep command.
`Bitcoinprice.txt` file

```json
{
  "coin": {
    "id": "bitcoin",
    "icon": "https://static.coinstats.app/coins/Bitcoin6l39t.png",
    "name": "Bitcoin",
    "symbol": "BTC",
    "rank": 1,
    "price": 57907.78008618953,
    "priceBtc": 1,
    "volume": 48430621052.9856,
    "marketCap": 1093175428640.1146,
    "availableSupply": 18877868,
    "totalSupply": 21000000,
    "priceChange1h": -0.19,
    "priceChange1d": -0.4,
    "priceChange1w": -9.36,
    "websiteUrl": "http://www.bitcoin.org",
    "twitterUrl": "https://twitter.com/bitcoin",
    "exp": [
      "https://blockchair.com/bitcoin/",
      "https://btc.com/",
      "https://btc.tokenview.com/"
    ]
  }
}
```


 JSON field you want to grab here is `"price": [numbers].[numbers]"`. 
 
 use `grep` command to extract it from the JSON text:
 `grep -oE "\"price\"\s*:\s*[0-9]*?\.[0-9]*"`


- `-o` tells `grep` to _only_ return the matching portion
- `-E` tells `grep` to be able to use extended regex symbols such as `?`
- `\"price\"` matches the string `"price"`
- `\s*` matches any number (including 0) of whitespace (`\s`) characters
- `:` matches `:`
- `[0-9]*` matches any number of digits (from 0 to 9)
- `?\.` optionally matches a `.`


Use the cat command to get the output of the JSON file and pipe it with the grep command to get the required output.

 `cat Bitcoinprice.txt | grep -oE "\"price\"\s*:\s*[0-9]*?\.[0-9]*"`

### Examples of Bash Shell Features
 **➡ Metacharacters ⬅️**

**Metacharacters** are characters having special meaning that the shell interprets as instructions.

|Metacharacter|Meaning|
|---|---|
|`#`|Precedes a comment|
|`;`|Command separator|
|`*`|Filename expansion wildcard|
|`?`|Single character wildcard in filename expansion|

**Pound `#`**

The pound `#` metacharacter is used to represent comments in shell scripts or configuration files. 

 `#!/bin/bash`
 `# This is a comment`

**Semicolon `;`**

The semicolon `;` metacharacter is used to separate multiple commands on a single command line. 

 `$ echo "Hello, "; echo "world!"`
 `Hello,`
 `world!`

**Asterisk `*`**

The asterisk `*` metacharacter is used as a wildcard character to represent any sequence of characters, including none.
 `ls *.txt`


`*.txt` is a wildcard pattern that matches any file in the current directory with a `.txt` extension. 

**Question mark `?`**
`?` metacharacter is used as a wildcard character to represent any single character.
 `ls file?.txt`

`file?.txt` is a wildcard pattern that matches any file in the current directory with a name starting with `file`, followed by any single character, and ending with the `.txt` extension.

**➡ Quoting ⬅️**

**Quoting** is a mechanism that allows you to remove the special meaning of characters, spaces, or other metacharacters in a command argument or shell script. 
You use quoting when you want the shell to interpret characters literally.

|Symbol|Meaning|
|---|---|
|`\`|Escape metacharacter interpretation|
|`" "`|Interpret metacharacters within string|
|`' '`|Escape all metacharacters within string|

**Backslash `\`**

The backslash character is used as an escape character. 

For example, if you have a file with spaces in its name, you can use backslashes followed by a space to handle those spaces literally:

 `touch file\ with\ space.txt`

**Double quotes `" "`**

When a string is enclosed in double quotes, most characters are interpreted literally, 
but metacharacters are interpreted according to their special meaning. 

For example, you can access variable values using the dollar `$` character:
 `$ echo "Hello $USER"`
 `Hello <username>`

**Single quotes `' '`**

When a string is enclosed in single quotes, all characters and metacharacters enclosed within the quotes are interpreted literally. Single quotes alter the above example to produce the following output:


1. `$ echo 'Hello $USER'`
2. `Hello $USER`
**➡ Input/Output redirection ⬅️**

|Symbol|Meaning|
|---|---|
|`>`|Redirect output to file, overwrite|
|`>>`|Redirect output to file, append|
|`2>`|Redirect standard error to file, overwrite|
|`2>>`|Redirect standard error to file, append|
|`<`|Redirect file contents to standard input|

**Input/output (IO) redirection** is the process of directing the flow of data between a program and its input/output sources.

By default, a program reads input from _standard input_, the keyboard, and writes output to _standard output_, the terminal. However, using IO redirection, you can redirect a program's input or output to or from a file or another program.

**Redirect output `>`**

This symbol is used to redirect the standard output of a command to a specified file.

> `ls > files.txt` will create a file called `files.txt` if it doesn't exist, and write the output of the `ls` command to it.

> Warning: When the file already exists, the output overwrites all of the file's contents!


**Redirect and append output `>>`**

This notation is used to redirect and append the output of a command to the end of a file. For example,

> `ls >> files.txt` appends the output of the `ls` command to the end of file `files.txt`, and preserves any content that already existed in the file.

**Redirect standard output `2>`**

This notation is used to redirect the standard error output of a command to a file. For example, if you run the ls command on a non-existing directory as follows,

> `ls non-existent-directory 2> error.txt` the shell will create a file called `error.txt` if it doesn't exist, and redirect the error output of the `ls` command to the file.

> Warning: When the file already exists, the error message overwrites all of the file's contents!

**Append standard error `2>>`**

This symbol redirects the standard error output of a command and appends the error message to the end of a file without overwriting its contents.

> `ls non-existent-directory 2>> error.txt` will append the error output of the `ls` command to the end of the `error.txt` file.

**Redirect input `<`**

This symbol is used to redirect the standard input of a command from a file or another command. For example,

> `sort < data.txt` will `sort` the contents of the `data.txt` file.

**➡ Command Substitution ⬅️**

**Command substitution** allows you to run command and use its output as a component of another command's argument. Command substitution is denoted by enclosing a command in either backticks (**`command`**) or using the `$()` syntax. 

When the encapsulate command is executed, its output is substituted in place, and it can be used as an argument within another command. This is particularly useful for automating tasks that require the use of a command's output as input for another command.

For example, you could store the path to your current directory in a variable by applying command substitution on the `pwd` command, then move to another directory, and finally return to your original directory by invoking the `cd` command on the variable you stored, as follows:

 `$ here=$(pwd)`
 `$ cd path_to_some_other_directory`
`$ cd $here`

**➡ Command Line Arguments ⬅️**

**Command line arguments** are additional inputs that can be passed to a program when the program is run from a command line interface. These arguments are specified after the name of the program, and they can be used to modify the behavior of the program, provide input data, or provide output locations. Command line arguments are used to pass arguments to a shell script.

For example, the following command provides two arguments, arg1, and arg2, that can be accessed from within your Bash script:

 `$ ./MyBashScript.sh arg1 arg2`


### Introduction to Advanced Bash Scripting

---

**1. Conditionals:**

Conditionals, also known as if statements, enable executing commands based on specific conditions.

```bash
if [ condition ]; 
then
    statement_block_1  
else
    statement_block_2  
fi
```

**Tips:**
- Always use spaces within square brackets `[ ]`.
- Each `if` block must be paired with `fi`.
- Optionally use an `else` block for handling false conditions.

**Example:**
```bash
# [[ $# == 2 ]] # integer comparisons in the condition
if [ condition1 ] && [ condition2 ] #"and" operator
if [ condition1 ] || [ condition2 ] #"or" operator

# >>>>>>>>>>>>>>>>>>>>

if [[ $# == 2 ]]; 
then
  echo "number of arguments is equal to 2"
else
  echo "number of arguments is not equal to 2"
fi
```

**2. Logical Operators:**

Logical operators facilitate comparisons within condition blocks.

**Operators:**
- `==`: Equal to
- `!=`: Not equal to
- `<=` or `-le`: Less than or equal to

**Examples:**
```bash
[a == 2]
[a != 2]
[a <= 3]
[ $a -le $b ]
```

**3. Arithmetic Calculations:**

Perform integer arithmetic using `$(())`.

**Operators:**
- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division

**Example:**
```bash
echo $((3+2))
# >>>>>>>>>>>>>>>>>>>>
a=3
b=2
c=$(($a+$b))
echo $c
```

**4. Arrays:**

Arrays are space-delimited lists enclosed in parentheses.

**Creation:**
```bash
my_array=(1 2 "three" "four" 5)  

# >>>>>>>>>>>>>>>>>>>>
declare -a empty_array
```

**Manipulation:**
```bash
# add items to array
my_array+=("six")
my_array+=(7)
```

**print Elements:**
```bash
echo ${my_array[0]}    # First element
echo ${my_array[2]}    # Third element
echo ${my_array[@]}    # All elements
```

**5. For Loops:**

For loops iterate over elements or indices of an array.

**Examples:**
```bash
for item in ${my_array[@]}; do
  echo $item
done
```
or
```bash
for i in ${!my_array[@]}; do
  echo ${my_array[$i]}
done
```

```bash
N=6
for (( i=0; i<=$N; i++ )); do
  echo $i
done
```

### Scheduling Jobs using crontab

**Introduction:**
Cron is a system daemon designed for executing specified tasks in the background at scheduled times. Crontab files are used to manage these scheduled tasks and are edited using the `crontab` command.

**Syntax Overview:**
A crontab file comprises lines with five time-and-date fields, followed by a command, and terminated with a newline character (`\n`). These fields are delimited by spaces.

**Time-and-Date Fields:**

1. **Minute Field:**
   - Allowed Values: 0-59

2. **Hour Field:**
   - Allowed Values: 0-23 (0 denotes midnight)

3. **Day Field:**
   - Allowed Values: 1-31

4. **Month Field:**
   - Allowed Values: 1-12

5. **Weekday Field:**
   - Allowed Values: 0-6 (0 represents Sunday)

**Examples:**
```plaintext
Minute Hour Day Month Weekday command_to_execute

* * * * * * command_to_execute
```
- To run a command every day at 3:30 AM:
```plaintext
30 3 * * * command_to_execute
```

- To schedule a task to run every Monday at 8:00 PM:
```plaintext
0 20 * * 1 command_to_execute
```

The `-l` option of the `crontab` command prints the current crontab.
 `crontab -l`

 **Adding a Job to Crontab**
To add a cron job, follow these steps:
1. Open your crontab file for editing:
```
crontab -e
```

2. Scroll down to the end of the file using the arrow keys.
3. Add the following line at the end of the crontab file:
```
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```

   This job runs the `echo` command at 9:00 p.m. every day, and the output is redirected to `/tmp/echo.txt`.

4. Press `Ctrl + x` to save the changes.
5. Press `y` to confirm.
6. Press `Enter` to exit the editor.
7. Verify if the job is added to the crontab:
```
crontab -l
```

   You should see the newly added job in the output.

**Scheduling a Shell Script**

Follow these steps to schedule a shell script:

1. Create a new file named `diskusage.sh` using the menu on the lab screen (`File -> New File`).

2. Save the following commands into the shell script:
   ```bash
   #! /bin/bash
   # Print the current date time
   date
   # Print the disk free statistics
   df -h
   ```

3. Save the file using the `File -> Save` menu option.
4. Verify that the script is working:
```bash
chmod u+x diskusage.sh
./diskusage.sh
```

   The script should print the current timestamp and the disk usage stats.
5. Edit the crontab:
```
crontab -e
```

6. Add the following line to the end of the file:
```
0 0 * * * /home/project/diskusage.sh >> /home/project/diskusage.log
```

   This schedules the script to run every day at midnight (0:00), and the output is appended to `/home/project/diskusage.log`.

7. Press `Ctrl + x` to save the changes.
8. Press `y` to confirm.
9. Press `Enter` to exit the editor.
10. Check if the job is added to the crontab:
```
crontab -l
```

**Remove the current crontab**
To remove the current crontab, use the `-r` option with the `crontab` command:

```bash
crontab -r
```

Caution: This command will remove all your cron jobs. Exercise caution, especially on production servers.

After executing the command, you can verify if your crontab is removed by checking for its contents:

```bash
crontab -l
```



## W4 ❉ Final Project

