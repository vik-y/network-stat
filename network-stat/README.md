### Instructions to Run 

In one terminal
```sh
python main.py 
```

Open another terminal in the same directory and type:
```sh
tail -f log.txt
# This will keep printing the logs which will help you for debugging.
```

### Info about understanding the code structure
```
util.py
```
This file has all the data collection functions. 

```
main.py
```
Currently, this is used only to test if the functions written in util.py 
are working properly or not. Right now there is no mechanism in place to
upload the collected data anywhere. 

