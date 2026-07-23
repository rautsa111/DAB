import dlt

@dlt.table(
    name = 'test'
)
def test():
  return spark.range(10)