from utils import open_operations_json, numbers, sort_dict_by_date, last_five_count

def main():
    number = 5
    new_json = open_operations_json()
    executed = numbers(new_json)
    list_sort = sort_dict_by_date(executed)
    print(last_five_count(list_sort, number))

if __name__ == "__main__":
    main()