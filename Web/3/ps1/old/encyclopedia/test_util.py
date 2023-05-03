# import util 

# print(dir(util))

from util import get_entry, list_entries, save_entry

# import inspect
# lines = inspect.getsource(get_entry)
# print(lines)

entries = list_entries()

entries = util.list_entries()
print(entries)

title = "New Entry"
content = """
# Here comes the title
## Here comes the content

### Table 
| Header | Header |
| ------ | ------ |
| Cell | Cell |
| Cell | Cell |

### List
- Item 1
- Item 2
- Item 3

### Code
```python
import os
print(os.path.abspath(__file__))
```

### Link
[Google](https://www.google.com)


"""
util.save_entry(title, content)

c = util.get_entry("New Entry")
print(c)

