def Delete_table(doc, table_index):
  doc.tables[table_index]._element.getparent().remove(doc.tables[table_index]._element)
  return True
