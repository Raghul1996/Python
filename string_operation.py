def resume(first, second, parent, city, phone, start, strfind, string1):
   first=first.strip().capitalize()
   print(first,end=" ")
   second=second.strip().capitalize()
   print(second,end=" ")
   parent=parent.strip().capitalize()
   print(parent,end=" ")
   city=city.strip()
   print(city)
   print(phone.isnumeric())
   print(phone.startswith(start.strip()))
   strfind=strfind.strip()
   print(first.count(strfind)+second.count(strfind)+parent.count(strfind)+city.count(strfind))
   print(string1.split())
   print(city.find(strfind))
#resume("   rryy "," lastname","father   ","city","phone","start","y","any,sentence")
resume("    nick","      cage","     actor","     chicago","     8634871690"," 86"," o"," the world is a better place")