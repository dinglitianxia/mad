import xmlrpc.client as xmlrpclib
import argparse
import sys
import csv

HEADER = ['config_id', 'config_vector_name', 'config_vector_comment', 'config_vector_value']

class ConfigVectorTool(object):

    def __init__(self, server_url, csv_path):
        self.process_count = 0
        self.server_url = server_url
        self.server = xmlrpclib.Server(server_url, allow_none=True)
        self.csv_path = csv_path
    
    def config_vector_get(self, config_vector_name, config_id):
        config_vectors_details = self.server.show_config_vectors(config_vector_name, config_id)
        return config_vectors_details

    def _config_vector_add(self):
        print("Adding new config vectors from %s" % (self.csv_path))
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['config_id'] and row['config_vector_name'] and row['config_vector_value']:
                    existing_vector = self.config_vector_get(row['config_vector_name'], row['config_id'])
                    # print(existing_vector)
                    if len(existing_vector) != 0:
                        print("%s already exists in Config id %s, skip" % (row['config_vector_name'], row['config_id']))
                        continue
                    else:
                        try:
                            new_vector_id = self.server.add_config_vector(row['config_vector_name'], row['config_vector_comment'], row['config_vector_value'], row['config_id'])
                        except Exception as e:
                            print("Unsuccessful add call: ", row)
                            sys.exit(1)
                        else:
                            print('Added: ', row, ', config_vector_id: ', new_vector_id)
                            self.process_count += 1
                else:
                    print("Parameters missing in csv, exiting")
                    sys.exit(1)
        print("%d config vectors added" % self.process_count)

    def _config_vector_delete(self):
        print("Deleting config vectors from %s" % (self.csv_path))
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['config_id'] and row['config_vector_name']:
                    existing_vector = self.config_vector_get(row['config_vector_name'], row['config_id'])
                    if len(existing_vector) == 0:
                        print("%s doesn't exist in Config id %s, skip" % (row['config_vector_name'], row['config_id']))
                        continue
                    else:
                        try:
                            for vector in existing_vector:
                                self.server.delete_config_vectors(vector['id'])
                        except Exception as e:
                            print("Unsuccessful delete call: ", row)
                            sys.exit(1)
                        else:
                            print('Deleted: ', row)
                            self.process_count += 1
                else:
                    print("Parameters missing in csv, exiting")
                    sys.exit(1)
        print("%d config vectors deleted" % self.process_count)


    def _config_vector_update(self):
        print("Updating value/comment for config vectors from %s" % (self.csv_path))
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['config_id'] and row['config_vector_name'] and (row['config_vector_value'] or row['config_vector_comment']):
                    existing_vector = self.config_vector_get(row['config_vector_name'], row['config_id'])
                    if len(existing_vector) == 0:
                        print("%s doesn't exist in Config id %s, skip" % (row['config_vector_name'], row['config_id']))
                        continue
                    else:
                        try:
                            for vector in existing_vector:
                                _ = self.server.update_task_vector(vector['id'], None, row['config_vector_comment'], row['config_vector_value'], None, None)
                        except Exception as e:
                            print("Unsuccessful update call: ", row)
                            sys.exit(1)
                        else:
                            print('Updated: ', row)
                            self.process_count += 1
                else:
                    print("Parameters missing in csv, exiting")
                    sys.exit(1)
        print("%d config vectors updated" % self.process_count)


if __name__ == '__main__':
    # check parameters and usage
    parser = argparse.ArgumentParser(description='Process Config Vectors', usage='%(prog)s [options]')
    parser.add_argument('action', choices=['add', 'delete', 'update'], help="Config Vector Actions Supported")
    parser.add_argument('-u', '--url', dest='url', required=True, help="Berta Server URL with authentication: https://user:password@ra-berta.jf.intel.com")
    parser.add_argument('-p', '--path', dest='path', required=True, help="Config Vector CSV Path")
    inputs = parser.parse_args()

    cv = ConfigVectorTool(inputs.url, inputs.path)
    method = '_config_vector_' + inputs.action
    try:
        eval('cv.' + method)()
    except Exception as e:
        print("Process error.")