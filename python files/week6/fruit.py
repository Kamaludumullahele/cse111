def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f"fruit list:{fruit_list}")
  fruit_list.append("orenge")
  print(f"fruit list:{fruit_list}")
  i = fruit_list.index("apple")
  fruit_list.insert(i,"cherry")
  print(f"fruit list: {fruit_list}")
  fruit_list.remove("banana")
  print(f"fruit list: {fruit_list}")
  item = fruit_list.pop()
  print(item)
  print(f"fruit list: {fruit_list}")
  fruit_list.sort()
  print(f"sorted list: {fruit_list}")
  fruit_list.clear()
  print(f"Cleared list:{fruit_list}")
  

  


if __name__ == "__main__":
  main()