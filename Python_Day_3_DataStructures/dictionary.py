thisdict={"key1":"Android","key2":"Ios"}
print(thisdict)
print(len(thisdict))
print(type(thisdict))
print(thisdict.get("key1"))
print(thisdict.keys())
print(thisdict.values())
thisdict["key3"]="Apple"
print(thisdict)
thisdict["key1"]="c"
print(thisdict)
thisdict.pop("key1")
print(thisdict)
thisdict.clear()
print(thisdict)

del thisdict
print(thisdict)