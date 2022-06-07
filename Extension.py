s=input("Input the Filename:")

li=list(s.split("."))

s1=li[1]

myDict= {
    "c": "C Program",
    "CPP": "C++ Program",
    "java": "Java Program",
    "py": "python",
    "js": "Java Script",
    "kt": "Kotlin",
    "swift": "Swift"
    }

print(myDict[s1])
      
