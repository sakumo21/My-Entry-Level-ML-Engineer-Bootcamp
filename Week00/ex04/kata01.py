kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

key_list = list(kata.keys())
print(f"{key_list[0]} was created by {kata['Python']}",
      f"{key_list[1]} was created by {kata['Ruby']}",
      f"{key_list[2]} was created by {kata['PHP']}",
      sep='\n')