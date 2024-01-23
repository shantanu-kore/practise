student_name=input("enter your name:")
physics=int(input("enter physics marks:"))
chemistry=int(input("enter chemistry marks:"))
maths=int(input("enter maths marks:"))
total=physics+chemistry+maths
pcm=total/3
print("[",student_name,"]obtained",pcm,"% of  marks in pcm")
print("physics:[", physics,"%] chemistry:[", chemistry,"%], maths:[", maths,"%]")
print("total:[",pcm,'%]')