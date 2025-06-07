 # Coding style for this project

 ## Use zip to Process Iterators in Parallel
 Often in Python you find yourself with many lists of related objects. 
 
 The zip generator yields tuples containing the next value from each iterator. These 
tuples can be unpacked directly within a for statement. The resulting 
code is much cleaner than the code for indexing into multiple lists:
```python
    for detected, projected in zip(charucoCorners, imgPoints_proj):
        x1, y1 = int(detected[0][0]), int(detected[0][1])  # Detected
        x2, y2 = int(projected[0][0]), int(projected[0][1])  # Projected
```
zip consumes the iterators it wraps one item at a time, which means 
it can be used with infinitely long inputs without risk of a program 
using too much memory and crashing.

## Use print statements but not for output
Yeah, yeah, print statement... blah blah... linters... blah blah... bad practice... blah blah... logging... blah blah

Feel free to mindlessly use print statements when contributing to this project. You may already see a lot of print statements. But at the same time, feel free to remove any print statement. Removing a print statement will not take away any of the features from this project. A feature shall not be dependent on a print statement. Any addition or removal of print statements by your commits will be ignored when your pull request is reviewed. What does that mean? Don't show your result through a print statement. If your result is a numpy array, save it as an array or image; if your result is some text, dump it in a json (see Why Json?)file. If you want to print your result alongside saving it, feel free, just be aware that any print statements in this project shall be assumed as debuggers and may be removed in any future commit by any contributor. 

## Why Json?
JSON data in python is essentially a dictionary (at least they are interchangeable, there are some minor differences with the formatting). Have you tried saving a dictionary to a simple text file?
```python
my_data = {
    'a': [1, 2, 3],
    'b': {'foo': 'bar',
          'baz': [4, 5, 6]}
    }

with open('test_file.txt', 'w') as file:
    file.write(my_data)
```
This is not possible because Python expects a string that it can write to a file. It doesn't know how to turn a dictionary into something it can write to a file.

But, maybe you then do this instead:
```python
my_data = {
    "a": [1, 2, 3],
    "b": {"foo": "bar",
          "baz": [4, 5, 6]}
    }

with open('test_file.txt', 'w') as file:
    # cast my_data to a string first
    file.write(str(my_data))
```
And it works. But what if you want to read that file?
```python
with open('test_file.txt', 'r') as file:
    read_data = file.read()
```
Now you have a problem, because your output is this string:
```python
"{'a': [1, 2, 3], 'b': {'foo': 'bar', 'baz': [4, 5, 6]}}"
```
How do you convert a string into a dictionary? This here doesn't work:
```python
with open('test_file.txt', 'r') as file:
    read_data = dict(file.read())
```
Python by itself does not know how to convert a string into a dictionary. For that you need JSON. Also it makes sure that you meet all the conventions of the JSON format so that you can exchange data between different languages (e.g. from Python to JavaScript).

The other thing is, if you have a .txt file, how would anybody know that this file contains a data structure without opening the file? If the file extension says "JSON" everybody knows how to interpret the data. Same with .XML, .HTML etc.

Say you do not want to save any dictionary. You just want to save 
```json
        "Eye": [
            eyeX,
            eyeY,
            eyeZ
        ], <br/>
        "Lookat": [
            centerX,
            centerY,
            centerZ
        ], <br/>
        "Up": [
            upX,
            upY,
            upZ
        ],
```
as three lists in a file. If you want to save or load a primitive data type, such as int or float or str, sure, `ConfigParser` may be a good decision. But a ConfigParser does not have built-in functionality to read data as Python List. So even for a simple txt file you will have to write custom code to read data as a list. [cite](https://buklijas.info/blog/2018/01/01/always-start-with-simple-solution/)