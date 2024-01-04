# Berta Api Tools

## Config Vector Tool

### Usage:
```
$ python config_vector_tool.py -h

usage: config_vector_tool.py [options]

Process Config Vectors

positional arguments:
  {add,delete,update,get}
                        Config Vector Actions Supported

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Berta Server URL with authentication: https://user:password@ra-berta.jf.intel.com
  -p PATH, --path PATH  Config Vector CSV Path
  -c CONFIGS_NAME, --configsname CONFIGS_NAME
                        Optional Choice: get target configs, can be one/more(split by ',') [Name] [ID] [Prefix] or [RE Expression]
```
### Sample command line:
```
$ python config_vector_tool.py add -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vector_sample.csv
$ python config_vector_tool.py delete -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vector_sample.csv
$ python config_vector_tool.py update -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vector_sample.csv
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_vectors_configs.csv
```
### Get file.csv command:
```
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_all.csv
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c 57
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c 57,58,59
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c "val vmra"
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c "val vmra.*"
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c "val vmra full_nfv","val vmra basic",""val vmra reg_dc"
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c "val vmra full_nfv (crio)(ra-proxy)"
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c "val vmra full_nfv (crio)(ra-proxy)","val vmra basic (redeploy)(ra-proxy)","val vmra reg_dc (ra-proxy)"
$ python config_vector_tool.py get -u https://xxx:xxxxx@ra-berta.jf.intel.com -p config_match.csv -c "(docker)(no_sgx)(ra-proxy)"
```

### Reference api
```
https://cspv-berta.sh.intel.com/docs/api.html

show_config_vectors()
show_config_vectors_configs()
```
