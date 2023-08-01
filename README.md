# Berta Api Tools

## Config Vector Tool
```
$ python config_vector_tool.py -h
usage: config_vector_tool.py [options]

Process Config Vectors

positional arguments:
  {add,delete,update}   Config Vector Actions Supported

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Berta Server URL with authentication: https://user:password@ra-berta.jf.intel.com
  -p PATH, --path PATH  Config Vector CSV Path
```

Sample command line:
```
$ python configvector_tool.py add -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vector_sample.csv
$ python configvector_tool.py delete -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vector_sample.csv
$ python configvector_tool.py update -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vector_sample.csv
```
