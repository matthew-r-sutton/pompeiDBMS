def generate_results_table(query_dict_list):
    query_dict_list
    print_results(query_dict_list):
    print('---')
    for dict in query_dict_list:
        print(dict['name'],dict['operator'].get(),dict['query'].get())
    print('---')
