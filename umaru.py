
import json


# JSON string
a = '{"name": "Bob", "languages": "English", "subject": "Math"}'

# deserializes into dict
# and returns dict.
y = json.loads(a)

print("JSON string is = ", y)
print()



