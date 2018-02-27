
def get_schema(num_col_names, str_col_names):
    assert isinstance(num_col_names[0], str)
    assert isinstance(str_col_names[0], str)
    struct = StructType()
    for i in num_col_names:
        struct.add(i, FloatType())
    for i in str_col_names:
        struct.add(i, StringType())
    return struct
