# -*- coding: utf-8 -*-
class HiveRow(object):
    def __init__(self):
        self._cols = {}
        self._cells = []
        pass
    def setCols(self, cols):
        self._cols = {}
        for i, v in enumerate(cols):
            self._cols[v] = i
        self._cells = [None] * len(self._cols.keys())
    def getCells(self):
        return self._cells
    def setCell(self, colname, value):
        i = self._cols[colname]
        self._cells[i] = value
class HiveStruct(object):
    def __init__(self):
        self._fields = {}
        self._values = []
        pass
    def setFields(self, fields):
        self._fields = {}
        for i, v in enumerate(fields):
            self._fields[v] = i
        self._values = [None] * len(self._fields.keys())
    def getValues(self):
        return self._values
    def setValue(self, fieldname, value):
        i = self._fields[fieldname]
        self._values[i] = value    
        
class HiveSerdeWriter():
    def __init__(self):
        
        self.field_terminator = '\001'
        self.collection_item_terminator = '\002'
        self.map_key_terminator = '\003'
        self.line_terminator = '\n'
        self.unicode_encoding = 'utf-8'
    def dumps(self, obj):
        ret = ''
        if type(obj) == HiveRow:
            ret = self.field_terminator.join( [self.dumps(cell) for cell in obj.getCells()] ) 
            ret += self.line_terminator
        elif type(obj) == HiveStruct:
            ret = self.collection_item_terminator.join( [self.dumps(v) for v in obj.getValues()] )
        elif type(obj) == type([]):
            ret = self.collection_item_terminator.join( [self.dumps(ele) for ele in obj] )
        elif type(obj) == type({}):
            ret = self.collection_item_terminator.join( [self.dumps(k) + self.map_key_terminator + self.dumps(v) for k, v in obj.items()] )
        elif type(obj) == unicode:
            return obj.encode(self.unicode_encoding)
        elif obj == None:
            return ''
         
        else:
            ret = str(obj)
        return ret
        
if __name__ == "__main__":
    hr = HiveRow()
    hs = HiveStruct()
    print type(hr) == HiveRow
    print type(hs)
    hs.setFields(["field1", "field2"])
    hs.setValue("field1", "hs-value1")
    hs.setValue("field2", u"汉字")
    writer = HiveSerdeWriter()
    hr.setCols(["col1", "col2", "col3", "col4", "col5"])
    hr.setCell("col1", 123)
    hr.setCell("col2", "afgafdg")
    hr.setCell("col3", [123,24234,456])
    hr.setCell("col4", {"key1":"value1"})
    hr.setCell("col5", hs)
    s = writer.dumps(hr)
    f = open("hive-out", "wb")
    f.write(s)
    f.close()