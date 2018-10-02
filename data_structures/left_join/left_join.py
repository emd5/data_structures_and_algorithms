from .hash_table import HashTable


def left_join(ht1, ht2):
    """This method accepts two hash tables and left joins two tables, returns a list of left join tables"""
    join_list = []

    if ht1 is not None:
        join_list.append(ht1)

    # for i in join_list:
    #     if join_list[i] is None:
    #         join_list.pop(join_list[i])

    return join_list
