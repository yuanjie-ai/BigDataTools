from pyspark.sql.types import StructType, StructField
def get_schema(num_col_names, str_col_names):
    assert isinstance(num_col_names[0], str)
    assert isinstance(str_col_names[0], str)
    _struct = StructType()
    for i in num_col_names:
        _struct.add(i, FloatType())
    for i in str_col_names:
        _struct.add(i, StringType())
    return _struct
