import json
class StudentSystem:
    def __init__(n):
        n.file = "students.json"
        n.data = n.load()
    def load(n):
        try:
            with open(n.file, "r") as f:
                return json.load(f)
        except:
            return []
    def save(n):
        with open(n.file, "w") as f:
            json.dump(n.data, f, indent=4)
    def add(n):
        id = input("Student ID: ")
        name = input("Student Name: ")
        age = input("Age: ")
        course = input("Course: ")
        n.data.append({
            "id": id,
            "name": name,
            "age": age,
            "course": course
        })
        n.save()
        print("Record Added")
    def show(n):
        if len(n.data) == 0:
            print("No Data")
            return
        print("\nID\tName\tAge\tCourse")
        for i in n.data:
            print(i["id"], "\t", i["name"], "\t", i["age"], "\t", i["course"])
    def search(n):
        id = input("Enter ID: ")
        for i in n.data:
            if i["id"] == id:
                print(i)
                return
        print("Record Not Found")
    def update(n):
        id = input("Enter ID: ")
        for i in n.data:
            if i["id"] == id:
                i["name"] = input("New Name: ")
                i["age"] = input("New Age: ")
                i["course"] = input("New Course: ")
                n.save()
                print("Record Updated")
                return
        print("Record Not Found")
    def delete(n):
        id = input("Enter ID: ")
        for i in n.data:
            if i["id"] == id:
                n.data.remove(i)
                n.save()
                print("Record Deleted")
                return
        print("Record Not Found")
obj = StudentSystem()
while True:
    print("\n--- Student Management System ---")
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")
    ch = input("Enter Choice: ")
    if ch == "1":
        obj.add()
    elif ch == "2":
        obj.show()
    elif ch == "3":
        obj.search()
    elif ch == "4":
        obj.update()
    elif ch == "5":
        obj.delete()
    elif ch == "6":
        print("Program Closed")
        break
    else:
        print("Wrong Choice")