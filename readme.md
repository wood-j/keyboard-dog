# Keyboard Dog

This project is a python application to log computer keyboard input background

## Environment

- Python3.7

```bash
pip3 install -r requirements.txt
```

## Run

Use following command to run application:

```bash
python3 main.py
```

Application will keep running forever and print keyboard input:

```log
Connected to pydev debugger (build 181.5087.37)
2020-11-27 09:44:23 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 20： dog stared
2020-11-27 09:44:30 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 11： on_press: 'y'
2020-11-27 09:44:30 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 15： on_release: 'y'
2020-11-27 09:44:31 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 11： on_press: 't'
2020-11-27 09:44:32 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 11： on_press: 'h'
2020-11-27 09:44:32 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 15： on_release: 't'
2020-11-27 09:44:32 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 15： on_release: 'h'
2020-11-27 09:44:32 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 11： on_press: 'i'
2020-11-27 09:44:32 DEBUG File "/home/wood/project/keyboard-dog/main.py", line 15： on_release: 'i'
```

## Log

All log at `data/logs/`