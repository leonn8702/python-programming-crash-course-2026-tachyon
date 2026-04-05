# enumerate() ফাংশনটি ব্যবহার করলে আমরা একই সাথে index (ক্রমসংখ্যা) এবং value (মান) — দুটোই পেতে পারি।
students = ["Abdullah", "Tasnim", "Fahim", "Ahmed"]
for i, std in enumerate(students):
    print(i)
    print(std)