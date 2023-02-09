# Q5. Write a python program to add items from another set to the current set. thisset ={"Java", "Python", "SQL"}
thisset={"Java","Python","SQL"}
otherset={"C","C++","javascript"}
otherset.discard("C++")
thisset.add("C++")
print(thisset)
print(otherset)