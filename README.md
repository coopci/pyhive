pyhive
======

hive related python code


HiveSerdeWriter.py 
    This lib can be used to generate data files which are loadable by hive TextFile and org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe.
    Use python primitive types for hive primitive type.
    Use python list for hive array.
    Use python dict for hive map.
    Use class HiveStruct for hvie struct.
    Use class HiveRow for a hive row.
    
    See __main__ for how to use this lib.
