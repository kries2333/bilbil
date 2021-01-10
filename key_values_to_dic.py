def key_values_to_dic(key_values_):
    """
    将键值对转换为字典形式
    :param key_values_:
    :return:
    """
    key_values_dic_ = {}
    for line in key_values_.split(";"):
        line = line.strip()
        if not line:
            continue
        try:
            key, value = line.split("=", 1)
            key = key.strip()
            key_values_dic_[key] = value
        except ValueError:
            print("ERROR: 键值对错误，转换失败", line)
    return key_values_dic_