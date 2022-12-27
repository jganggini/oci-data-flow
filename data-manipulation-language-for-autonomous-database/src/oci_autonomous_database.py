from src.parameters import *
import cx_Oracle
import os
import tempfile
import zipfile

class oci_autonomous_database(cx_Oracle.Connection):

    def __init__(self, *args, cloud_config=None, **kwargs):
        self.temp_dir = None
        self.tns_entries = {}
        if cloud_config is not None:
            self._setup_cloud_config(cloud_config)
            if len(args) > 2:
                dsn = args[2]
            else:
                dsn = kwargs.get('dsn')
            if dsn in self.tns_entries:
                dsn = self.tns_entries[dsn]
                if len(args) > 2:
                    args = args[:2] + (dsn,) + args[3:]
                else:
                    kwargs = kwargs.copy()
                    kwargs['dsn'] = dsn
        super(oci_autonomous_database, self).__init__(*args, **kwargs)

    def _setup_cloud_config(self, cloud_config):

        # extract files in wallet zip to a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        zipfile.ZipFile(cloud_config).extractall(self.temp_dir.name)

        # parse tnsnames.ora to get list of entries and modify them to include
        # the wallet location
        fname = os.path.join(self.temp_dir.name, 'tnsnames.ora')
        for line in open(fname):
            pos = line.find(' = ')
            if pos < 0:
                continue
            name = line[:pos]
            entry = line[pos + 3:].strip()
            key_phrase = '(security='
            pos = entry.find(key_phrase) + len(key_phrase)
            wallet_entry = '(MY_WALLET_DIRECTORY=%s)' % self.temp_dir.name
            entry = entry[:pos] + wallet_entry + entry[pos:]
            self.tns_entries[name] = entry

    # Delete row in ADB
    def delete_row(table_name, row_name, rowid):
        try:
            conn = oci_autonomous_database(oci_adb_user_name_1, oci_adb_password_1, oci_adb_service_name_1, cloud_config=oci_adb_wallet_location_1)
            
            # create a cursor
            with conn.cursor() as cursor:
                # execute the insert statement
                sql = 'DELETE FROM ' + table_name + ' WHERE ' + row_name + '=' + str(rowid)
                cursor.execute(sql)
                # commit the change
                conn.commit()

            print('  Delete object ([' + table_name  + '].[' + row_name + ']=' + str(rowid) + ')...[Succeded]\n')

        except cx_Oracle.Error as e:
            print(e)