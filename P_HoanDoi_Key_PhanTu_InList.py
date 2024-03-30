def hoan_doi(dictionary):
    new_dict = {value: key for key, value in dictionary.items()}  # Sử dụng dictionary comprehension để tạo dictionary mới bằng cách hoán đổi giá trị và key của dictionary đầu vào
    return new_dict if len(new_dict) == len(dictionary) else None  # Trả về new_dict nếu không có key nào bị trùng, ngược lại trả về None

# Ví dụ sử dụng:
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = hoan_doi(my_dict)
print("Dictionary mới sau khi hoán đổi: ", result)

my_dict = {'a': 1, 'b': 2, 'c': 2}
result = hoan_doi(my_dict)
print("Dictionary mới sau khi hoán đổi: ", result)
