#dictonary in python
marks = {
    "nency" : 98,
    "niyati" : 96,
    "vraj": 92
}
print(marks , type(marks))
print(marks["vraj"])

#methods of dict
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"nency":97,"dev":97.56})
print(marks)
print(marks.get("nency"))
print(marks.pop("niyati"))#remove niyati's key and returns its value
print(marks)
